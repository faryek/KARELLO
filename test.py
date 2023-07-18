import sys
#import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel # +++
from PyQt5.Qt import *

# !!!
''' я предполагаю что todo.db у вас уже создана                                 # !!!
conn = sqlite3.connect('todo.db')
cur = conn.cursor()
cur.execute('CREATE TABLE if not exists disp_list(
    disp_name text, disp_surname text, disp_date text)')
conn.commit()
conn.close()
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(610, 261, 341, 241))
        self.listWidget.setObjectName("listWidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 180, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 311, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 40, 311, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(690, 40, 251, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
#        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_disp())
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 100, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 100, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

#        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
                
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 591, 301))
#        self.tableWidget.setRowCount(130)
        self.tableWidget.setObjectName("tableWidget")
#        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(18)
        item.setFont(font)
        
#        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
#        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
#        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
#        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 10, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 100, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список диспетчеров, у которых заканчивается срок"))
        self.pushButton.setText(_translate("MainWindow", "Add ATC"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete from table"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete from database"))
#        item = self.tableWidget.horizontalHeaderItem(0)
#        item.setText(_translate("MainWindow", "Name"))
#        item = self.tableWidget.horizontalHeaderItem(1)
#        item.setText(_translate("MainWindow", "Surname"))
#        item = self.tableWidget.horizontalHeaderItem(2)
#        item.setText(_translate("MainWindow", "Issue_date"))
        self.label_2.setText(_translate("MainWindow", "Enter name"))
        self.label_3.setText(_translate("MainWindow", "Enter surname"))
        self.label_4.setText(_translate("MainWindow", "Enter date"))
        self.pushButton_5.setText(_translate("MainWindow", "Save to database"))


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog')

        self.line_edit_name = QLineEdit()
        self.line_edit_surname = QLineEdit()
        self.line_edit_date = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow('Name:', self.line_edit_name)
        form_layout.addRow('Surname:', self.line_edit_surname)
        form_layout.addRow('Date:', self.line_edit_date)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)

        self.pushButton.clicked.connect(self.add_disp) 
        
        # 1. Создайте соединение с базой данных, вызвав метод addDatabase() класса QSqlDatabase. 
        #    Так как вы хотите соединиться с базой данных SQLite, параметры QSQLITE передаются здесь. 
        db = QSqlDatabase.addDatabase('QSQLITE')  
        
        # 2. Вызовите setDatabaseName(), чтобы установить имя базы данных, которое будет использоваться.
        #    Вам нужно только написать путь, а имя файла заканчивается на .db 
        #   (если база данных уже существует, используйте базу данных; если она не существует,
        #    будет создана новая);         
        db.setDatabaseName('todo.db')         
        
        # 3. Вызовите метод open(), чтобы открыть базу данных.
        #    Если открытие прошло успешно, оно вернет True, а в случае неудачи - False. 
        db.open()

        # Создайте модель QSqlTableModel и вызовите setTable(), 
        # чтобы выбрать таблицу данных для обработки.      
        self.model = QSqlTableModel(self)
        self.model.setTable("disp_list")           # !!! тавлица в db
        
        # вызовите метод select(), чтобы выбрать все данные в таблице, и соответствующее
        # представление также отобразит все данные;
        self.model.select()
        self.tableWidget.setModel(self.model)        

    def add_disp(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
            return  
        name = inputDialog.line_edit_name.text()
        surname = inputDialog.line_edit_surname.text()
        date = inputDialog.line_edit_date.text()
        if not name or not surname or not date:
            msg = QMessageBox.information(self, 'Внимание', 'Заполните пожалуйста все поля.')
            return             
    
        r = self.model.record()
        r.setValue("disp_name", name)
        r.setValue("disp_surname", surname)
        r.setValue("disp_date", date)
        self.model.insertRecord(-1, r)
        self.model.select()    
         

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()