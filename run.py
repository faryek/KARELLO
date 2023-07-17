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
        self.ui.memberEnterButton.clicked.connect(self.member_swap)
        self.ui.okButton.clicked.connect(self.check_member)
        
    def check_data(self):
        login = self.ui.loginLine.text()
        password = self.ui.passLine.text()
        try: login = int(login)
        except: sys.exit(2)
        
        query = QSqlQuery()
        try: query.exec(f'SELECT role_id, name FROM Users WHERE login = {login} AND password = {password}')
        except: sys.exit(3)
        if not query.next():
            sys.exit(3)
        role = query.record().indexOf('role_id')
        role = query.value(role)
        name = query.record().indexOf('name')
        name = query.value(name)
        query.finish()
        
        self.mpage_swap(role, name)

    def check_member(self):
        code = self.ui.memberCodeLine.text()
        

    def member_swap(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)

    def mpage_swap(self, role, name):
        if role in range(2, 6):
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(2)
        elif role == 6:
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(0)
            
    def welcome(self, role, name):
        if role in range(2, 6):
            self.ui.welcomeExpertLabel.setText(f'Здравствуйте, {name}')
        elif role == 6:
            self.ui.welcomeLabel.setText(f'Здравствуйте, {name}')

            

            
        

        




if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())


    
