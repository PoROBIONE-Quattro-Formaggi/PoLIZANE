# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recpie_screen.ui'
#
# Created by: PyQt5 ui_designs code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui.lists_window import Ui_lists_window
from ui.ingredients_window import Ui_ingredients_window


# noinspection PyArgumentList,PyAttributeOutsideInit,PyPep8Naming,PyShadowingNames
class Ui_recpie_window(object):
    def open_lists(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_lists_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_fridge(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ingredients_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, recpie_window):
        recpie_window.setObjectName("recpie_window")
        recpie_window.resize(1200, 800)
        recpie_window.setMinimumSize(QtCore.QSize(1200, 800))
        recpie_window.setMaximumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo/polizane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        recpie_window.setWindowIcon(icon)
        recpie_window.setStatusTip("")
        recpie_window.setStyleSheet("background-color: rgb(49, 87, 44);\n"
                                    "color: rgb(255, 255, 255);")
        self.recpie_screen = QtWidgets.QWidget(recpie_window)
        self.recpie_screen.setObjectName("recpie_screen")
        self.add_button = QtWidgets.QPushButton(self.recpie_screen)
        self.add_button.setGeometry(QtCore.QRect(30, 20, 300, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: rgb(49, 87, 44);\n"
                                      "color: white;\n"
                                      "border-radius: 12px;\n"
                                      "border-width: 2px;\n"
                                      "border-color: white;\n"
                                      "border-style: outset;")
        self.add_button.setObjectName("add_button")
        self.go_to_lists_button = QtWidgets.QPushButton(self.recpie_screen, clicked=lambda: self.open_lists())
        self.go_to_lists_button.setGeometry(QtCore.QRect(920, 20, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.go_to_lists_button.setFont(font)
        self.go_to_lists_button.setStyleSheet("background-color: white;\n"
                                              "color: rgb(49, 87, 44);\n"
                                              "border-radius: 12px;")
        self.go_to_lists_button.setObjectName("go_to_lists_button")
        self.go_to_fridge_button = QtWidgets.QPushButton(self.recpie_screen, clicked=lambda: self.open_fridge())
        self.go_to_fridge_button.setGeometry(QtCore.QRect(650, 20, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.go_to_fridge_button.setFont(font)
        self.go_to_fridge_button.setStyleSheet("background-color: white;\n"
                                               "color: rgb(49, 87, 44);\n"
                                               "border-radius: 12px;")
        self.go_to_fridge_button.setObjectName("go_to_fridge_button")
        self.filter = QtWidgets.QRadioButton(self.recpie_screen)
        self.filter.setGeometry(QtCore.QRect(30, 730, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.filter.setFont(font)
        self.filter.setStyleSheet("QRadioButton {\n"
                                  "    background-color:       rgb(49, 87, 44);\n"
                                  "    color:                  white;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator {\n"
                                  "    width:                  10px;\n"
                                  "    height:                 10px;\n"
                                  "    border-radius:          7px;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator:checked {\n"
                                  "    background-color:       white;\n"
                                  "    border:                 2px solid white;\n"
                                  "}\n"
                                  "\n"
                                  "QRadioButton::indicator:unchecked {\n"
                                  "    background-color:       rgb(49, 87, 44);\n"
                                  "    border:                 2px solid white;\n"
                                  "}")
        self.filter.setObjectName("filter")
        self.display = QtWidgets.QListWidget(self.recpie_screen)
        self.display.setGeometry(QtCore.QRect(30, 130, 1141, 571))
        self.display.setStyleSheet("border-color: rgb(49, 87, 44);\n"
                                   "border-width: 0px;\n"
                                   "border-style: outset;")
        self.display.setObjectName("display")
        recpie_window.setCentralWidget(self.recpie_screen)
        self.statusbar = QtWidgets.QStatusBar(recpie_window)
        self.statusbar.setObjectName("statusbar")
        recpie_window.setStatusBar(self.statusbar)

        self.retranslateUi(recpie_window)
        QtCore.QMetaObject.connectSlotsByName(recpie_window)

    def retranslateUi(self, recpie_window):
        _translate = QtCore.QCoreApplication.translate
        recpie_window.setWindowTitle(_translate("recpie_window", "PoLIZANE"))
        self.add_button.setStatusTip(
            _translate("recpie_window", "Click this button to add a new recpie to the database"))
        self.add_button.setText(_translate("recpie_window", "+"))
        self.go_to_lists_button.setStatusTip(_translate("recpie_window", "Open lists window"))
        self.go_to_lists_button.setText(_translate("recpie_window", "Lists"))
        self.go_to_fridge_button.setStatusTip(_translate("recpie_window", "Open fridge window"))
        self.go_to_fridge_button.setText(_translate("recpie_window", "Fridge"))
        self.filter.setStatusTip(_translate("recpie_window",
                                            "Click to show only the recpies that you can make based on the contents "
                                            "of the virtual fridge"))
        self.filter.setText(_translate("recpie_window", "Filter ready to make"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    recpie_window = QtWidgets.QMainWindow()
    ui = Ui_recpie_window()
    ui.setupUi(recpie_window)
    recpie_window.show()
    sys.exit(app.exec_())
