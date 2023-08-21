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
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore

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
        self.ui.addCompetitionButton.clicked.connect(self.add_Competitions_Table)
        self.ui.saveCompetitionButton.clicked.connect(self.Save_Champions)
        self.ui.exitButton_2.clicked.connect(self.exit_on_main_page)
        self.ui.exitButton_3.clicked.connect(self.exit_on_main_page)
        self.ui.pushButton.clicked.connect(self.Open_main_file_btn)
        

        self.ui.enterButton.clicked.connect(self.check_data)
        self.ui.memberEnterButton.clicked.connect(self.member_swap)
        self.ui.okButton.clicked.connect(self.check_member)
        self.BD_Championship()
        self.BD_Expert()
        self.BD_Protokols()
        self.addSity()

    def BD_Championship(self):
        while (self.ui.championshipTable.rowCount() > 0):
            self.ui.championshipTable.setRowCount(0)
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Competitions')
        id = query.record().indexOf('id')
        title = query.record().indexOf('title')
        date_start = query.record().indexOf('date_start')
        date_end = query.record().indexOf('date_end')
        city_id = query.record().indexOf('city_id')
        desc = query.record().indexOf('desc')

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.championshipTable.setRowCount(row)
            self.ui.championshipTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(id))))
            self.ui.championshipTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.championshipTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query.value(date_start))))
            self.ui.championshipTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(date_end))))

            query1 = QSqlQuery()
            query1.exec(f'SELECT title FROM Cities WHERE id = {query.value(city_id)}')
            City = query1.record().indexOf('title')
            query1.next()
            self.ui.championshipTable.setItem(Tablerow, 4, QtWidgets.QTableWidgetItem(str(query1.value(City))))

            self.ui.championshipTable.setItem(Tablerow, 5, QtWidgets.QTableWidgetItem(str(query.value(desc))))

            pushButton = QtWidgets.QPushButton()
            pushButton.clicked.connect(self.changeClick)
            # pushButton.setStyleSheet('image: url(:Logo/trash1.png);')
            self.ui.championshipTable.setCellWidget(Tablerow, 6, pushButton)
            pushButton1 = QtWidgets.QPushButton()
            pushButton1.clicked.connect(self.deleteClicked)
            # pushButton1.setStyleSheet('image: url(:Logo/galka.png);')
            self.ui.championshipTable.setCellWidget(Tablerow, 7, pushButton1)

            Tablerow+=1
            row+=1

    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.ui.championshipTable.indexAt(button.pos()).row() # type: ignore
            id = self.ui.championshipTable.item(row,0).text()
            self.ui.championshipTable.removeRow(row)
            query = QSqlQuery()
            query.exec(f'DELETE FROM Competitions WHERE id = {id}')
            id = query.record().indexOf('main_expert')
            query.next()
    
    def addSity(self):
        self.ui.Sity.addItem("Город не выбран")
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Cities')
        title_sity = query.record().indexOf('title')
        while query.next():
            self.ui.Sity.addItem(str(query.value(title_sity)))
        

    def add_Competitions_Table(self):
        maxRow = -1
        for row in range(self.ui.competitionTable.rowCount()):
            for col in range(self.ui.competitionTable.columnCount()):
                item = self.ui.competitionTable.item(row, col)
                if not item or not item.text():
                    continue
                maxRow = row
        row = maxRow + 1
        Tablerow = maxRow + 1
        self.ui.competitionTable.setRowCount(row+1)

        query1 = QSqlQuery()
        query1.exec(f'SELECT * FROM Users WHERE role_id = 2')
        name_expert = query1.record().indexOf('name')
        valueExpert = 1
        combobox = QtWidgets.QComboBox()
        combobox.addItem(" ")
        while query1.next():
            combobox.addItem(str(query1.value(name_expert)))
            valueExpert+=1
        self.ui.competitionTable.setCellWidget(Tablerow, 0, combobox)

        query5 = QSqlQuery()
        query5.exec(f'SELECT * FROM Skills')
        title_Komp = query5.record().indexOf('title')
        valueExpert = 1
        combobox1 = QtWidgets.QComboBox()
        combobox1.addItem(" ")
        while query5.next():
            combobox1.addItem(str(query5.value(title_Komp)))
            valueExpert+=1
        self.ui.competitionTable.setCellWidget(Tablerow, 1, combobox1)

    def changeClick(self):
        self.ui.stackedWidget_1.setCurrentIndex(1)
        button = self.sender()
        if button:
            row = self.ui.championshipTable.indexAt(button.pos()).row() # type: ignore
            Data_start = self.ui.championshipTable.item(row,2).text()
            Data_end = self.ui.championshipTable.item(row,3).text()
            title = self.ui.championshipTable.item(row,1).text()
            Sity = self.ui.championshipTable.item(row,4).text()

            query6 = QSqlQuery()
            query6.exec(f"SELECT * FROM Cities WHERE title = '{Sity}'")            
            id_sity = query6.record().indexOf('id')
            query6.next()
            self.ui.Sity.setCurrentIndex(int(query6.value(id_sity)))

            self.ui.startDateLine.setText(Data_start)
            self.ui.endDateLine.setText(Data_end)
            self.ui.titleLine.setText(title)
            id = self.ui.championshipTable.item(row,0).text()
            query = QSqlQuery()
            query.exec(f'SELECT * FROM Competition_skills WHERE competition_id = {id}')
            member_count = query.record().indexOf('member_count')
            expert_count = query.record().indexOf('expert_count')
            main_expert = query.record().indexOf('main_expert')
            skill_id = query.record().indexOf('skill_id')
            id_skill = query.record().indexOf('id')
            Tablerow = 0
            row = 1
            self.ui.Nomer.setText(id)
            while query.next():
                self.ui.competitionTable.setRowCount(row)
                
                query4 = QSqlQuery()
                query4.exec(f'SELECT * FROM Users WHERE id = {str(query.value(main_expert))}')
                name_expert = query4.record().indexOf('name')
                query4.next()

                query1 = QSqlQuery()
                query1.exec(f'SELECT * FROM Users WHERE role_id = 2')
                name_expert = query1.record().indexOf('name')
                valueExpert = 1
                combobox = QtWidgets.QComboBox()
                combobox.addItem(" ")
                while query1.next():
                    combobox.addItem(str(query1.value(name_expert)))
                    if str(query1.value(name_expert)) ==  str(query4.value(name_expert)):
                        combobox.setCurrentIndex(valueExpert)
                    valueExpert+=1
                self.ui.competitionTable.setCellWidget(Tablerow, 0, combobox)

                query2 = QSqlQuery()
                query2.exec(f'SELECT * FROM Skills WHERE id = {str(query.value(skill_id))}')
                title_Komp = query2.record().indexOf('title')
                query2.next()

                query5 = QSqlQuery()
                query5.exec(f'SELECT * FROM Skills')
                title_Komp = query5.record().indexOf('title')
                valueExpert = 1
                combobox1 = QtWidgets.QComboBox()
                combobox1.addItem(" ")
                while query5.next():
                    combobox1.addItem(str(query5.value(title_Komp)))
                    if str(query5.value(title_Komp)) ==  str(query2.value(title_Komp)):
                        combobox1.setCurrentIndex(valueExpert)
                    valueExpert+=1
                self.ui.competitionTable.setCellWidget(Tablerow, 1, combobox1)

                self.ui.competitionTable.setItem(Tablerow, 2, QtWidgets.QTableWidgetItem(str(query.value(expert_count))))

                self.ui.competitionTable.setItem(Tablerow, 3, QtWidgets.QTableWidgetItem(str(query.value(member_count))))

                Tablerow+=1
                row+=1

    def Save_Champions(self):
        id = self.ui.Nomer.text()
        if (id == ""):
            query4 = QSqlQuery()
            data_start = self.ui.startDateLine.text()
            data_end = self.ui.endDateLine.text()
            titleLine = self.ui.titleLine.text()
            title_sity = self.ui.Sity.currentText()

            query6 = QSqlQuery()
            query6.exec(f'SELECT * FROM Cities')
            id_Sity = query6.record().indexOf('id')
            query6.next()
            id_Sity_int = int(query6.value(id_Sity))

            query4.exec(f"INSERT INTO Competitions (title, date_start, date_end, city_id)" f"VALUES ('{titleLine}', '{data_start}', '{data_end}', '{id_Sity_int}')")
            query4.next()

            query5 = QSqlQuery()
            query5.exec(f'SELECT * FROM Competitions') 
            id_com = query5.record().indexOf('id')
            titile = query5.record().indexOf('title')
            while query5.next():
                if (titleLine == str(query5.value(titile))):
                    id = str(query5.value(id_com))
        query = QSqlQuery()
        query.exec(f'DELETE FROM Competition_skills WHERE competition_id = {id}')
        query.next()

        maxRow = -1
        for row in range(self.ui.competitionTable.rowCount()):
            for col in range(self.ui.competitionTable.columnCount()):
                item = self.ui.competitionTable.item(row, col)
                if not item or not item.text():
                    continue
                maxRow = row
        row = maxRow + 1
        for row1 in range(row):
            Main_expert = ""
            Competiton = ""
            id_expert_str = ""
            id_competition_str = ""
            Main_expert_str = self.ui.competitionTable.cellWidget(row1, 0)
            if isinstance(Main_expert_str, QtWidgets.QComboBox):
                Main_expert = Main_expert_str.currentText()

            Competiton_str = self.ui.competitionTable.cellWidget(row1, 1)
            if isinstance(Competiton_str, QtWidgets.QComboBox):
                Competiton = Competiton_str.currentText()

            CountEx = self.ui.competitionTable.item(row1, 2).text()
            CountUs = self.ui.competitionTable.item(row1, 3).text()

            query2 = QSqlQuery()
            query2.exec(f'SELECT * FROM Users WHERE role_id = 2') 
            id_expert = query2.record().indexOf('id')
            Name_expert = query2.record().indexOf('name')
            while query2.next():
                if (Main_expert == str(query2.value(Name_expert))):
                    id_expert_str = str(query2.value(id_expert))

            query3 = QSqlQuery()
            query3.exec(f'SELECT * FROM Skills')
            id_Competiton = query3.record().indexOf('id')
            title_Competition = query3.record().indexOf('title')
            while query3.next():
                if (Competiton == str(query3.value(title_Competition))):
                    id_competition_str = str(query3.value(id_Competiton))
            
            com_id = id
            query1 = QSqlQuery()
            query1.exec(f"INSERT INTO Competition_skills (competition_id, main_expert, skill_id, expert_count, member_count)" f"VALUES ({com_id}, {id_expert_str}, {id_competition_str}, {CountEx}, {CountUs})")
            query1.next()
            self.reset_on_click_back()

    def Clear_form_competition(self):
        self.ui.startDateLine.setText("")
        self.ui.endDateLine.setText("")
        self.ui.titleLine.setText("")
        self.ui.Nomer.setText("")
        self.ui.Sity.setCurrentIndex(0)
        while (self.ui.competitionTable.rowCount() > 0):
            self.ui.competitionTable.setRowCount(0)
        

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

    def BD_Protokols(self):
        query = QSqlQuery()
        query.exec(f'SELECT * FROM Protocols')
        title = query.record().indexOf('title')
        desc = query.record().indexOf('desc')
        query.next()

        Tablerow = 0
        row = 1
        while query.next():
            self.ui.protocolTable.setRowCount(row)
            
            self.ui.protocolTable.setItem(Tablerow, 0, QtWidgets.QTableWidgetItem(str(query.value(title))))
            self.ui.protocolTable.setItem(Tablerow, 1, QtWidgets.QTableWidgetItem(str(query.value(desc))))
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

        self.BD_Championship()
        self.Clear_form_competition()

        
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


    
