import os
from keras.preprocessing import image
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
import pickle
import numpy as np
from sklearn.svm import SVC
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from CNN_Training import build_cnnmodel
def build_model():
    try:

        print("[INFO] Loading Training dataset images...")
        DIRECTORY = "..\EmotionsDetection\dataset\\train"
        CATEGORIES = ['angry', 'disgust','fear','happy','neutral','sad']

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

        x_train = np.array(data)
        x_train = x_train.reshape(len(x_train), -1)
        y_train = np.array(clas)

        print("[INFO] Image Processing completed")

        #x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.3, random_state=42)

        #NN
        print("[INFO] Training NN model...")
        clf_mlp = MLPClassifier()
        clf_mlp.fit(x_train, y_train)
        #predicted = clf_mlp.predict(x_test)
        #accuracy_mlp = accuracy_score(y_test, predicted) * 100
        with open('NN.model', 'wb') as f:
            pickle.dump(clf_mlp, f)
        print("[INFO] NN model created successfully..!")

        #SVM
        print("[INFO] Training SVM model...")
        clf_svm =SVC(kernel='linear',decision_function_shape='ovr')
        clf_svm.fit(x_train, y_train)
        with open('SVM.model', 'wb') as f:
            pickle.dump(clf_svm, f)
        #predicted = clf_svm.predict(x_test)
        #accuracy_svm = accuracy_score(y_test, predicted) * 100
        print("[INFO]  SVM model created successfully..!")

        build_cnnmodel()



    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)

#build_model()

