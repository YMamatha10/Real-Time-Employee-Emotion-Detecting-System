
from PyQt5 import QtCore, QtGui, QtWidgets

from ModelEvaluations import calculate_accuracy
from ViewEmotions import VieEmotions
from BuildModel import build_model

class Ui_AdminHome(object):

    def build_model(self, event):
        try:
            build_model()
            self.showMessageBox("Information","Models are Trained successfully")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()


    def model_evaluations(self, event):

        calculate_accuracy()

        event.accept()


    def view_emotions(self, event):
        try:
            self.ve = QtWidgets.QDialog()
            self.ui = VieEmotions()
            self.ui.setupUi(self.ve)
            self.ui.emotionslist()
            self.ve.show()


        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(956, 738)
        Dialog.setStyleSheet("background-color: rgb(216, 108, 162);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 200, 261, 221))
        self.label.setStyleSheet("image: url(../EmotionsDetection/images/model.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.mousePressEvent = self.build_model
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 432, 221, 81))
        self.label_2.setStyleSheet("font: 16pt \"Bahnschrift Condensed\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 190, 211, 251))
        self.label_3.setStyleSheet("image: url(../EmotionsDetection/images/eval.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = self.model_evaluations
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(366, 430, 221, 81))
        self.label_4.setStyleSheet("font: 16pt \"Bahnschrift Condensed\";")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(690, 190, 231, 261))
        self.label_5.setStyleSheet("image: url(../EmotionsDetection/images/viewmotins.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.mousePressEvent = self.view_emotions
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(720, 430, 221, 81))
        self.label_6.setStyleSheet("font: 16pt \"Bahnschrift Condensed\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.label_2.setText(_translate("Dialog", "Build Models"))
        self.label_4.setText(_translate("Dialog", "Models Evaluations"))
        self.label_6.setText(_translate("Dialog", "Employee Emotions"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
