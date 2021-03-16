from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import sys
import main1

import requests
from bs4 import BeautifulSoup




data = [(1,1),(2,2),(3,3)]


class mywindow(QtWidgets.QMainWindow, main1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.start)


        self.response = requests.get('https://www.stoloto.ru/rapido2/archive')
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.quotes1 = self.soup.find_all('div', class_='elem')
    #quotes = soup.find_all('span', class_='zone')

    # print('-->',quotes1)
    # print(type(quotes1))

        self.paragraphs = []

        for x in self.quotes1:
            self.paragraphs.append([str(x)])
            print(self.paragraphs)

    def buttonClicked1(self):
        self.textEdit.append(self.start)

    def clear(self):
        self.ui.tableWidget.clear()

    def start(self):
        self.listWidget.clear()
        self.listWidget.addItem(x[:25] for x in self.paragraphs)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())