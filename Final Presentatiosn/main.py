import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from functools import partial
# Home Page Pictures
lst = []
lst.append("Final Presentatiosn/Images/headphone.png")
lst.append("Final Presentatiosn/Images/phone.png")
lst.append("Final Presentatiosn/Images/lap top.png")
lst.append("Final Presentatiosn/Images/hard.png")
lst.append("Final Presentatiosn/Images/tv.png")
i = 0

# Each Category Page Title Logic
EachCategoryPageTitle = "Phones"


# Home Page
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Final Presentatiosn/HomePageFinal.ui", self)
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
        widget.setCurrentIndex(widget.currentIndex()+2)
    
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+3)
        
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+4)
        
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
        loadUi("Final Presentatiosn/CategoryPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.HeadphonesButton.clicked.connect(self.GoToHeadphonesPage)
        self.PhonesButton.clicked.connect(self.GoToPhonesPage)
        self.LaptopsButton.clicked.connect(self.GoToLaptopsPage)
        self.TVButton.clicked.connect(self.GoToTVPage)
        self.HardButton.clicked.connect(self.GoToHardPage)
        self.USBButton.clicked.connect(self.GoToUSBPage)
        
    
    
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
        
    def GoToHeadphonesPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "Headphone"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
       
        
        
    def GoToPhonesPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "Phone"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
    def GoToLaptopsPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "Laptop"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def GoToTVPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "TV"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def GoToHardPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "Hard"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def GoToUSBPage(self):
        global EachCategoryPageTitle
        EachCategoryPageTitle = "USB"
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    
        
        
        
# Favorites Page       
        
class Favorites(QDialog):
    def __init__(self):
        super(Favorites, self).__init__()
        loadUi("Final Presentatiosn/FavoritesPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")        
        
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
        loadUi("Final Presentatiosn/LoginPageFinal.ui", self)
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
        loadUi("Final Presentatiosn/ProfilePageFinal.ui", self)
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
        loadUi("Final Presentatiosn/SignInPageFinal.ui", self)
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
        
#Each Category Page

class EachCategoryPage(QDialog):
    
    
    def __init__(self):
        super(EachCategoryPage, self).__init__()
        loadUi("Final Presentatiosn/EachCategoryPageFinal.ui", self)
        self.Category_Dict = {}
        f = open(f'Final Presentatiosn/Product_Names/{EachCategoryPageTitle}s_Name.txt', 'r')
        for m in f.readlines():
            self.Category_Dict[m] = ''
        self.BackButton.clicked.connect(self.GoToCategories)
        _translate = QtCore.QCoreApplication.translate
        self.TitleLable.setText(_translate("Dialog", EachCategoryPageTitle))
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in self.Category_Dict:
            temp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Cooper Black")
            font.setPointSize(14)
            temp.setFont(font)
            self.verticalLayout.addWidget(temp)
            temp.clicked.connect(partial(self.Pressed_For_Details,i))
            self.Category_Dict[i] = temp
        _translate = QtCore.QCoreApplication.translate
        for i in self.Category_Dict:
            self.Category_Dict[i].setText(_translate('Dialog', i))
    '''
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        for i in self.Category_Dict:
            self.Category_Dict[i].setText(_translate('Dialog', i))
    '''        
    def GoToCategories(self):
        categories = Categories()
        widget.addWidget(categories)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Pressed_For_Details(self, i):
        pass
        
# Product Hard Page
class ProductHardPage(QDialog):
    def __init__(self):
        super(ProductHardPage, self).__init__()
        loadUi("Final Presentatiosn/ProductHardPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


# Product Headphones Page
class ProductHeadphonesPage(QDialog):
    def __init__(self):
        super(ProductHeadphonesPage, self).__init__()
        loadUi("Final Presentatiosn/ProductHeadPhonePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        

# Product Laptops Page
class ProductLaptopsPage(QDialog):
    def __init__(self):
        super(ProductLaptopsPage, self).__init__()
        loadUi("Final Presentatiosn/ProductLaptopPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        

# Product Phones Page
class ProductPhonesPage(QDialog):
    def __init__(self):
        super(ProductPhonesPage, self).__init__()
        loadUi("Final Presentatiosn/ProductMobilePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Product TV Page
class ProductTVPage(QDialog):
    def __init__(self):
        super(ProductTVPage, self).__init__()
        loadUi("Final Presentatiosn/ProductTVPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Product USB Page
class ProductUSBPage(QDialog):
    def __init__(self):
        super(ProductUSBPage, self).__init__()
        loadUi("Final Presentatiosn/ProductTVPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)  
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        
        
    def GoToEachCategoryPage(self):
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
        
    def GoToHomePage(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def GoToProfile(self):
        profile = Profile()
        widget.addWidget(profile)
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
