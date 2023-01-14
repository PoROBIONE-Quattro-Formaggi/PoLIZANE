# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingredients_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ingredients_window(object):
    def setupUi(self, ingredients_window):
        ingredients_window.setObjectName("ingredients_window")
        ingredients_window.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ingredients_window.sizePolicy().hasHeightForWidth())
        ingredients_window.setSizePolicy(sizePolicy)
        ingredients_window.setMinimumSize(QtCore.QSize(1200, 800))
        ingredients_window.setMaximumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo/polizane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ingredients_window.setWindowIcon(icon)
        ingredients_window.setStatusTip("")
        ingredients_window.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: rgb(255, 255, 255);")
        ingredients_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.ingredients_screen = QtWidgets.QWidget(ingredients_window)
        self.ingredients_screen.setObjectName("ingredients_screen")
        self.add_button = QtWidgets.QPushButton(self.ingredients_screen)
        self.add_button.setGeometry(QtCore.QRect(30, 20, 1150, 80))
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
        self.display = QtWidgets.QListWidget(self.ingredients_screen)
        self.display.setGeometry(QtCore.QRect(30, 130, 1150, 571))
        self.display.setStyleSheet("border-color: rgb(49, 87, 44);\n"
"border-width: 0px;\n"
"border-style: outset;")
        self.display.setObjectName("display")
        ingredients_window.setCentralWidget(self.ingredients_screen)
        self.statusbar = QtWidgets.QStatusBar(ingredients_window)
        self.statusbar.setObjectName("statusbar")
        ingredients_window.setStatusBar(self.statusbar)

        self.retranslateUi(ingredients_window)
        QtCore.QMetaObject.connectSlotsByName(ingredients_window)

    def retranslateUi(self, ingredients_window):
        _translate = QtCore.QCoreApplication.translate
        ingredients_window.setWindowTitle(_translate("ingredients_window", "PoLIZANE - INGREDIENTS"))
        self.add_button.setStatusTip(_translate("ingredients_window", "Click this button to add a new list to the database"))
        self.add_button.setText(_translate("ingredients_window", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ingredients_window = QtWidgets.QMainWindow()
    ui = Ui_ingredients_window()
    ui.setupUi(ingredients_window)
    ingredients_window.show()
    sys.exit(app.exec_())
