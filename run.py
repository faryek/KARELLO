from Organization import Ui_MainWindow
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QStackedWidget,
    QTableWidget,
    QWidget
)
from PyQt6.QtSql import QSqlDatabase

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        con = QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('WS.db')
        try: con.open()
        except: sys.exit(1)


if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())
    
