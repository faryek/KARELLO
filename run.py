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
        self.ui.enterButton.clicked.connect(self.login_success)
        self.ui.addChampButton.clicked.connect(self.champinship_open_change)
        self.ui.championshipEditButton.clicked.connect(self.champinship_settings)
        self.ui.memberButton.clicked.connect(self.champinship_member_list)
        self.ui.mainExpertButton.clicked.connect(self.champinship_settings)
        self.ui.protocolCButton.clicked.connect(self.champinship_settings)


    def login_success(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)


    def champinship_open_change(self):
        self.ui.stackedWidget_1.setCurrentIndex(1)


    def champinship_settings(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def champinship_member_list(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def champinship_expert_list(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def champinship_protocol_list(self):
        self.ui.stackedWidget.setCurrentIndex(1)



if __name__ == '__main__':
    app = QApplication([])
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(app.exec())