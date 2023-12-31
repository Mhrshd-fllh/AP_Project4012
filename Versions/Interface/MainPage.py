# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from selenium import webdriver
from selenium.webdriver.common.by import By


#setting up selenium



#Global Variables
Mobiles_Name = []
Mobiles_Prices = []
Mobiles_Links = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.Mobiles = {}
        #Getting The Dictionary of mobiles
        with open ('mobile_prices.txt', 'r') as m:
            for line in m.readlines():
                input_list= line.split(': ')
                Mobiles_Name.append(input_list[0])
                Mobiles_Prices.append(input_list[1])
                Mobiles_Links.append(input_list[2])
                self.Mobiles[f'{input_list[0]}\n\n{input_list[1]}']= ''
        '''
        with open('Digikala_Mobile_Prices.txt', 'r') as m2:
            for line in m2.readlines():
                input_list= line.split(': ')
                Mobiles_Name.append(input_list[0])
                Mobiles_Prices.append(input_list[1])
                self.Mobiles[f'{input_list[0]}\n{input_list[1]}']= ''
        '''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 1280, 720))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1278, 718))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.index = 0
        for i in self.Mobiles:
            temp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setPointSize(16)
            temp.setFont(font)
            temp.setObjectName(f'product{i}')
            self.verticalLayout.addWidget(temp)
            temp.clicked.connect(partial(self.Pressed, self.index))
            self.Mobiles[i] = temp
            self.index += 1

        self.HomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomeButton.setGeometry(QtCore.QRect(5, 5, 70, 70))
        self.HomeButton.setObjectName("HomeButton")
        self.ProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProfileButton.setGeometry(QtCore.QRect(80, 5, 70, 70))
        self.ProfileButton.setObjectName("ProfileButton")
        self.PageTitle = QtWidgets.QLabel(self.centralwidget)
        self.PageTitle.setGeometry(QtCore.QRect(300, 5, 315, 70))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PageTitle.setFont(font)
        self.PageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle.setObjectName("PageTitle")
        self.SearchBox = QtWidgets.QTextEdit(self.centralwidget)
        self.SearchBox.setGeometry(QtCore.QRect(710, 15, 500, 35))
        self.SearchBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SearchBox.setTabChangesFocus(False)
        self.SearchBox.setObjectName("SearchBox")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(1225, 15, 70, 35))
        self.SearchButton.setObjectName("SearchButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(155, 5, 70, 70))
        self.BackButton.setObjectName("BackButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
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
        for i in self.Mobiles:
            self.Mobiles[i].setText(_translate("MainWindow", i))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.ProfileButton.setText(_translate("MainWindow", "Profile"))
        self.PageTitle.setText(_translate("MainWindow", "Mobile"))
        self.SearchBox.setPlaceholderText(_translate("MainWindow", "Search Here"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
    
    def Pressed(self, i):
        driver = webdriver.Chrome()
        driver.get(f'{Mobiles_Links[i]}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
