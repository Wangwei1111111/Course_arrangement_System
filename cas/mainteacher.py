# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainteacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainteacher(object):
    def setupUi(self, mainteacher):
        mainteacher.setObjectName("mainteacher")
        mainteacher.resize(997, 586)
        self.tableView = QtWidgets.QTableView(mainteacher)
        self.tableView.setGeometry(QtCore.QRect(30, 40, 791, 471))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(mainteacher)
        self.label.setGeometry(QtCore.QRect(30, 20, 72, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(mainteacher)
        self.pushButton.setGeometry(QtCore.QRect(860, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(mainteacher)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(mainteacher)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 220, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(mainteacher)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 290, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(mainteacher)
        QtCore.QMetaObject.connectSlotsByName(mainteacher)

    def retranslateUi(self, mainteacher):
        _translate = QtCore.QCoreApplication.translate
        mainteacher.setWindowTitle(_translate("mainteacher", "Form"))
        self.label.setText(_translate("mainteacher", "教师列表"))
        self.pushButton.setText(_translate("mainteacher", "增加教师"))
        self.pushButton_2.setText(_translate("mainteacher", "删除教师"))
        self.pushButton_3.setText(_translate("mainteacher", "查看课时明细"))
        self.pushButton_4.setText(_translate("mainteacher", "提交修改"))
