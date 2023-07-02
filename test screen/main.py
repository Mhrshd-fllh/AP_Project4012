import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test screen/screen1.ui", self)
        self.Button1.clicked.connect(self.GoToScreen2)
        self.Button2.clicked.connect(self.GoToScreen3)
    
    
    def GoToScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        



class Screen3(QDialog):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("test screen/screen3.ui", self)
        self.Button1.clicked.connect(self.GoToScreen1)
        self.Button2.clicked.connect(self.GoToScreen2)    
    
    def GoToScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("test screen/screen2.ui", self)
        self.Button1.clicked.connect(self.GoToScreen1)
        self.Button2.clicked.connect(self.GoToScreen3)
    
    
    def GoToScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
         
    def GoToScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    
        


#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
