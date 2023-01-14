# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewRecipe.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewRecipeWindow(object):
    def setupUi(self, ViewRecipeWindow):
        ViewRecipeWindow.setObjectName("ViewRecipeWindow")
        ViewRecipeWindow.resize(1200, 900)
        ViewRecipeWindow.setMinimumSize(QtCore.QSize(1200, 900))
        ViewRecipeWindow.setMaximumSize(QtCore.QSize(1200, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("325314459_826693388428270_2168916561632903173_n.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ViewRecipeWindow.setWindowIcon(icon)
        ViewRecipeWindow.setStyleSheet("background-color: white;")
        self.viewRecipeScreen = QtWidgets.QWidget(ViewRecipeWindow)
        self.viewRecipeScreen.setObjectName("viewRecipeScreen")
        self.recipeName = QtWidgets.QLabel(self.viewRecipeScreen)
        self.recipeName.setGeometry(QtCore.QRect(600, 0, 281, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        self.recipeName.setFont(font)
        self.recipeName.setStyleSheet("color: rgb(49, 87, 44)")
        self.recipeName.setAlignment(QtCore.Qt.AlignCenter)
        self.recipeName.setObjectName("recipeName")
        self.recipePicture = QtWidgets.QLabel(self.viewRecipeScreen)
        self.recipePicture.setGeometry(QtCore.QRect(70, 20, 450, 250))
        self.recipePicture.setStyleSheet("border-style: solid;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);\n"
"")
        self.recipePicture.setText("")
        self.recipePicture.setPixmap(QtGui.QPixmap("default-placeholder.png"))
        self.recipePicture.setScaledContents(True)
        self.recipePicture.setObjectName("recipePicture")
        self.deleteButton = QtWidgets.QPushButton(self.viewRecipeScreen)
        self.deleteButton.setGeometry(QtCore.QRect(600, 190, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setAccessibleDescription("")
        self.deleteButton.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.deleteButton.setObjectName("deleteButton")
        self.createListButton = QtWidgets.QPushButton(self.viewRecipeScreen)
        self.createListButton.setGeometry(QtCore.QRect(870, 190, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.createListButton.setFont(font)
        self.createListButton.setAccessibleDescription("")
        self.createListButton.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.createListButton.setObjectName("createListButton")
        self.lickButton = QtWidgets.QPushButton(self.viewRecipeScreen)
        self.lickButton.setGeometry(QtCore.QRect(600, 100, 520, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.lickButton.setFont(font)
        self.lickButton.setAccessibleDescription("")
        self.lickButton.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.lickButton.setObjectName("lickButton")
        self.listOfSteps = QtWidgets.QListWidget(self.viewRecipeScreen)
        self.listOfSteps.setGeometry(QtCore.QRect(70, 330, 1050, 260))
        self.listOfSteps.setStyleSheet("border-color: rgb(49, 87, 44);\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.listOfSteps.setObjectName("listOfSteps")
        self.stepsTitle = QtWidgets.QLabel(self.viewRecipeScreen)
        self.stepsTitle.setGeometry(QtCore.QRect(70, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.stepsTitle.setFont(font)
        self.stepsTitle.setStyleSheet("color: rgb(49, 87, 44)")
        self.stepsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.stepsTitle.setObjectName("stepsTitle")
        self.listOfIngredients = QtWidgets.QListWidget(self.viewRecipeScreen)
        self.listOfIngredients.setGeometry(QtCore.QRect(70, 650, 500, 220))
        self.listOfIngredients.setStyleSheet("border-color: rgb(49, 87, 44);\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"")
        self.listOfIngredients.setObjectName("listOfIngredients")
        self.listOfTimers = QtWidgets.QListWidget(self.viewRecipeScreen)
        self.listOfTimers.setGeometry(QtCore.QRect(620, 650, 500, 220))
        self.listOfTimers.setStyleSheet("border-color: rgb(49, 87, 44);\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"")
        self.listOfTimers.setObjectName("listOfTimers")
        self.ingredientsTitle = QtWidgets.QLabel(self.viewRecipeScreen)
        self.ingredientsTitle.setGeometry(QtCore.QRect(70, 600, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.ingredientsTitle.setFont(font)
        self.ingredientsTitle.setStyleSheet("color: rgb(49, 87, 44)")
        self.ingredientsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.ingredientsTitle.setObjectName("ingredientsTitle")
        self.timersTitle = QtWidgets.QLabel(self.viewRecipeScreen)
        self.timersTitle.setGeometry(QtCore.QRect(620, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.timersTitle.setFont(font)
        self.timersTitle.setStyleSheet("color: rgb(49, 87, 44)")
        self.timersTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.timersTitle.setObjectName("timersTitle")
        ViewRecipeWindow.setCentralWidget(self.viewRecipeScreen)
        self.statusbar = QtWidgets.QStatusBar(ViewRecipeWindow)
        self.statusbar.setObjectName("statusbar")
        ViewRecipeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewRecipeWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewRecipeWindow)

    def retranslateUi(self, ViewRecipeWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewRecipeWindow.setWindowTitle(_translate("ViewRecipeWindow", "PoLIZANE "))
        self.recipeName.setText(_translate("ViewRecipeWindow", "Recipe name"))
        self.deleteButton.setStatusTip(_translate("ViewRecipeWindow", "Delete your recipe"))
        self.deleteButton.setText(_translate("ViewRecipeWindow", "Delete"))
        self.createListButton.setStatusTip(_translate("ViewRecipeWindow", "Create shopping list out of your recipe"))
        self.createListButton.setText(_translate("ViewRecipeWindow", "Create List"))
        self.lickButton.setStatusTip(_translate("ViewRecipeWindow", "Lick your recipe"))
        self.lickButton.setText(_translate("ViewRecipeWindow", "Lick"))
        self.stepsTitle.setText(_translate("ViewRecipeWindow", "Steps"))
        self.ingredientsTitle.setText(_translate("ViewRecipeWindow", "Ingredients"))
        self.timersTitle.setText(_translate("ViewRecipeWindow", "Timers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewRecipeWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewRecipeWindow()
    ui.setupUi(ViewRecipeWindow)
    ViewRecipeWindow.show()
    sys.exit(app.exec_())
