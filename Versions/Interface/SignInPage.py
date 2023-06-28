# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignInPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.NameInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameInputLabel.setGeometry(QtCore.QRect(100, 150, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NameInputLabel.setFont(font)
        self.NameInputLabel.setObjectName("NameInputLabel")
        self.NameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.NameInput.setGeometry(QtCore.QRect(320, 150, 310, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameInput.setFont(font)
        self.NameInput.setObjectName("NameInput")
        self.EmailInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.EmailInputLabel.setGeometry(QtCore.QRect(100, 260, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EmailInputLabel.setFont(font)
        self.EmailInputLabel.setObjectName("EmailInputLabel")
        self.EmailInput = QtWidgets.QTextEdit(self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(320, 260, 310, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EmailInput.setFont(font)
        self.EmailInput.setObjectName("EmailInput")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(100, 480, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.LogInButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInButton.setGeometry(QtCore.QRect(320, 480, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LogInButton.setFont(font)
        self.LogInButton.setCheckable(False)
        self.LogInButton.setChecked(False)
        self.LogInButton.setAutoRepeat(False)
        self.LogInButton.setAutoDefault(False)
        self.LogInButton.setDefault(False)
        self.LogInButton.setFlat(False)
        self.LogInButton.setProperty("Wrap", False)
        self.LogInButton.setObjectName("LogInButton")
        self.PasswordInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordInputLabel.setGeometry(QtCore.QRect(100, 370, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PasswordInputLabel.setFont(font)
        self.PasswordInputLabel.setObjectName("PasswordInputLabel")
        self.PasswordInput = QtWidgets.QTextEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(320, 370, 310, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setObjectName("PasswordInput")
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
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.ProfileButton.setText(_translate("MainWindow", "Profile"))
        self.PageTitle.setText(_translate("MainWindow", "Sign In"))
        self.SearchBox.setPlaceholderText(_translate("MainWindow", "Search Here"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.NameInputLabel.setText(_translate("MainWindow", "Username:"))
        self.EmailInputLabel.setText(_translate("MainWindow", "Email:"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.LogInButton.setText(_translate("MainWindow", "Login"))
        self.PasswordInputLabel.setText(_translate("MainWindow", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
