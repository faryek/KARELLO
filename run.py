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
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        con = QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('WS.db')
        try: con.open()
        except: sys.exit(1)

        

        self.ui.enterButton.clicked.connect(self.check_data)
    def check_data(self):
        login = self.ui.loginLine.text()
        password = self.ui.passLine.text()
        try: login = int(login)
        except: sys.exit('Error!')
        query = QSqlQuery()
        query.exec(f'SELECT COUNT(role_id) FROM Users WHERE login = {login} AND password = {password}')
        print(f'SELECT role_id FROM Users WHERE login = {login} AND password = {password}')
        print(type(login))
        print(type(password))
        print(query.first())
        print(query.value(0))

        




if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())


    
