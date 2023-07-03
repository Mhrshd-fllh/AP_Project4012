#RUNNN! Final Version


#Here We Import What We Need For This Program 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Here We Run Our Program 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())