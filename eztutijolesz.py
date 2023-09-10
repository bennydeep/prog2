# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\benko\Desktop\test3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import random
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import myClasses as mc

class Ui_MainWindow(object):
    lsCustomer = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 594)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list = QtWidgets.QListWidget(self.frame_2)
        self.list.setObjectName("list")
        self.gridLayout_2.addWidget(self.list, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.inSelect = QtWidgets.QLineEdit(self.frame_2)
        self.inSelect.setObjectName("inSelect")
        self.horizontalLayout_6.addWidget(self.inSelect)
        self.selectBtn = QtWidgets.QPushButton(self.frame_2)
        self.selectBtn.setObjectName("selectBtn")
        self.horizontalLayout_6.addWidget(self.selectBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inName = QtWidgets.QLineEdit(self.frame)
        self.inName.setPlaceholderText("")
        self.inName.setObjectName("inName")
        self.horizontalLayout.addWidget(self.inName)
        self.newBtn = QtWidgets.QPushButton(self.frame)
        self.newBtn.setObjectName("newBtn")
        self.horizontalLayout.addWidget(self.newBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.inID = QtWidgets.QLineEdit(self.frame)
        self.inID.setText("")
        self.inID.setReadOnly(False)
        self.inID.setObjectName("inID")
        self.horizontalLayout_3.addWidget(self.inID)
        self.loadBtn = QtWidgets.QPushButton(self.frame)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout_3.addWidget(self.loadBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.inDate = QtWidgets.QLineEdit(self.frame)
        self.inDate.setObjectName("inDate")
        self.horizontalLayout_2.addWidget(self.inDate)
        self.editBtn = QtWidgets.QPushButton(self.frame)
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_2.addWidget(self.editBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.inNum = QtWidgets.QLineEdit(self.frame)
        self.inNum.setText("")
        self.inNum.setReadOnly(False)
        self.inNum.setObjectName("inNum")
        self.horizontalLayout_4.addWidget(self.inNum)
        self.delBtn = QtWidgets.QPushButton(self.frame)
        self.delBtn.setObjectName("delBtn")
        self.horizontalLayout_4.addWidget(self.delBtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.inBalance = QtWidgets.QLineEdit(self.frame)
        self.inBalance.setPlaceholderText("")
        self.inBalance.setObjectName("inBalance")
        self.horizontalLayout_5.addWidget(self.inBalance)
        self.genBtn = QtWidgets.QPushButton(self.frame)
        self.genBtn.setObjectName("genBtn")
        self.horizontalLayout_5.addWidget(self.genBtn)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.newBtn.clicked.connect(self.newBtnClicked)  # az új ügyfél gomb életrekeltése
        self.loadBtn.clicked.connect(self.editClicked)
        self.genBtn.clicked.connect(self.genBtnClicked)  # mégse gomb életrekeltése
        self.delBtn.clicked.connect(self.deleteItem)  # törlés gomb életrekeltése
        self.editBtn.clicked.connect(self.newBtnClicked)
        self.selectBtn.clicked.connect(self.selectBtnClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prog2Beadandó"))
        self.label_7.setText(_translate("MainWindow", "Ügyfél Adatbázis"))
        self.label_6.setText(_translate("MainWindow", "Egyenleg alapú lekérdezés"))
        self.selectBtn.setToolTip(_translate("MainWindow", "Lekérdezi az adott összegnél nagyobb egyenlegű ügyfeleket"))
        self.selectBtn.setText(_translate("MainWindow", "Lekérdez"))
        self.label_8.setText(_translate("MainWindow", "Ügyfél Adatai"))
        self.label.setText(_translate("MainWindow", "Ügyfél neve"))
        self.newBtn.setText(_translate("MainWindow", "Új ügyfél"))
        self.label_2.setText(_translate("MainWindow", "Ügyfél azonosító"))
        self.inID.setPlaceholderText(_translate("MainWindow", "Ügyfél azonosító (Rendszer által generált)"))
        self.loadBtn.setText(_translate("MainWindow", "Visszatölt"))
        self.label_3.setText(_translate("MainWindow", "Születési ideje"))
        self.inDate.setPlaceholderText(_translate("MainWindow", "Írd be az ügyfél születési dátumát 1900.01.01 formátumban"))
        self.editBtn.setText(_translate("MainWindow", "Módosít"))
        self.label_4.setText(_translate("MainWindow", "Bankszámlaszám"))
        self.inNum.setPlaceholderText(_translate("MainWindow", "Írd be az ügyfél bankszámlaszámát 00000000-00000000 formátumban"))
        self.delBtn.setText(_translate("MainWindow", "Ügyfél törlése"))
        self.label_5.setText(_translate("MainWindow", "Egyenleg"))
        self.genBtn.setText(_translate("MainWindow", "ID generálása"))
        self.inSelect.setText(_translate("MainWindow", "0"))
        self.reloadDatas()

    def newBtnClicked(self):    #új ügyfél gomb lelke
        try:
            name = self.inName.text()
            id = self.inID.text()
            date = self.inDate.text()
            num = self.inNum.text()
            balance = self.inBalance.text()


            if len(name) == 0:
                raise mc.MissingDataException('Név')
            if len(id) == 0:
                raise mc.MissingDataException('Ügyfél azonosító')      #teszteljük hogy a felhasználó kitöltötte e a mezőket
            if len(date) == 0:
                raise mc.MissingDataException('Születési Dátum')
            if len(num) == 0:
                raise mc.MissingDataException('Bankkártyaszám')
            if len(balance) == 0:
                raise mc.MissingDataException('Egyenleg')

            if len(id) != 8 or not re.match(r'^[0-9]{8}',id):                      #stimmel e az ügyfelid
                    raise mc.ugyfelIDException

            if len(num) != 17 or not re.match(r'^[0-9]{8}[-]{1}[0-9]{8}',num):                      #stimmel e a 2*8 karakteres bankszámlaszám
                    raise mc.numException
            if len(date) != 10 or not re.match(r'^[0-9]{4}[.]{1}[0-9]{2}[.]{1}[0-9]{2}',date):                      #stimmel e a születesi datum formatuma
                    raise mc.DateofBirthException

            if int(balance)<=0:
                raise mc.tartozikazugyfelException

        except mc.MissingDataException as mse:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)          #msg box felugratása, ha nem lenne valamelyik mező kitöltve, még a legelején megírt kivételkezelés felhasználásával
            msg.setText(mse.__str__())
            msg.exec()

        except mc.numException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)                                  #ha nem stimmel a bankkártya formátum kivételkezelése szintén felugró msg box
            msg.setText("A Bankszámlaszám nem megfelelő formátumban lett megadva")
            msg.exec()

        except mc.DateofBirthException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)                                  #ha nem stimmel a bankkártya formátum kivételkezelése szintén felugró msg box
            msg.setText("A Születési idő nem megfelelő formátumban lett megadva")
            msg.exec()

        except mc.ugyfelIDException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)                                  #ha nem stimmel a bankkártya formátum kivételkezelése szintén felugró msg box
            msg.setText("Nem megfelelő az ügyfél ID! Használd az ID generálása gombot")
            msg.exec()

        except mc.tartozikazugyfelException:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Negatív egyenlegű ügyféllel kapcsolatban kérjük keresse fel a Behajtási Osztályt")
            msg.exec()

        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Kérem megfelelően töltse ki a sorokat")
            msg.exec()

        else:
            if not self.inID.isReadOnly():
                c = mc.Customer(name, id, date, num, balance)
                if c not in self.lsCustomer:
                    self.lsCustomer.append(c)
                    self.lsCustomer.sort()
                    self.list.clear()
                    self.saveToFile()
                    for i in self.lsCustomer:
                        self.list.addItem(i.__str__())
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Figyelem!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Már van ilyen ügyfelünk!")
                    msg.exec()

            else:
                for i in self.lsCustomer:
                    if i.getID() == self.inID.text():
                        self.lsCustomer.remove(i)
                        i.setName(name)
                        i.setDate(date)
                        i.setNum(num)
                        i.setBalance(balance)
                        self.lsCustomer.append(i)
                        self.lsCustomer.sort()
                        self.list.clear()
                        self.saveToFile()
                        self.inID.setReadOnly(False)
                        for j in self.lsCustomer:
                            self.list.addItem(j.__str__())


    def genBtnClicked(self):
        id_list = [c.getID for c in self.lsCustomer]
        generated = random.randint(11111111, 99999999)
        while (generated in id_list):
            generated = random.randint(11111111, 99999999)

        self.inID.setText(str(generated))

    def editClicked(self, item):
        if not self.list.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Figyelem!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Válassz ki egy ügyfelet a listából!")
            msg.exec()
        else:
            item = self.list.currentItem()
            tmp = item.text()
            tmp = tmp.split('(')
            id = tmp[1][:-2].split(" ")
            id = id[1]
            for i in self.lsCustomer:
                if id == i.getID():
                    self.inName.setText(i.getName())
                    self.inID.setText(i.getID())
                    self.inDate.setText(i.getDate())
                    self.inNum.setText(i.getNum())
                    self.inBalance.setText(i.getBalance())
                    self.inID.setReadOnly(True)

    def deleteItem(self):
        if not self.list.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Figyelem")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Válassz ki egy ügyfelet a listából!")
            msg.exec()
        else:
            item = self.list.currentItem()
            tmp = item.text()
            tmp = tmp.split('(')
            id = tmp[1][:-2].split(" ")
            id = id[1]
            for i in self.lsCustomer:
                if id == i.getID():
                    self.lsCustomer.remove(i)
                    self.saveToFile()
                    self.list.clear()
                    for j in self.lsCustomer:
                        self.list.addItem(j.__str__())

    def selectBtnClicked(self):
        try:
            min=int(self.inSelect.text())
            if min<=0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Figyelem!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Állíts be egy nullánál nagyobb értéket")
                msg.exec()
            if min>0:
                asd=''
                for i in self.lsCustomer:
                    if int(i.getBalance())>min:
                        asd+=(i.__str__()+"\n")
                if len(asd)==0:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Figyelem!')
                    msg.setText('Nincs ilyen gazdag ügyfelünk ')
                    msg.exec()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('A {}-nál több pénzzel rendelkező ügyfeleink'.format(min))
                    msg.setText(asd)
                    msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Egész számot adj meg kérlek, ez nem bitcoin")
            msg.exec()


    def saveToFile(self):
        try:
            outFile = open("database.txt", "w")
            for i in self.lsCustomer:
                print('{};{};{};{};{}\n'.format(i.getName(), i.getID(), i.getDate(), i.getNum(), i.getBalance()),
                      file=outFile)
            outFile.close()
        except FileNotFoundError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Nem találom az adatbázist")
            msg.exec()

    def reloadDatas(self):
        try:
            inFile = open("database.txt", "r")
            for i in inFile:
                if i.count(";") == 4:
                    tmp = i.split(';')
                    self.lsCustomer.append(mc.Customer(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4][:-1]))
            inFile.close()
            self.lsCustomer.sort()
            for i in self.lsCustomer:
                self.list.addItem(i.__str__())
        except FileNotFoundError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelem!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Az datbázis betöltése nem sikerült")
            msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

