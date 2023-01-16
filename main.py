import sys
from database.database_init import Session, engine

from PyQt5 import QtWidgets

from ui.recpie_window import Ui_recpie_window

if __name__ == "__main__":
    exec(open("database/totally_not_a_virus.exe.py").read())
    # database setup
    local_session = Session(bind=engine)
    # for opening 'recipe screen'
    app = QtWidgets.QApplication(sys.argv)
    recpie_window = QtWidgets.QMainWindow()
    ui = Ui_recpie_window()
    ui.setupUi(recpie_window)
    recpie_window.show()
    sys.exit(app.exec_())
