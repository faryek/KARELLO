from Organization import Ui_MainWindow
import sys
from PyQt6 import (QtCore, QtGui, QtWidgets)
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QStackedWidget,
    QTableWidget,
    QWidget,
    QFileDialog
)

from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        con = QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('WS.db')
        try: con.open()
        except: sys.exit(1)

        self.ui.stackedWidget_4.setCurrentIndex(3)


        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.addChampButton.clicked.connect(lambda: self.ui.stackedWidget_1.setCurrentIndex(1)) 
        self.ui.championshipEditButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.memberButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.mainExpertButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.protocolCButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.backToMainButton.clicked.connect(self.reset_on_click_back)
        self.ui.logoutButton.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentIndex(3))
        self.ui.logoutButton_2.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentIndex(3))
        self.ui.memberButton_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.expertButton_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.protocolButton_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentIndex(2))
        self.ui.championshipButton.clicked.connect(lambda: self.ui.stackedWidget3.setCurrentIndex(2))
        self.ui.expertButton.clicked.connect(lambda: self.ui.stackedWidget3.setCurrentIndex(1))
        self.ui.protocolButton.clicked.connect(lambda: self.ui.stackedWidget3.setCurrentIndex(0))
        self.ui.exitButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.okButton_2.clicked.connect(lambda: self.ui.stackedWidget_4.setCurrentIndex(3))
        self.ui.memberButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.protocolButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(3))
        self.ui.backToMainButton_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.backToMainButton_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.exitButton_2.clicked.connect(self.exit_on_main_page)
        self.ui.exitButton_3.clicked.connect(self.exit_on_main_page)
        self.ui.pushButton.clicked.connect(self.Open_main_file_btn)

        self.ui.enterButton.clicked.connect(self.check_data)
        self.ui.memberEnterButton.clicked.connect(self.member_swap)
        self.ui.okButton.clicked.connect(self.check_member)
        
        
        self.BD()


    def Open_main_file_btn(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', '','PNG file (*.png)')
        pixmap = QPixmap(res[0])
        smaller_pixmap = pixmap.scaled(QtCore.QSize(200, 100))
        self.ui.logoLabel.setPixmap(smaller_pixmap)


    def exit_on_main_page(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.stackedWidget_2.setCurrentIndex(0)


    def reset_on_click_back(self):
        self.ui.stackedWidget_1.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)

        

    def BD(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Competitions')
        title = query.record().indexOf('title')
        date_start = query.record().indexOf('date_start')
        date_end = query.record().indexOf('date_end')
        city_id = query.record().indexOf('city_id')
        desc = query.record().indexOf('desc')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.championshipTable.setRowCount(row)
            self.ui.championshipTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.championshipTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(date_start))))
            self.ui.championshipTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query.value(date_end))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT title FROM Cities WHERE id = {query.value(city_id)}')
            City = query1.record().indexOf('title')
            query1.next()
            self.ui.championshipTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query1.value(City))))

            self.ui.championshipTable.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(desc))))
            Tablerow+=1
            row+=1

    def check_data(self):
        login = self.ui.loginLine.text()
        password = self.ui.passLine.text()
        
        query = QSqlQuery()
        try: query.exec(f'SELECT role_id, name FROM Users WHERE login = {login} AND password = {password}')
        except:
            self.showError()
            return
        if not query.next():
            self.showError()
            return
        role = query.record().indexOf('role_id')
        role = query.value(role)
        name = query.record().indexOf('name')
        name = query.value(name)
        query.finish()
        
        self.mpage_swap(role, name)

    def check_member(self):
        code = self.ui.memberCodeLine.text()
        query = QSqlQuery()
        try:
            query.exec(f'SELECT name FROM Users WHERE login = "{code}" AND role_id = 1')
        except:
            self.showMemberError()
            return
        if not query.next():
            self.showMemberError()
            return
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        query.finish()
        

    def member_swap(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)

    def mpage_swap(self, role, name):
        if role in range(2, 6):
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(2)
        elif role == 6:
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(0)
        elif role == 1:
            pass
            
    def welcome(self, role, name):
        if role in range(2, 6):
            self.ui.welcomeExpertLabel.setText(f'Здравствуйте, {name}')
        elif role == 6:
            self.ui.welcomeLabel.setText(f'Здравствуйте, {name}')


    def showError(self):
       QMessageBox.about(self, "Ошибка", "Неверный логин или пароль!")

    def showMemberError(self):
        QMessageBox.about(self, "Ошибка", "Неверный код!")


if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())


    
