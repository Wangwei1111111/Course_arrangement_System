# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noteacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_noteacher(object):
    def setupUi(self, noteacher):
        noteacher.setObjectName("noteacher")
        noteacher.resize(945, 588)
        self.tableView = QtWidgets.QTableView(noteacher)
        self.tableView.setGeometry(QtCore.QRect(40, 30, 256, 491))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(noteacher)
        self.tableView_2.setGeometry(QtCore.QRect(360, 30, 256, 491))
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton = QtWidgets.QPushButton(noteacher)
        self.pushButton.setGeometry(QtCore.QRect(730, 400, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(noteacher)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 450, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(noteacher)
        self.label.setGeometry(QtCore.QRect(40, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(noteacher)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(noteacher)
        self.checkBox.setGeometry(QtCore.QRect(720, 120, 171, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(noteacher)
        self.checkBox_2.setGeometry(QtCore.QRect(720, 150, 171, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(noteacher)
        self.checkBox_3.setGeometry(QtCore.QRect(720, 180, 171, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(noteacher)
        self.checkBox_4.setGeometry(QtCore.QRect(720, 210, 171, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(noteacher)
        self.checkBox_5.setGeometry(QtCore.QRect(720, 240, 171, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(noteacher)
        self.checkBox_6.setGeometry(QtCore.QRect(720, 270, 171, 19))
        self.checkBox_6.setObjectName("checkBox_6")

        self.retranslateUi(noteacher)
        QtCore.QMetaObject.connectSlotsByName(noteacher)

    def retranslateUi(self, noteacher):
        _translate = QtCore.QCoreApplication.translate
        noteacher.setWindowTitle(_translate("noteacher", "Form"))
        self.pushButton.setText(_translate("noteacher", "增加"))
        self.pushButton_2.setText(_translate("noteacher", "删除"))
        self.label.setText(_translate("noteacher", "老师列表"))
        self.label_2.setText(_translate("noteacher", "老师不能上课时间"))
        self.checkBox.setText(_translate("noteacher", "8：00-10：00不能上"))
        self.checkBox_2.setText(_translate("noteacher", "10：00-12：00不能上"))
        self.checkBox_3.setText(_translate("noteacher", "12：00-2：00不能上"))
        self.checkBox_4.setText(_translate("noteacher", "2：00-4：00不能上"))
        self.checkBox_5.setText(_translate("noteacher", "4：00-6：00不能上"))
        self.checkBox_6.setText(_translate("noteacher", "7：00-9：00不能上"))
