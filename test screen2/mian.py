import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
lst = []
lst.append("test screen2/headphone.png")
lst.append("test screen2/phone.png")
lst.append("test screen2/lap top.png")
lst.append("test screen2/hard.png")
lst.append("test screen2/tv.png")
i = 0



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test screen2/HomePage.ui", self)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.next.clicked.connect(self.next_clicked)
        self.previous.clicked.connect(self.previous_clicked)
        
    
    
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
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
        
   
        




        
        
class Categories(QDialog):
    def __init__(self):
        super(Categories, self).__init__()
        loadUi("test screen2/category_page.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        
    
    
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
         
   
        
        
    
        


#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(870)
categories = Categories()
widget.addWidget(categories)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
