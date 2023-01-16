import sys
from PyQt5 import QtWidgets
from database.database_init import Session, engine
from ui.recpie_window import Ui_recpie_window

if __name__ == "__main__":
    # Database setup
    local_session = Session(bind=engine)
    # Opening 'recipe screen' and starting application
    app = QtWidgets.QApplication(sys.argv)
    recpie_window = QtWidgets.QMainWindow()
    ui = Ui_recpie_window()
    ui.setupUi(recpie_window)
    recpie_window.show()
    sys.exit(app.exec_())
