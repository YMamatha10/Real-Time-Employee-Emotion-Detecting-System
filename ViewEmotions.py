

from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection


class VieEmotions(object):

    def emotionslist(self):
        try:
            mydb = DBConnection.getConnection()
            cursor = mydb.cursor()
            query= "select *from emotions"
            cursor.execute(query)
            row = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.tableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1225, 800)
        Dialog.setStyleSheet("QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(175, 77, 227, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(100, 90, 1051, 631))
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(112, 82, 44, 170), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 10, 421, 61))
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(143, 102, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(170, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 350)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Emotions"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Employee Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Emotions"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date"))
        self.label.setText(_translate("Dialog", "View Emotions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = VieEmotions()
    ui.setupUi(Dialog)
    ui.emotionslist()
    Dialog.show()
    sys.exit(app.exec_())
