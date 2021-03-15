from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from main1 import *  # импорт нашего сгенерированного файла
import requests
from bs4 import BeautifulSoup


def start():
    url = 'https://www.stoloto.ru/rapido2/archive'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes1 = soup.find_all('div', class_='elem')
    quotes = soup.find_all('span', class_='zone')

    # print('-->',quotes1)
    # print(type(quotes1))

    paragraphs = []

    for x in quotes1:
        paragraphs.append([str(x)])
        #print(paragraphs)
data = [(1,1),(2,2),(3,3)]


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Меняем текст
        self.ui.lineEdit.setText("Добро пожаловать на PythonScripts")
        # указать максимальную длину
        self.ui.lineEdit_2.setMaxLength(10)
        # ввод пароля
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        # только чтение без изменения содержимого.
        self.ui.lineEdit_4.setReadOnly(True)
        # меняем цвет вводимого текста
        self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")
        # изменение цвета фона QLineEdit
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(3)
        # очистка таблицы при клике на кнопку.
        self.ui.pushButton.clicked.connect(self.clear)
        # кнопка парсера
        self.ui.pushButton_2.clicked.connect(self.buttonClicked1)
        # Кол-во рядов меняется в зависимости от значений в data.
        self.ui.tableWidget.setRowCount(len(data))

        # Кол-во столбцов меняется в зависимости от data.
        self.ui.tableWidget.setColumnCount(len(data[0]))

        # заголовки для столбцов.
        self.ui.tableWidget.setHorizontalHeaderLabels(('Марка', 'Год выпуска'))
        # названия рядов.
        #self.ui.tableWidget.setVerticalHeaderLabels(('900$', '5000$', '13000$'))

        row = 0
        for tup in data:
            col = 0

            for item in tup:
               cellinfo = QTableWidgetItem(item)
               # Только для чтения
               cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
               self.ui.tableWidget.setItem(row, col, cellinfo)
               col += 1
            row += 1
        # Сортировка по году выпуска.
        # 0 - Марка
        # 1 - Год выпуска
        self.ui.tableWidget.sortByColumn(1, QtCore.Qt.AscendingOrder)

    def buttonClicked1(self):
        self.textEdit.append(start())

    def clear(self):
        self.ui.tableWidget.clear()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())