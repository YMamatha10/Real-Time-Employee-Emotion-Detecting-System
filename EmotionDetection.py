from statistics import mode
import os
import cv2
from keras.models import load_model
import numpy as np
import sys
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input

from DBConnection import DBConnection


def Detection(emp_id):

        try:
            # parameters for loading data and images
            detection_model_path = '../EmotionsDetection/haarcascade_frontalface_default.xml'
            emotion_model_path = '../EmotionsDetection/cnn_model.hdf5'
            emotion_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

            # hyper-parameters for bounding boxes shape
            frame_window = 10
            emotion_offsets = (20, 40)

            # loading models
            face_detection = load_detection_model(detection_model_path)
            emotion_classifier = load_model(emotion_model_path, compile=False)

            # getting input model shapes for inference
            emotion_target_size = emotion_classifier.input_shape[1:3]

            # starting lists for calculating modes
            emotion_window = []

            # starting video streaming
            #cv2.namedWindow('Face Expression Recognition')
            video_capture = cv2.VideoCapture(0)
            while True:
                bgr_image = video_capture.read()[1]
                gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
                rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
                faces = detect_faces(face_detection, gray_image)

                for face_coordinates in faces:

                    x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
                    gray_face = gray_image[y1:y2, x1:x2]
                    try:
                        gray_face = cv2.resize(gray_face, (emotion_target_size))
                    except:
                        continue

                    gray_face = preprocess_input(gray_face, True)
                    gray_face = np.expand_dims(gray_face, 0)
                    gray_face = np.expand_dims(gray_face, -1)
                    emotion_prediction = emotion_classifier.predict(gray_face)
                    emotion_probability = np.max(emotion_prediction)
                    emotion_label_arg = np.argmax(emotion_prediction)
                    emotion_text = emotion_labels[emotion_label_arg]
                    emotion_window.append(emotion_text)

                    if len(emotion_window) > frame_window:
                        emotion_window.pop(0)
                    try:
                        emotion_mode = mode(emotion_window)
                    except:
                        continue

                    if emotion_text == 'Angry':
                        color = emotion_probability * np.asarray((255, 0, 0))
                    elif emotion_text == 'Sad':
                        color = emotion_probability * np.asarray((0, 0, 255))
                    elif emotion_text == 'Happy':
                        color = emotion_probability * np.asarray((255, 255, 0))
                    elif emotion_text == 'Surprise':
                        color = emotion_probability * np.asarray((0, 255, 255))
                    elif emotion_text == 'Neutral':
                        color = emotion_probability * np.asarray((0, 255, 255))
                    elif emotion_text == 'Fear':
                        color = emotion_probability * np.asarray((0, 255, 255))
                    else:
                        color = emotion_probability * np.asarray((0, 255, 0))
                    color = color.astype(int)
                    color = color.tolist()

                    draw_bounding_box(face_coordinates, rgb_image, color)
                    draw_text(face_coordinates, rgb_image, emotion_mode, color, 30, 290, 1, 1)

                bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
                cv2.imshow('Employee Emotions Detection', bgr_image)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    database = DBConnection.getConnection()
                    cursor = database.cursor()
                    sql = "insert into emotions values(%s,%s,now())"
                    values = (emp_id, emotion_text)
                    cursor.execute(sql, values)
                    database.commit()

                   # break
                    video_capture.release()
                    cv2.destroyAllWindows()




        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
#Detection("a")