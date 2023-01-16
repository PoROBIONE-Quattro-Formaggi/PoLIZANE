# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_recipe.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_recipe_window(object):
    def setupUi(self, add_recipe_window):
        add_recipe_window.setObjectName("add_recipe_window")
        add_recipe_window.resize(1400, 1000)
        add_recipe_window.setMinimumSize(QtCore.QSize(1400, 1000))
        add_recipe_window.setMaximumSize(QtCore.QSize(1400, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PoLIZANE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_recipe_window.setWindowIcon(icon)
        add_recipe_window.setStyleSheet("background-color: white;")
        self.add_recipe_screen = QtWidgets.QWidget(add_recipe_window)
        self.add_recipe_screen.setObjectName("add_recipe_screen")
        self.add_recipe_label = QtWidgets.QLabel(self.add_recipe_screen)
        self.add_recipe_label.setGeometry(QtCore.QRect(750, 40, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        self.add_recipe_label.setFont(font)
        self.add_recipe_label.setStyleSheet("color: rgb(49, 87, 44);")
        self.add_recipe_label.setObjectName("add_recipe_label")
        self.list_name = QtWidgets.QPlainTextEdit(self.add_recipe_screen)
        self.list_name.setGeometry(QtCore.QRect(710, 110, 620, 90))
        self.list_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_name.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);\n"
"placeholder {\n"
"  color: rgb(49, 87, 44, 75);\n"
"};\n"
" font-size: 24px;")
        self.list_name.setObjectName("list_name")
        self.add_button_step = QtWidgets.QPushButton(self.add_recipe_screen)
        self.add_button_step.setGeometry(QtCore.QRect(1030, 220, 300, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.add_button_step.setFont(font)
        self.add_button_step.setStyleSheet("background-color: white;\n"
"color:  rgb(49, 87, 44);\n"
"border-radius: 12px;\n"
"border: solid;\n"
"border-color:  rgb(49, 87, 44);\n"
"border-width: 2px;")
        self.add_button_step.setObjectName("add_button_step")
        self.add_photo = QtWidgets.QLabel(self.add_recipe_screen)
        self.add_photo.setGeometry(QtCore.QRect(70, 20, 620, 221))
        self.add_photo.setStyleSheet("border-style: solid;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);")
        self.add_photo.setText("")
        self.add_photo.setPixmap(QtGui.QPixmap("no_image.png"))
        self.add_photo.setScaledContents(True)
        self.add_photo.setObjectName("add_photo")
        self.steps_label = QtWidgets.QLabel(self.add_recipe_screen)
        self.steps_label.setGeometry(QtCore.QRect(70, 260, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.steps_label.setFont(font)
        self.steps_label.setStyleSheet("color: rgb(49, 87, 44);")
        self.steps_label.setObjectName("steps_label")
        self.steps_list = QtWidgets.QListWidget(self.add_recipe_screen)
        self.steps_list.setGeometry(QtCore.QRect(69, 330, 1261, 192))
        self.steps_list.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);")
        self.steps_list.setObjectName("steps_list")
        self.ingredients_label = QtWidgets.QLabel(self.add_recipe_screen)
        self.ingredients_label.setGeometry(QtCore.QRect(70, 580, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.ingredients_label.setFont(font)
        self.ingredients_label.setStyleSheet("color: rgb(49, 87, 44);")
        self.ingredients_label.setObjectName("ingredients_label")
        self.timers_label = QtWidgets.QLabel(self.add_recipe_screen)
        self.timers_label.setGeometry(QtCore.QRect(710, 570, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.timers_label.setFont(font)
        self.timers_label.setStyleSheet("color: rgb(49, 87, 44);")
        self.timers_label.setObjectName("timers_label")
        self.ingredients_list = QtWidgets.QListWidget(self.add_recipe_screen)
        self.ingredients_list.setGeometry(QtCore.QRect(70, 660, 620, 192))
        self.ingredients_list.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);")
        self.ingredients_list.setObjectName("ingredients_list")
        self.timers_list = QtWidgets.QListWidget(self.add_recipe_screen)
        self.timers_list.setGeometry(QtCore.QRect(710, 660, 620, 192))
        self.timers_list.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 12px;\n"
"border-color: rgb(49, 87, 44);")
        self.timers_list.setObjectName("timers_list")
        self.add_button_ingredient = QtWidgets.QPushButton(self.add_recipe_screen)
        self.add_button_ingredient.setGeometry(QtCore.QRect(390, 550, 300, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.add_button_ingredient.setFont(font)
        self.add_button_ingredient.setStyleSheet("background-color: white;\n"
"color:  rgb(49, 87, 44);\n"
"border-radius: 12px;\n"
"border: solid;\n"
"border-color:  rgb(49, 87, 44);\n"
"border-width: 2px;")
        self.add_button_ingredient.setObjectName("add_button_ingredient")
        self.add_button_timer = QtWidgets.QPushButton(self.add_recipe_screen)
        self.add_button_timer.setGeometry(QtCore.QRect(1030, 550, 300, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.add_button_timer.setFont(font)
        self.add_button_timer.setStyleSheet("background-color: white;\n"
"color:  rgb(49, 87, 44);\n"
"border-radius: 12px;\n"
"border: solid;\n"
"border-color:  rgb(49, 87, 44);\n"
"border-width: 2px;")
        self.add_button_timer.setObjectName("add_button_timer")
        self.save_button = QtWidgets.QPushButton(self.add_recipe_screen)
        self.save_button.setGeometry(QtCore.QRect(440, 870, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.save_button.setObjectName("save_button")
        self.delete_button = QtWidgets.QPushButton(self.add_recipe_screen)
        self.delete_button.setGeometry(QtCore.QRect(710, 870, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("background-color: rgb(49, 87, 44);\n"
"color: white;\n"
"border-radius: 12px;")
        self.delete_button.setObjectName("delete_button")
        add_recipe_window.setCentralWidget(self.add_recipe_screen)
        self.statusbar = QtWidgets.QStatusBar(add_recipe_window)
        self.statusbar.setObjectName("statusbar")
        add_recipe_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_recipe_window)
        QtCore.QMetaObject.connectSlotsByName(add_recipe_window)

    def retranslateUi(self, add_recipe_window):
        _translate = QtCore.QCoreApplication.translate
        add_recipe_window.setWindowTitle(_translate("add_recipe_window", "PoLIZANE - Add recipe"))
        self.add_recipe_label.setStatusTip(_translate("add_recipe_window", "Add recipe"))
        self.add_recipe_label.setText(_translate("add_recipe_window", "Add recipe"))
        self.list_name.setStatusTip(_translate("add_recipe_window", "Type recipe name here"))
        self.list_name.setPlaceholderText(_translate("add_recipe_window", "Recipe name"))
        self.add_button_step.setStatusTip(_translate("add_recipe_window", "Click plus to add new step to the recipe"))
        self.add_button_step.setText(_translate("add_recipe_window", "+"))
        self.add_photo.setStatusTip(_translate("add_recipe_window", "Add photo here"))
        self.steps_label.setStatusTip(_translate("add_recipe_window", "Steps"))
        self.steps_label.setText(_translate("add_recipe_window", "Steps:"))
        self.steps_list.setStatusTip(_translate("add_recipe_window", "Added steps list"))
        self.ingredients_label.setStatusTip(_translate("add_recipe_window", "Ingredients"))
        self.ingredients_label.setText(_translate("add_recipe_window", "Ingredients:"))
        self.timers_label.setStatusTip(_translate("add_recipe_window", "Timers"))
        self.timers_label.setText(_translate("add_recipe_window", "Timers:"))
        self.ingredients_list.setStatusTip(_translate("add_recipe_window", "Added ingredienst list"))
        self.timers_list.setStatusTip(_translate("add_recipe_window", "Added timers list"))
        self.add_button_ingredient.setStatusTip(_translate("add_recipe_window", "Click plus to add new ingredient to the recipe"))
        self.add_button_ingredient.setText(_translate("add_recipe_window", "+"))
        self.add_button_timer.setStatusTip(_translate("add_recipe_window", "Click plus to add new timer to the recipe"))
        self.add_button_timer.setText(_translate("add_recipe_window", "+"))
        self.save_button.setStatusTip(_translate("add_recipe_window", "Click save the recipe"))
        self.save_button.setText(_translate("add_recipe_window", "Save"))
        self.delete_button.setStatusTip(_translate("add_recipe_window", "Click delete if you don\'t want to create this recipe"))
        self.delete_button.setText(_translate("add_recipe_window", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_recipe_window = QtWidgets.QMainWindow()
    ui = Ui_add_recipe_window()
    ui.setupUi(add_recipe_window)
    add_recipe_window.show()
    sys.exit(app.exec_())
