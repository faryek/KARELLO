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
    QFileDialog,
    QHeaderView
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
        self.ui.stackedWidget_1.setCurrentIndex(0)

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

        tables_ = [self.ui.tableWidget, self.ui.expertTable,self.ui.expertTable_2,self.ui.expertTable,
                   self.ui.memberTable,self.ui.memberTable_2,self.ui.protocolTable,self.ui.protocolTable_2,self.ui.protocolTable,
                   self.ui.mainExpertTable,self.ui.competitionTable,self.ui.championshipTable,self.ui.MembersPage_MembersList,self.ui.MembersPage_ProtocolsPage]

        d = 0
        for i in range(len(tables_)):
            tables_[d].horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode(1))
            tables_[d].resizeRowsToContents()
            d+=1


        self.ui.enterButton.clicked.connect(self.check_data)
        self.ui.memberEnterButton.clicked.connect(self.member_swap)
        self.ui.okButton.clicked.connect(self.check_member)

        combo1_array = []
        combo2_array = []

        self.BD()
        query_combo1 = QSqlQuery()
        query_combo1.exec(f'SELECT title FROM Skills')
        query_combo2 = QSqlQuery()
        title = query_combo1.record().indexOf('title')
        while query_combo1.next():
            combo1_array.append(query_combo1.value(title))
        self.ui.competitionCombo.addItem('Любая')
        self.ui.competitionCombo.addItems(combo1_array)
        query_combo2.exec(f'SELECT role FROM Roles')
        role = query_combo2.record().indexOf('role')
        while query_combo2.next():
            combo2_array.append(query_combo2.value(role))
        combo2_array.pop(5)
        self.ui.roleCombo.addItem('Любая')
        self.ui.roleCombo.addItems(combo2_array)
        self.users_table()
        self.ui.roleCombo.currentTextChanged.connect(self.sort_users)
        self.ui.competitionCombo.currentTextChanged.connect(self.sort_users)
        self.ui.showUnknownCheck.toggled.connect(self.sort_users)
        



    def users_table(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Users JOIN Competition_skills ON Users.comp_skill_id = Competition_skills.id JOIN Skills ON Skills.id = Competition_skills.skill_id JOIN Roles ON Roles.id = Users.role_id JOIN Regions on Regions.id = Users.region_id JOIN Statuses ON Statuses.id = Users.status_id WHERE Roles.role != "Организатор"')
        role = query.record().indexOf('Roles.role')
        name = query.record().indexOf('Users.name')
        phone = query.record().indexOf('Users.phone')
        gender = query.record().indexOf('Users.gender')
        email = query.record().indexOf('Users.email')
        region = query.record().indexOf('Regions.title')
        comp = query.record().indexOf('Skills.title')
        status = query.record().indexOf('Statuses.title')
        Tablerow = 0
        row = 1

        while query.next():
            self.ui.memberTable.setRowCount(row)
            self.ui.memberTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(role))))
            self.ui.memberTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(name))))
            self.ui.memberTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query.value(phone))))
            self.ui.memberTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(gender))))
            self.ui.memberTable.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(email))))
            self.ui.memberTable.setItem(Tablerow, 5, QtWidgets.QTableWidgetItem(str(query.value(region))))
            self.ui.memberTable.setItem(Tablerow, 6, QtWidgets.QTableWidgetItem(str(query.value(comp))))
            self.ui.memberTable.setItem(Tablerow, 7, QtWidgets.QTableWidgetItem(str(query.value(status))))
            Tablerow+=1
            row+=1
            

    def sort_users(self):
        query = QSqlQuery()
        sql_query = f'SELECT * FROM Users JOIN Competition_skills ON Users.comp_skill_id = Competition_skills.id JOIN Skills ON Skills.id = Competition_skills.skill_id JOIN Roles ON Roles.id = Users.role_id JOIN Regions on Regions.id = Users.region_id JOIN Statuses ON Statuses.id = Users.status_id WHERE Roles.role != "Организатор"'
        if self.ui.roleCombo.currentIndex() != 0:
            sql_query = sql_query + f' AND Roles.role = "{self.ui.roleCombo.currentText()}"'
        if self.ui.competitionCombo.currentIndex() != 0:
            sql_query = sql_query + f' AND Skills.title = "{self.ui.competitionCombo.currentText()}"'
        if self.ui.showUnknownCheck.isChecked() == True:
            sql_query = sql_query + f' AND Statuses.id != 1'
        query.exec(sql_query)
        if not query.next():
            while self.ui.memberTable.rowCount() > 0:
                self.ui.memberTable.removeRow(0)
            return
        else:
            query.finish()
            query.exec(sql_query)
        role = query.record().indexOf('Roles.role')
        name = query.record().indexOf('Users.name')
        phone = query.record().indexOf('Users.phone')
        gender = query.record().indexOf('Users.gender')
        email = query.record().indexOf('Users.email')
        region = query.record().indexOf('Regions.title')
        comp = query.record().indexOf('Skills.title')
        status = query.record().indexOf('Statuses.title')
        Tablerow = 0
        row = 1

        while query.next():
            self.ui.memberTable.setRowCount(row)
            self.ui.memberTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(role))))
            self.ui.memberTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(name))))
            self.ui.memberTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query.value(phone))))
            self.ui.memberTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(gender))))
            self.ui.memberTable.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(email))))
            self.ui.memberTable.setItem(Tablerow, 5, QtWidgets.QTableWidgetItem(str(query.value(region))))
            self.ui.memberTable.setItem(Tablerow, 6, QtWidgets.QTableWidgetItem(str(query.value(comp))))
            self.ui.memberTable.setItem(Tablerow, 7, QtWidgets.QTableWidgetItem(str(query.value(status))))
            Tablerow+=1
            row+=1


        
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
        self.BD_Championship()
        self.BD_Expert()
        self.BD_Protokols()
        self.BD_Members_for_member()
        self.BD_Protokols_for_member()
        self.BD_Members_for_expert()
        self.BD_Experts_for_expert()
        self.BD_Protokols_for_expert()

    def BD_Championship(self):
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
        query.finish()

    def BD_Expert(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Users WHERE role_id = 2')
        Name = query.record().indexOf('name')
        Mail = query.record().indexOf('phone')
        Phone = query.record().indexOf('email')
        Com_id = query.record().indexOf('comp_skill_id')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.expertTable.setRowCount(row)
            
            self.ui.expertTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(Name))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT * FROM Competition_skills WHERE id = {query.value(Com_id)}')
            competit_id = query1.record().indexOf('competition_id')
            skill_id = query1.record().indexOf('skill_id')
            query1.next()

            query2 = QSqlQuery()
            query2.exec(f'SELECT * FROM Competitions WHERE id = {query1.value(competit_id)}')
            title = query2.record().indexOf('title')
            query2.next()
            self.ui.expertTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query2.value(title))))

            query3 = QSqlQuery()
            query3.exec(f'SELECT * FROM Skills WHERE id = {query1.value(skill_id)}')
            title = query3.record().indexOf('title')
            query3.next()
            self.ui.expertTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query3.value(title))))

            self.ui.expertTable.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(Phone))))
            self.ui.expertTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(Mail))))

            Tablerow+=1
            row+=1
        query.finish()

    def BD_Protokols(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Protocols')
        title = query.record().indexOf('title')
        desc = query.record().indexOf('desc')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.protocolTable.setRowCount(row)
            
            self.ui.protocolTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.protocolTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(desc))))
            
            Tablerow+=1
            row+=1
        query.finish()

    def BD_Members_for_member(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Users WHERE role_id = 1')
        Name = query.record().indexOf('name')
        Com_id = query.record().indexOf('comp_skill_id')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.MembersPage_MembersList.setRowCount(row)
            
            self.ui.MembersPage_MembersList.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(Name))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT * FROM Competition_skills WHERE id = {query.value(Com_id)}')
            competit_id = query1.record().indexOf('competition_id')
            skill_id = query1.record().indexOf('skill_id')
            query1.next()

            query2 = QSqlQuery()
            query2.exec(f'SELECT * FROM Competitions WHERE id = {query1.value(competit_id)}')
            title = query2.record().indexOf('title')
            query2.next()
            self.ui.MembersPage_MembersList.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query2.value(title))))

            query3 = QSqlQuery()
            query3.exec(f'SELECT * FROM Skills WHERE id = {query1.value(skill_id)}')
            title = query3.record().indexOf('title')
            query3.next()
            self.ui.MembersPage_MembersList.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query3.value(title))))

            Tablerow+=1
            row+=1
        query.finish()

    def BD_Protokols_for_member(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Protocols')
        title = query.record().indexOf('title')
        desc = query.record().indexOf('desc')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.MembersPage_ProtocolsPage.setRowCount(row)
            
            self.ui.MembersPage_ProtocolsPage.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.MembersPage_ProtocolsPage.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(desc))))
            
            Tablerow+=1
            row+=1
        query.finish()

    def BD_Members_for_expert(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Users WHERE role_id = 1')
        Name = query.record().indexOf('name')
        Com_id = query.record().indexOf('comp_skill_id')
        Mail = query.record().indexOf('phone')
        Phone = query.record().indexOf('email')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.memberTable_2.setRowCount(row)
            
            self.ui.memberTable_2.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(Name))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT * FROM Competition_skills WHERE id = {query.value(Com_id)}')
            competit_id = query1.record().indexOf('competition_id')
            skill_id = query1.record().indexOf('skill_id')
            query1.next()

            query2 = QSqlQuery()
            query2.exec(f'SELECT * FROM Competitions WHERE id = {query1.value(competit_id)}')
            title = query2.record().indexOf('title')
            query2.next()
            self.ui.memberTable_2.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query2.value(title))))

            query3 = QSqlQuery()
            query3.exec(f'SELECT * FROM Skills WHERE id = {query1.value(skill_id)}')
            title = query3.record().indexOf('title')
            query3.next()
            self.ui.memberTable_2.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query3.value(title))))

            self.ui.memberTable_2.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(Mail))))
            self.ui.memberTable_2.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(Phone))))

            Tablerow+=1
            row+=1
        query.finish()

    def BD_Experts_for_expert(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Users WHERE role_id = 2 OR role_id = 4 OR role_id = 5')
        Name = query.record().indexOf('name')
        Com_id = query.record().indexOf('comp_skill_id')
        Mail = query.record().indexOf('phone')
        Phone = query.record().indexOf('email')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.expertTable_2.setRowCount(row)
            
            self.ui.expertTable_2.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(Name))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT * FROM Competition_skills WHERE id = {query.value(Com_id)}')
            competit_id = query1.record().indexOf('competition_id')
            skill_id = query1.record().indexOf('skill_id')
            query1.next()

            query2 = QSqlQuery()
            query2.exec(f'SELECT * FROM Competitions WHERE id = {query1.value(competit_id)}')
            title = query2.record().indexOf('title')
            query2.next()
            self.ui.expertTable_2.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query2.value(title))))

            query3 = QSqlQuery()
            query3.exec(f'SELECT * FROM Skills WHERE id = {query1.value(skill_id)}')
            title = query3.record().indexOf('title')
            query3.next()
            self.ui.expertTable_2.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query3.value(title))))

            self.ui.expertTable_2.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(Mail))))
            self.ui.expertTable_2.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query.value(Phone))))

            Tablerow+=1
            row+=1
        query.finish()

    def BD_Protokols_for_expert(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Protocols')
        title = query.record().indexOf('title')
        desc = query.record().indexOf('desc')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.protocolTable_2.setRowCount(row)
            
            self.ui.protocolTable_2.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.protocolTable_2.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(desc))))
            
            Tablerow+=1
            row+=1
        query.finish()

    

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


    def check_data(self):
        login = self.ui.loginLine.text()
        password = self.ui.passLine.text()
        
        query = QSqlQuery()
        try: query.exec(f'SELECT role_id, name, comp_skill_id FROM Users WHERE login = {login} AND password = {password}')
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
        cs_id = query.record().indexOf('comp_skill_id')
        cs_id = query.value(cs_id)

        try: query.exec(f'SELECT competition_id, skill_id FROM Competition_skills WHERE id = {cs_id}')
        except:
            pass
        if not query.next():
            pass
        
        c_id = query.record().indexOf('competition_id')
        c_id = query.value(c_id)

        s_id = query.record().indexOf('skill_id')
        s_id = query.value(s_id)
        
        query.finish()

        query2 = QSqlQuery()
        query2.exec(f'SELECT title FROM Competitions WHERE id = {c_id}')
        c_title = query2.record().indexOf('title')
        query2.next()
        c_title = query2.value(c_title)
        query2.finish()

        query3 = QSqlQuery()
        query3.exec(f'SELECT title FROM Skills WHERE id = {s_id}')
        s_title = query3.record().indexOf('title')
        query3.next()
        s_title = query3.value(s_title)
        query3.finish()

        
            
        self.set_titles(c_title, s_title)
        self.mpage_swap(role, name)

    def check_member(self):
        code = self.ui.memberCodeLine.text()
        query = QSqlQuery()
        try:
            query.exec(f'SELECT comp_skill_id FROM Users WHERE login = "{code}" AND role_id = 1')
        except:
            self.showMemberError()
            return

        if not query.next():
            self.showMemberError()
            return
        
        cs_id = query.record().indexOf('comp_skill_id')
        cs_id = query.value(cs_id)

        try: query.exec(f'SELECT competition_id, skill_id FROM Competition_skills WHERE id = {cs_id}')
        except:
            self.showMemberError()
            return
        if not query.next():
            self.showMemberError()
            return
        
        c_id = query.record().indexOf('competition_id')
        c_id = query.value(c_id)

        s_id = query.record().indexOf('skill_id')
        s_id = query.value(s_id)

        query.finish()

        query2 = QSqlQuery()
        query2.exec(f'SELECT title FROM Competitions WHERE id = {c_id}')
        c_title = query2.record().indexOf('title')
        query2.next()
        c_title = query2.value(c_title)
        query2.finish()

        query3 = QSqlQuery()
        query3.exec(f'SELECT title FROM Skills WHERE id = {s_id}')
        s_title = query3.record().indexOf('title')
        query3.next()
        s_title = query3.value(s_title)
        query3.finish()

        
            
        self.set_titles(c_title, s_title)
        
        self.ui.stackedWidget_2.setCurrentIndex(1)
        

    def member_swap(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)

    def mpage_swap(self, role, name):
        if role in range(2, 6):
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(2)
        elif role == 6:
            self.welcome(role, name)
            self.ui.stackedWidget_4.setCurrentIndex(0)
            self.ui.stackedWidget_1.setCurrentIndex(0)
            self.ui.stackedWidget3.setCurrentIndex(2)
        elif role == 1:
            pass
            
    def welcome(self, role, name):
        if role in range(2, 6):
            self.ui.welcomeExpertLabel.setText(f'Здравствуйте, {name}')
        elif role == 6:
            self.ui.welcomeLabel.setText(f'Здравствуйте, {name}')

    def set_titles(self, comp, skill):
        self.ui.champTitleLabel.setText(comp)
        self.ui.compTitleLabel.setText(skill)
        self.ui.champTitleLabel_2.setText(comp)
        self.ui.compTitleLabel_2.setText(skill)
        self.ui.champTitleLabel_3.setText(comp)
        self.ui.compTitleLabel_3.setText(skill)
        self.ui.champTitleLabel_5.setText(comp)
        self.ui.compTitleLabel_4.setText(skill)


    def showError(self):
       QMessageBox.about(self, "Ошибка", "Неверный логин или пароль!")

    def showMemberError(self):
        QMessageBox.about(self, "Ошибка", "Неверный код!")


if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())


    
