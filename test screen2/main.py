import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

# Home Page Pictures
lst = []
lst.append("test screen2/Images/headphone.png")
lst.append("test screen2/Images/phone.png")
lst.append("test screen2/Images/lap top.png")
lst.append("test screen2/Images/hard.png")
lst.append("test screen2/Images/tv.png")
i = 0


# Home Page
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test screen2/HomePageFinal.ui", self)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.next.clicked.connect(self.next_clicked)
        self.previous.clicked.connect(self.previous_clicked)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        
        
    
    
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
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
        
   
        




# Categories Page       
        
class Categories(QDialog):
    def __init__(self):
        super(Categories, self).__init__()
        loadUi("test screen2/CategoryPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        
    
    
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
# Favorites Page       
        
class Favorites(QDialog):
    def __init__(self):
        super(Favorites, self).__init__()
        loadUi("test screen2/FavoritesPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

# Login Page         
        
class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("test screen2/LoginPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.SignInButton.clicked.connect(self.GoToSignIn)
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def GoToFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
   
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToSignIn(self):
        signin = SignIn()
        widget.addWidget(signin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
# Profile Page        
        
class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("test screen2/ProfilePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.LoginButton.clicked.connect(self.GoToLogin)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    
    
    def GoToFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
   
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
# Sign In Page        
        
class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("test screen2/SignInPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def GoToFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
   
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
         
   
        
        
    
        


#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(841)
widget.setFixedWidth(991)
categories = Categories()
widget.addWidget(categories)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
