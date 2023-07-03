#RUNNN! Final Version


#Here We Import What We Need For This Program 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Home Page(Qt designer)
lst = []
lst.append("Versions/Interface/home page/headphone.png")
lst.append("Versions/Interface/home page/phone.png")
lst.append("Versions/Interface/home page/lap top.png")
lst.append("Versions/Interface/home page/hard.png")
lst.append("Versions/Interface/home page/tv.png")
i = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo1 = QtWidgets.QLabel(self.centralwidget)
        self.photo1.setGeometry(QtCore.QRect(130, 180, 521, 331))
        self.photo1.setText("")
        self.photo1.setPixmap(QtGui.QPixmap("Versions/Interface/home page/tv.png"))
        self.photo1.setScaledContents(True)
        self.photo1.setObjectName("photo1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 381, 121))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(390, 510, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(270, 510, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.previous.setFont(font)
        self.previous.setObjectName("previous")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 550, 761, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 600, 751, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SearchBox = QtWidgets.QTextEdit(self.centralwidget)
        self.SearchBox.setGeometry(QtCore.QRect(520, 120, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.SearchBox.setFont(font)
        self.SearchBox.setObjectName("SearchBox")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(430, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCategories = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.actionCategories.setFont(font)
        self.actionCategories.setObjectName("actionCategories")
        self.actionProfile_Page = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.actionProfile_Page.setFont(font)
        self.actionProfile_Page.setObjectName("actionProfile_Page")
        self.actionLogin_Page = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.actionLogin_Page.setFont(font)
        self.actionLogin_Page.setObjectName("actionLogin_Page")
        self.actionFavorites = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.actionFavorites.setFont(font)
        self.actionFavorites.setObjectName("actionFavorites")
        self.menuMenu.addAction(self.actionCategories)
        self.menuMenu.addAction(self.actionProfile_Page)
        self.menuMenu.addAction(self.actionLogin_Page)
        self.menuMenu.addAction(self.actionFavorites)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.next.clicked.connect(self.next_clicked)
        self.previous.clicked.connect(self.previous_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Runnn!"))
        self.label.setText(_translate("MainWindow", "Home Page"))
        self.label_2.setText(_translate("MainWindow", "Runnn!"))
        self.next.setText(_translate("MainWindow", "NEXT"))
        self.previous.setText(_translate("MainWindow", "PREVIOUS"))
        self.label_3.setText(_translate("MainWindow", "Contact us via : @comfortablynumb7 on Telegram or 09908611517                                                                                          "))
        self.label_4.setText(_translate("MainWindow", "Company Address : Iran - Tehran - Narmak - IUST "))
        self.SearchBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cooper Black\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCategories.setText(_translate("MainWindow", "Categories"))
        self.actionProfile_Page.setText(_translate("MainWindow", "Profile "))
        self.actionLogin_Page.setText(_translate("MainWindow", "Login "))
        self.actionFavorites.setText(_translate("MainWindow", "Favorites"))

    def next_clicked(self):
            global i
            global lst
            i = i + 1
            if i > 4:
                i = 0
            self.photo1.setPixmap(QtGui.QPixmap(lst[i]))

    def previous_clicked(self):
            global i
            global lst
            i = i - 1
            if i < 0:
                i = 4
            self.photo1.setPixmap(QtGui.QPixmap(lst[i]))





#Here We Run Our Program 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())