#RUNNN! Version 1.

# Here is what we need to import for Application
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from functools import partial
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import csv
from unidecode import unidecode
from googletrans import Translator, constants
import pandas as pd
translator = Translator()


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

#products name that we want to go through it for seeing details
CurrentProduct = ''

#Sites that we want to scrape for products
Site1 = ''
Site2 = ''
Site3 = ''

#Current User Id that is be gotten from Users.db
Current_User_ID = 0


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
        global CurrentProduct
        global Site1
        global Site2
        global Site3
        CurrentProduct = i.strip()
        if EachCategoryPageTitle == 'TV':
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Link_of_TVs.csv'))
            for temp_list in lines_list:
                temp_list = list(temp_list)
                if temp_list[0] == i:
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
            productTVpage = ProductTVPage()
            widget.addWidget(productTVpage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Phone':
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Links_of_Mobiles.csv'))
            for temp_list in lines_list:
                temp_list= list(temp_list)
                if temp_list[0] == CurrentProduct:
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
                else:
                    continue
            productPhonespage = ProductPhonesPage()
            widget.addWidget(productPhonespage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'USB':
            temp_list = list(temp_list)
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Link_of_USBs.csv'))
            for temp_list in lines_list:
                if temp_list[0] == CurrentProduct:
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
                else:
                    continue
            productUSBpage = ProductUSBPage()
            widget.addWidget(productUSBpage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Laptop':
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Link_of_Laptops.csv'))
            for temp_list in lines_list:
                temp_list = list(temp_list)
                if temp_list[0] == CurrentProduct:
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
                else:
                    continue
            productLaptopspage = ProductLaptopsPage()
            widget.addWidget(productLaptopspage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Headphone':
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Link_of_Headphones.csv'))
            for temp_list in lines_list:
                temp_list = list(temp_list)
                if str(temp_list[0]) == str(CurrentProduct):
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
                    break
                else:
                    continue
            productHeadphonespage = ProductHeadphonesPage()
            widget.addWidget(productHeadphonespage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Hard':
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Link_of_Hards.csv'))
            for temp_list in lines_list:
                if temp_list[0] == CurrentProduct:
                    Site1 = temp_list[1]
                    Site2 = temp_list[2]
                    Site3 = temp_list[3]
                else:
                    continue
            productHardpage = ProductHardPage()
            widget.addWidget(productHardpage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        
# Product Hard Page
class ProductHardPage(QDialog):
    def __init__(self):
        super(ProductHardPage, self).__init__()
        loadUi("Final Presentatiosn/ProductHardPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.UpdateButton.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        except:
            self.Image_Hard.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        
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

    def Update(self):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()

        self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        
        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too
        driver.close()



# Product Headphones Page
class ProductHeadphonesPage(QDialog):
    def __init__(self):
        super(ProductHeadphonesPage, self).__init__()
        loadUi("Final Presentatiosn/ProductHeadPhonePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.Update_Button.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image_Headphone.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        except:
            self.Image_Headphone.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        
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
        
    def Update(self):
        details_list = []
        details_list.append(CurrentProduct)
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/HeadPhoneImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image_Headphone.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        
        price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div/div[1]/span').text)
        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too
        with open('final Presentatiosn/Product_Details/Hard_Details.csv', 'w') as f:
            for i in range(0,7):
                f.write(details_list[i])
                if i != 6:
                    f.write(',')
            f.write('\n')
            
# Product Laptops Page
class ProductLaptopsPage(QDialog):
    def __init__(self):
        super(ProductLaptopsPage, self).__init__()
        loadUi("Final Presentatiosn/ProductLaptopPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.UpdateButton.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        except:
            self.Image.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        
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

    def Update(self):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/LaptopImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))

        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too    
        

# Product Phones Page
class ProductPhonesPage(QDialog):
    def __init__(self):
        super(ProductPhonesPage, self).__init__()
        loadUi("Final Presentatiosn/ProductMobilePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.UpdateButton.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png'))
        except:
            self.Image.setText(_translate("Dialog", 'Image Have Not been downloaded yet.')) 
        
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

    def Update(self):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png'))

        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too

# Product TV Page
class ProductTVPage(QDialog):
    def __init__(self):
        super(ProductTVPage, self).__init__()
        loadUi("Final Presentatiosn/ProductTVPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.UpdateButton.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image_TV.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        except:
            self.Image_TV.setText(_translate("Dialog", 'Image Have Not been downloaded yet.')) 
        
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

    def Update(self):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/TVImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image_TV.setPixmap(QtCore.QPixmap(f'Final Presentatiosn/Images/TVImage{CurrentProduct}.png'))

        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too

# Product USB Page
class ProductUSBPage(QDialog):
    def __init__(self):
        super(ProductUSBPage, self).__init__()
        loadUi("Final Presentatiosn/ProductTVPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)  
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.UpdateButton.clicked.connect(self.Update)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        except:
            self.Image_Hard.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        
        
        
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
    
    def Update(self):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/USBImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))

        driver.get(Site2)
        # Some work here
        driver.get(Site3)
        #Some work here too
         
   
        
        
    
def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(',')

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
