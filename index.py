# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/front.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from dateutil.relativedelta import relativedelta

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"
    
class Ui_MainWindow(object):
    def setupUi(self, Form):
        #? UI Content
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(374, 490)
        Form.setMinimumSize(QtCore.QSize(374, 490))
        Form.setMaximumSize(QtCore.QSize(374, 490))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 331, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.NgaySinh = QtWidgets.QDateEdit(self.tab)
        self.NgaySinh.setGeometry(QtCore.QRect(190, 180, 110, 22))
        self.NgaySinh.setDate(QtCore.QDate(2006, 1, 1))
        self.NgaySinh.setObjectName("NgaySinh")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 271, 41))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 91, 16))
        self.label_3.setObjectName("label_3")
        self.normal_result = QtWidgets.QLabel(self.tab)
        self.normal_result.setGeometry(QtCore.QRect(30, 320, 271, 51))
        self.normal_result.setObjectName("normal_result")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 181, 71))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.label_5.setObjectName("label_5")
        self.age = QtWidgets.QSpinBox(self.tab_2)
        self.age.setGeometry(QtCore.QRect(210, 180, 71, 20))
        self.age.setMinimum(1)
        self.age.setMaximum(200)
        self.age.setSingleStep(1)
        self.age.setProperty("value", 1)
        self.age.setObjectName("age")
        self.smart_result = QtWidgets.QLabel(self.tab_2)
        self.smart_result.setGeometry(QtCore.QRect(30, 320, 271, 51))
        self.smart_result.setObjectName("smart_result")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 280, 91, 16))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        #? UI Style
        self.smart_result.setStyleSheet("font-weight: bold; text-align: center; font-size: 27px;")
        self.normal_result.setStyleSheet("font-weight: bold; text-align: center; font-size: 27px;")

        #? Event
        self.NgaySinh.dateChanged.connect(self.NormalChanged)
        self.age.valueChanged.connect(self.SmartChanged)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Máy tính tuổi"))
        self.label.setText(_translate("Form", "Ngày sinh của bạn:"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MÁY TÍNH TUỔI THƯỜNG</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Số tuổi của bạn là: "))
        self.normal_result.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Thường"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">MÁY TÍNH TUỔI</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">THÔNG MINH</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "Nhập số tuổi của bạn:"))
        self.smart_result.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_9.setText(_translate("Form", "Số tuổi của bạn là: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Thông minh"))

    def NormalChanged(self, date):
        rdelta = relativedelta(datetime.now().date(), date.toPyDate())
        if (rdelta.years<0):
            self.normal_result.setText("Bạn chưa sinh ra")
        else:
            self.normal_result.setText(str(rdelta.years))
    def SmartChanged(self, number):
        self.smart_result.setText(str(number))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())