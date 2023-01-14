# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_step.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../sof-eng/PoLIZANE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 490, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.save_button.setObjectName("save_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(610, 490, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.delete_button.setObjectName("delete_button")
        self.add_step_label = QtWidgets.QLabel(self.centralwidget)
        self.add_step_label.setGeometry(QtCore.QRect(350, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        self.add_step_label.setFont(font)
        self.add_step_label.setStyleSheet("color: rgb(49, 87, 44);")
        self.add_step_label.setObjectName("add_step_label")
        self.step_description_areatext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.step_description_areatext.setGeometry(QtCore.QRect(40, 90, 820, 350))
        self.step_description_areatext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.step_description_areatext.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);\n"
"placeholder {\n"
"  color: rgb(49, 87, 44, 75);\n"
"};\n"
" font-size: 24px;")
        self.step_description_areatext.setObjectName("step_description_areatext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PoLIZANE"))
        self.save_button.setStatusTip(_translate("MainWindow", "Click save to add step to the Recipe"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.delete_button.setStatusTip(_translate("MainWindow", "Click delete if you don\'t want to add this step to the recipe"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.add_step_label.setStatusTip(_translate("MainWindow", "Add step"))
        self.add_step_label.setText(_translate("MainWindow", "Add step"))
        self.step_description_areatext.setStatusTip(_translate("MainWindow", "Type description of the step here"))
        self.step_description_areatext.setPlaceholderText(_translate("MainWindow", "Step description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
