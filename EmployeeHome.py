
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from EmotionDetection import Detection
class Ui_EmployeeHome(object):

    def __init__(self, emp_id):
        self.emp_id = emp_id

    def emotions_detection(self,event):
        try:
            Detection(self.emp_id)

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(854, 683)
        Dialog.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 110, 311, 291))
        self.label_3.setStyleSheet("image: url(../EmotionsDetection/images/emd.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = self.emotions_detection
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 400, 221, 31))
        self.label_4.setStyleSheet("font: 16pt \"Bahnschrift Condensed\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EmployeeHome"))
        self.label_4.setText(_translate("Dialog", "Emotions Detections"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_EmployeeHome("a")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
