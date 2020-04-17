# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myCalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(938, 699)
        MainWindow.setMinimumSize(QtCore.QSize(60, 45))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(100, 270, 771, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:40px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color:#e7e7e7;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(42)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 350, 331, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_rand = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_rand.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_rand.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_rand.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_rand.setObjectName("pushButton_rand")
        self.gridLayout.addWidget(self.pushButton_rand, 3, 3, 1, 1)
        self.pushButton_inverse = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_inverse.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_inverse.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_inverse.setFont(font)
        self.pushButton_inverse.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_inverse.setObjectName("pushButton_inverse")
        self.gridLayout.addWidget(self.pushButton_inverse, 4, 0, 1, 1)
        self.pushButton_sin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sin.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_sin.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.gridLayout.addWidget(self.pushButton_sin, 2, 0, 1, 1)
        self.pushButton_cos = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cos.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_cos.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.gridLayout.addWidget(self.pushButton_cos, 2, 1, 1, 1)
        self.pushButton_tan = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_tan.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_tan.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_tan.setFont(font)
        self.pushButton_tan.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_tan.setObjectName("pushButton_tan")
        self.gridLayout.addWidget(self.pushButton_tan, 2, 2, 1, 1)
        self.pushButton_rad = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_rad.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_rad.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_rad.setFont(font)
        self.pushButton_rad.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_rad.setObjectName("pushButton_rad")
        self.gridLayout.addWidget(self.pushButton_rad, 2, 3, 1, 1)
        self.pushButton_square = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_square.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_square.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_square.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_square.setObjectName("pushButton_square")
        self.gridLayout.addWidget(self.pushButton_square, 1, 0, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sqrt.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_sqrt.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 1, 1, 1, 1)
        self.pushButton_log = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_log.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_log.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_log.setFont(font)
        self.pushButton_log.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_log.setObjectName("pushButton_log")
        self.gridLayout.addWidget(self.pushButton_log, 1, 2, 1, 1)
        self.pushButton_ln = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ln.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_ln.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_ln.setFont(font)
        self.pushButton_ln.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.gridLayout.addWidget(self.pushButton_ln, 1, 3, 1, 1)
        self.pushButton_factorial = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_factorial.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_factorial.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_factorial.setFont(font)
        self.pushButton_factorial.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.gridLayout.addWidget(self.pushButton_factorial, 3, 2, 1, 1)
        self.pushButton_rightpart = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_rightpart.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_rightpart.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_rightpart.setFont(font)
        self.pushButton_rightpart.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_rightpart.setObjectName("pushButton_rightpart")
        self.gridLayout.addWidget(self.pushButton_rightpart, 3, 1, 1, 1)
        self.pushButton_leftpart = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_leftpart.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_leftpart.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_leftpart.setFont(font)
        self.pushButton_leftpart.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_leftpart.setObjectName("pushButton_leftpart")
        self.gridLayout.addWidget(self.pushButton_leftpart, 3, 0, 1, 1)
        self.pushButton_power = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_power.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_power.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_power.setFont(font)
        self.pushButton_power.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_power.setObjectName("pushButton_power")
        self.gridLayout.addWidget(self.pushButton_power, 4, 1, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_percent.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_percent.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_percent.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 4, 2, 1, 1)
        self.pushButton_exp = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_exp.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_exp.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_exp.setFont(font)
        self.pushButton_exp.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_exp.setObjectName("pushButton_exp")
        self.gridLayout.addWidget(self.pushButton_exp, 4, 3, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(420, 350, 271, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_9.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_7.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_0.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_0.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout_2.addWidget(self.pushButton_0, 4, 0, 1, 1)
        self.pushButton_pi = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_pi.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_pi.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_pi.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_pi.setObjectName("pushButton_pi")
        self.gridLayout_2.addWidget(self.pushButton_pi, 4, 3, 1, 1)
        self.pushButton_point = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_point.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_point.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout_2.addWidget(self.pushButton_point, 4, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_1.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_1.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_5.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_6.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(690, 350, 181, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_AC = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_AC.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_AC.setMaximumSize(QtCore.QSize(60, 55))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_AC.setFont(font)
        self.pushButton_AC.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(126, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.horizontalLayout.addWidget(self.pushButton_AC)
        self.pushButton_DEL = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_DEL.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_DEL.setMaximumSize(QtCore.QSize(60, 55))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_DEL.setFont(font)
        self.pushButton_DEL.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(126, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.horizontalLayout.addWidget(self.pushButton_DEL)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(690, 420, 181, 191))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_mul = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_mul.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout_3.addWidget(self.pushButton_mul, 0, 0, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_div.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_div.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout_3.addWidget(self.pushButton_div, 0, 1, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_plus.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_plus.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setAutoFillBackground(False)
        self.pushButton_plus.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout_3.addWidget(self.pushButton_plus, 1, 0, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_sub.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout_3.addWidget(self.pushButton_sub, 1, 1, 1, 1)
        self.pushButton_e = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_e.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_e.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_e.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_e.setObjectName("pushButton_e")
        self.gridLayout_3.addWidget(self.pushButton_e, 2, 0, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_equal.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_equal.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setAutoFillBackground(False)
        self.pushButton_equal.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(0, 0, 0);\n"
"color:white;\n"
"")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout_3.addWidget(self.pushButton_equal, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 70, 771, 191))
        self.textBrowser.setStyleSheet("font: 18pt \".SF NS Text\";")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(50, 350, 22, 261))
        self.verticalSlider.setMaximum(9)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setProperty("value", 5)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 270, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_2.setText(_translate("MainWindow", "QiangZiBro"))
        self.pushButton_rand.setText(_translate("MainWindow", "Rand"))
        self.pushButton_inverse.setText(_translate("MainWindow", "1/x"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_tan.setText(_translate("MainWindow", "tan"))
        self.pushButton_rad.setText(_translate("MainWindow", "Rad"))
        self.pushButton_square.setText(_translate("MainWindow", "x²"))
        self.pushButton_sqrt.setText(_translate("MainWindow", "√"))
        self.pushButton_log.setText(_translate("MainWindow", "log"))
        self.pushButton_ln.setText(_translate("MainWindow", "ln"))
        self.pushButton_factorial.setText(_translate("MainWindow", "n!"))
        self.pushButton_rightpart.setText(_translate("MainWindow", ")"))
        self.pushButton_leftpart.setText(_translate("MainWindow", "("))
        self.pushButton_power.setText(_translate("MainWindow", "x^y"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_exp.setText(_translate("MainWindow", "EXP"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_pi.setText(_translate("MainWindow", "π"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_AC.setText(_translate("MainWindow", "AC"))
        self.pushButton_DEL.setText(_translate("MainWindow", "DEL"))
        self.pushButton_mul.setText(_translate("MainWindow", "×"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_e.setText(_translate("MainWindow", "e"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Baoli SC\';\"><br /></p></body></html>"))


