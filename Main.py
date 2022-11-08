
from PyQt5 import QtCore, QtGui, QtWidgets

from Admin import Ui_Admin

from Employee import Ui_Employee

class Ui_Dialog(object):

    def adminlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def employelogin(self, event):
        try:
            self.emp = QtWidgets.QDialog()
            self.ui = Ui_Employee(self.emp)
            self.ui.setupUi(self.emp)
            self.emp.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 717)
        Dialog.setStyleSheet("background-color: rgb(216, 144, 108);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 50, 861, 81))
        self.label.setStyleSheet("font: 25pt \"Bauhaus 93\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 240, 301, 261))
        self.label_2.setStyleSheet("image: url(../EmotionsDetection/images/adminn.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent = self.adminlogin
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(191, 480, 211, 71))
        self.label_3.setStyleSheet("font: 15pt \"Bauhaus 93\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(660, 221, 231, 291))
        self.label_4.setStyleSheet("image: url(../EmotionsDetection/images/emple.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent = self.employelogin
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(730, 490, 190, 61))
        self.label_5.setStyleSheet("font: 15pt \"Bauhaus 93\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "Real time-Employee Emotion Detection system "))
        self.label_3.setText(_translate("Dialog", "Administrator"))
        self.label_5.setText(_translate("Dialog", "Employee"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
