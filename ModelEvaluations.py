import os
import numpy as np
from keras.preprocessing import image
import cv2
import sys
import pickle
from sklearn import metrics
from keras.models import load_model
from utils.inference import detect_faces
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input
from sklearn.metrics import accuracy_score
from Graph import view
def calculate_accuracy():
    detection_model_path = '../EmotionsDetection/haarcascade_frontalface_default.xml'
    emotion_model_path = '../EmotionsDetection/cnn_model.hdf5'
    emotion_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

    # hyper-parameters for bounding boxes shape
    frame_window = 10
    emotion_offsets = (20, 40)
    emotion_text = ""

    # loading models
    face_detection = load_detection_model(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)

    # getting input model shapes for inference
    emotion_target_size = emotion_classifier.input_shape[1:3]
    DIRECTORY = "../EmotionsDetection/testing"
    CATEGORIES = [ "Angry", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

    predicted = []
    actual = []
    for category in CATEGORIES:
        path = os.path.join(DIRECTORY, category)
        for img in os.listdir(path):
            bgr_image = cv2.imread(path + "/" +str(img))
            # print(bgr_image)
            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
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
                emotion_label_arg = np.argmax(emotion_prediction)
                emotion_text = emotion_labels[emotion_label_arg]
            predicted.append(emotion_text)
            actual.append(category)
    correct = 0
    for x in range(len(predicted)):
        if predicted[x] == actual[x]:
            correct += 1
    accuracy_cnn = (correct / float(len(actual)) * 100.0)
    print("Algorithm Performance")
    print("===============================================")
    print("CNN Accuracy = ",accuracy_cnn)




    DIRECTORY = "../EmotionsDetection/testing"
    CATEGORIES = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad','surprise']

    data = []
    clas = []

    for category in CATEGORIES[:2]:

        path = os.path.join(DIRECTORY, category)

        for img in os.listdir(path)[:150]:
            img_path = os.path.join(path, img)
            img = image.load_img(img_path, target_size=(128, 128))
            img = image.img_to_array(img)
            img = img / 255
            data.append(img)
            clas.append(category)

    x_test = np.array(data)
    x_test = x_test.reshape(len(x_test), -1)
    y_test = np.array(clas)




    print("CALCULATING SVM ACCURACY......")
    svm_model = open('../EmotionsDetection/SVM.model', 'rb')
    clf_svm = pickle.load(svm_model)
    predicted = clf_svm.predict(x_test)
    accuracy_svm = accuracy_score(y_test, predicted) * 100
    print("SVM Accuracy = ",accuracy_svm)

    print("CALCULATING NN ACCURACY......")
    nn_model = open('../EmotionsDetection/NN.model', 'rb')
    clf_nn = pickle.load(nn_model)
    predicted = clf_nn.predict(x_test)
    accuracy_nn = accuracy_score(y_test, predicted) * 100
    print("NN Accuracy = ", accuracy_nn)

    list =[]
    list.append(accuracy_svm)
    list.append(accuracy_nn)
    list.append(accuracy_cnn)

    view(list)



#calculate_accuracy()
