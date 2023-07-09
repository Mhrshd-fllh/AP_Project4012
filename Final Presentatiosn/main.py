#RUNNN! Version 1.

# Here is what we need to import for Application
import Database
import TV
import Phone
import Headphone
import Hard
import Laptop
import USB
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
import time



translator = Translator()




#A list that will be used for comparing products and its maximum length will be 2
Compare_List = []

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


Matching_List = []
# Home Page
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Final Presentatiosn/HomePageFinal.ui", self)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.next.clicked.connect(self.next_clicked)
        self.previous.clicked.connect(self.previous_clicked)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        if Current_User_ID == 0:
            self.LoginButton.clicked.connect(self.GoToLogin)
        else:
            self.LoginButton.clicked.connect(self.GoToProfile)
        if Current_User_ID != 0:
            self.ProfileButton.clicked.connect(self.GoToProfile)
        else:
            self.ProfileButton.clicked.connect(self.GoToLogin)
        
        self.SearchButton.clicked.connect(partial(Search,self.SearchBox.text()))
        
    
    
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
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        
    
    
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
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))        
        
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
        self.SubmitButton.clicked.connect(self.LogIn)
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        
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

    def LogIn(self, Current):
        global Current_User_ID
        Done_Flag = 0
        User_Name = self.NameInput.text()
        User_Password = self.PasswordInput.text()
        Done_Flag , Current_User_ID = Database.Login(User_Name, User_Password)
        if Done_Flag == 0:
            Exit_text = QtWidgets.QInputDialog.getText(self,'Error' , Current_User_ID + 'Type Exit')
            self.NameInput.clear()
            self.PasswordInput.clear()
            Current_User_ID = 0
        else:
            self.GoToProfile()


# Profile Page        
class Profile(QDialog):
    global Current_User_ID
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Final Presentatiosn/ProfilePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        if Current_User_ID == 0:
            self.LoginButton.clicked.connect(self.GoToLogin)
        _translate =QtCore.QCoreApplication.translate
        User_Name, User_Email = Database.Show_User_Info(Current_User_ID)
        self.NameLabel_Output.setText(_translate('Dialog', User_Name))
        self.EmailLabel_Output.setText(_translate('Dialog', User_Email))
        self.PasswordReset.clicked.connect(self.ChangePassword)
        self.Logout_Button.clicked.connect(self.GoToLogin)
        self.Logout_Button.clicked.connect(self.Logout)
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        
        
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

    def ChangePassword(self):
        Old, state = QtWidgets.QInputDialog.getText(self, "Change Password", "Old Password: ")
        New, state = QtWidgets.QInputDialog.getText(self, "Change Password", "New Password: ")
        Database.Change_Password(Current_User_ID, Old, New)

    def Logout(self):
        global Current_User_ID
        Current_User_ID = 0
        

# Sign In Page        
class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("Final Presentatiosn/SignInPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.FavoritesButton.clicked.connect(self.GoToFavorites)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.LogInButton.clicked.connect(self.GoToLogin)
        self.SubmitButton.clicked.connect(self.Register)
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))

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
    
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Register(self):
        global Current_User_ID
        Done_Flag = 0
        User_Name = self.NameInput.text()
        Email = self.EmailInput.text()
        Password = self.PaasswordInput.text()
        
        Done_Flag , Current_User_ID = Database.Register(User_Name, Email, Password)
        if Done_Flag == 0:
            Exit_text, state = QtWidgets.QInputDialog.getText(self,'Error' ,  Current_User_ID + 'Incorrect Password')
            self.NameInput.clear()
            self.EmailInput.clear()
            self.PasswordInput.clear()
            Current_User_ID = 0
        else:
            self.GoToProfile()


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
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in self.Category_Dict:
            temp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Cooper Black")
            font.setPointSize(14)
            temp.setFont(font)
            self.verticalLayout.addWidget(temp)
            if len(Compare_List) != 2:
                temp.clicked.connect(partial(self.Pressed_For_Details,i))
            else:
                temp.clicked.connect(partial(self.Pressed_For_Compare,i))
            self.Category_Dict[i] = temp
        _translate = QtCore.QCoreApplication.translate
        for i in self.Category_Dict:
            self.Category_Dict[i].setText(_translate('Dialog', i))
       
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
            lines_list = list(csv_reader('Final Presentatiosn/Product_Links/Links_of_TVs.csv'))
            for temp_list in lines_list:
                temp_list = list(temp_list)
                if temp_list[0] == CurrentProduct:
                    Site1 = temp_list[1]
                    Site3 = temp_list[2]
                    Site2 = temp_list[3]
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
        
    def Pressed_For_Compare(self, i):
        global Compare_List
        Compare_List.append(i.strip())
        if EachCategoryPageTitle == 'TV':
            tvcompare = TVComparePage()
            widget.addWidget(tvcompare)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Phone':
            phonecompare = PhoneComparePage()
            widget.addWidget(phonecompare)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Headphone':
            headphonecompare = HeadphonesComparePage()
            widget.addWidget(headphonecompare)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'USB':
            usbcompare = USBComparePage()
            widget.addWidget(usbcompare)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Laptop':
            laptopcompare = LaptopComparePage()
            widget.addWidget(laptopcompare)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif EachCategoryPageTitle == 'Hard':
            hardcompare = HardComparePage()
            widget.addWidget(hardcompare)
            widget.setCurrentIndex(widget.currentIndex()+1)





# Product Hard Page
class ProductHardPage(QDialog):
    def __init__(self):
        super(ProductHardPage, self).__init__()
        self.PictureFlag = 0
        loadUi("Final Presentatiosn/ProductHardPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
            self.PictureFlag = 1
        except:
            self.Image_Hard.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        Done = Hard.Check_For_Product(CurrentProduct, False)
        if Done == 1:
            Details = Hard.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate("Dialog", Details[0]))
            self.Storage_Label.setText(_translate("Dialog", Details[1]))
            self.Speed_Label.setText(_translate("Dialog", Details[2]))
            self.Connection_Label.setText(_translate("Dialog", Details[3]))
            self.DigiKala_Label.setText(_translate("Dialog", Details[4]))
            self.MeghdadITLabel.setText(_translate("Dialog", Details[5]))
            self.TechnoLife_Label.setText(_translate('Dialog',Details[6]))
            widget.update()
        self.UpdateButton.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(self.Compare)
        
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

    def Compare(self):
        global Compare_List
        Compare_List.append(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Update(self, Done):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()

        self.Image_Hard.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{CurrentProduct}.png'))
        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:                                          
            Price1 = 'Not Available'
        if Price1 == 'Not Available':
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
            except:
                Price1 = 'Not Available'
        self.DigiKala_Label.setText(_translate('Dialog',Price1))
        
        driver.get(Site3)
        time.sleep(10)
        try: 
            Price3_tmp = driver.find_element(By.XPATH, '//*[@id="lblPrice"]').text
            Price3 = Price3_tmp.split(' ')[0]
        except:
            Price3 = 'Not Available'
        self.MeghdadITLabel.setText(_translate('Dialog',Price3))

        driver.get(Site2)
        time.sleep(15)
        try:
            Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[3]/div[2]/h6/span[1]').text)
        except:                                             
            Price2 = 'Not Available'
        if Price2 == 'Not Available':
            try:
                Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[2]/div/').text)
                Price2 = Price2.split(' ')[0]
            except:
                Price2 = 'Not Available'
        self.TechnoLife_Label.setText(_translate('Dialog',Price2))
        if Done ==0:
            Storage = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[2]/div[2]').text)
            self.Storage_Label.setText(_translate('Dialog',Storage.text))
            Speed = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[4]/div[2]').text)
            self.Speed_Label.setText(_translate('Dialog',Speed.text))
            Connection = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[1]/div[2]').text)
            self.Connection_Label.setText(_translate('Dialog',Connection.text))
            Hard.Get_Product(CurrentProduct, Storage.text, Speed.text, Connection.text, Price1,Price2,Price3,EachCategoryPageTitle)
        else:
            Hard.Update_Price(CurrentProduct,Price1,Price2,Price3)
        driver.close()


# Product Headphones Page
class ProductHeadphonesPage(QDialog):
    def __init__(self):
        super(ProductHeadphonesPage, self).__init__()
        self.PictureFlag = 0
        loadUi("Final Presentatiosn/ProductHeadPhonePageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        if Current_User_ID != 0:
            self.ProfileButton.clicked.connect(self.GoToProfile)
        else:
            self.ProfileButton.clicked.connect(self.GoToLogin)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        Done = Headphone.Check_For_Product(CurrentProduct,False)
        _translate = QtCore.QCoreApplication.translate
        if Done:
            Details = Headphone.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate("Dialog",Details[0]))
            self.Version_Label.setText(_translate("Dialog",Details[1]))
            self.Connection_Label.setText(_translate("Dialog",Details[2]))
            self.USBPort_Label.setText(_translate("Dialog",Details[3]))
            self.Battery_Label.setText(_translate("Dialog",Details[4]))
            self.Weight_Label.setText(_translate("Dialog",Details[5]))
            self.Digikala_Label.setText(_translate('Dialog', Details[6]))
            self.TechnoLife_Label.setText(_translate('Dialog', Details[7]))
            self.MeghdadIT_Label.setText(_translate('Dialog', Details[8]))
        widget.update()
        try:
            self.Image_Headphone.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HeadPhoneImage{CurrentProduct}.png'))
        except:
            self.Image_Headphone.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        self.Update_Button.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(self.Compare)
        
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
    
    def GoToLogin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Compare(self):
        global Compare_List
        Compare_List.append(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Update(self,Done):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)  
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/HeadPhoneImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image_Headphone.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HeadPhoneImage{CurrentProduct}.png'))
        
        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:                                          
            Price1 = 'Not Available'
        if Price1 == 'Not Available':
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
                Price1 = Price1.split(' ')[0]
            except:
                Price1 = 'Not Available'
        self.Digikala_Label.setText(_translate('Dialog',Price1))
        
        driver.get(Site3)
        time.sleep(10)
        try: 
            Price3_tmp = driver.find_element(By.XPATH, '//*[@id="lblPrice"]').text
            Price3 = Price3_tmp.split(' ')[0]
        except:
            Price3 = 'Not Available'
        self.MeghdadIT_Label.setText(_translate('Dialog',Price3))
        driver.get(Site2)
        time.sleep(15)
        try:
            Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[3]/div[2]').text)
            Price2 = Price2.split(' ')[0]
        except:                                             
            Price2 = 'Not Available'
        if Price2 == 'Not Available':
            try:
                Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[2]/div/h6/span[1]').text)
            except:
                pass
        self.TechnoLife_Label.setText(_translate('Dialog',Price2))
        if Done == 0:
            self.Name_Label.setText(_translate('Dialog', CurrentProduct))
            Version = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-2"]/li[3]/div[2]').text)
            self.Version_Label.setText(_translate('Dialog', Version.text))
            Connection = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-2"]/li[2]/div[2]').text)    
            self.Connection_Label.setText(_translate('Dialog', Connection.text))
            try:
                USBPort = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-4"]/li[4]/div[2]').text)
            except:
                USBPort = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-2"]/li[4]/div[2]').text)
            self.USBPort_Label.setText(_translate('Dialog', USBPort.text))
            try:
                Battery = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-4"]/li[3]/div[2]').text)
            except:
                Battery = 'No Battery'
            self.Battery_Label.setText(_translate('Dialog', Battery.text)) if type(Battery) != str else self.Battery_Label.setText(_translate('Dialog', Battery))
            Weight = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-0"]/li[1]/div[2]').text)
            self.Weight_Label.setText(_translate('Dialog', Weight.text))
            Headphone.Get_Product(CurrentProduct, Version.text, Connection.text, USBPort.text if type(USBPort) != str else USBPort, Battery.text if type(Battery) != str else Battery, Weight.text, Price1,Price2,Price3,EachCategoryPageTitle)
        else:
            Headphone.Update_Price(CurrentProduct,Price1,Price2,Price3)
        driver.close()


# Product Laptops Page
class ProductLaptopsPage(QDialog):
    def __init__(self):
        super(ProductLaptopsPage, self).__init__()
        self.PictureFlag = 0
        loadUi("Final Presentatiosn/ProductLaptopPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/LaptopImage{CurrentProduct}.png'))
            self.PictureFlag = 1
        except:
            self.Image.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        Done = Laptop.Check_For_Product(CurrentProduct, False)
        if Done == 1:
            Details = Laptop.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate("Dialog",Details[0]))
            self.RAM_Label.setText(_translate("Dialog",Details[1]))
            self.Storage_Label.setText(_translate("Dialog",Details[2]))
            self.CPU_Label.setText(_translate("Dialog",Details[3]))
            self.USBPort_Label.setText(_translate("Dialog",Details[4]))
            self.Battery_Label.setText(_translate("Dialog",Details[5]))
            self.Size_Label.setText(_translate("Dialog",Details[6]))
            self.Weight_Label.setText(_translate("Dialog",Details[7]))
            self.Digikala_Label.setText(_translate("Dialog",Details[8]))
            self.TechonLife_Label.setText(_translate("Dialog",Details[9]))
            self.MeghdadIT_Label.setText(_translate("Dialog",Details[10]))
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))    
        self.UpdateButton.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(partial(self.Compare))

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

    def Compare(self):
        global Compare_List
        Compare_List.append(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Update(self, Done):
        _translate = QtCore.QCoreApplication.translate
        
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)
        
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)
        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/LaptopImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/LaptopImage{CurrentProduct}.png'))

        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:                                          
            Price1 = 'Not Available'
        if Price1 == 'Not Available':
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
            except:
                Price1 = 'Not Available'
        self.Digikala_Label.setText(_translate('Dialog',Price1))
        
        driver.get(Site3)
        time.sleep(10)
        try: 
            Price3_tmp = driver.find_element(By.XPATH, '//*[@id="lblPrice"]').text
            Price3 = Price3_tmp.split(' ')[0]
        except:
            Price3 = 'Not Available'
        self.MeghdadIT_Label.setText(_translate('Dialog',Price3))

        driver.get(Site2)
        time.sleep(10)
        try:
            Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[3]/div[2]/h6/span[1]').text)
        except:                                             
            Price2 = 'Not Available'
        if Price2 == 'Not Available':
            try:
                Price2 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[2]/div').text)
                Price2 = Price2.split(' ')[0]
            except:
                pass
        self.TechonLife_Label.setText(_translate('Dialog',Price2))
        if Done == 0:
            self.Name_Label.setText(_translate('Dialog', CurrentProduct))
            Ram = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-4"]/li[1]/div[2]').text)
            self.RAM_Label.setText(_translate('Dialog',Ram.text))
            Storage = translator.translate(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[1]/div/ul/li[1]/h3/span').text)
            Storage = Storage.text
            Storage = Storage.split(": ")[1]
            self.Storage_Label.setText(_translate('Dialog',Storage))
            Cpu = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-3"]/li[1]/div[2]').text)
            self.CPU_Label.setText(_translate('Dialog',Cpu.text))
            USBPort = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-7"]/li[6]/div[2]').text)
            self.USBPort_Label.setText(_translate('Dialog',USBPort.text))
            try:    
                Battery = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-9"]/li[1]/div[2]').text)
            except:
                Battery = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-8"]/li[1]/div[2]').text)
            self.Battery_Label.setText(_translate('Dialog', Battery.text))
            Size = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-2"]/li[1]/div[2]').text)
            self.Size_Label.setText(_translate('Dialog', Size.text))
            Weight = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[2]/div[2]').text)
            self.Weight_Label.setText(_translate('Dialog', Weight.text))
            Laptop.Get_Product(CurrentProduct, Ram.text, Storage,Cpu.text,USBPort.text, Battery.text, Size.text,Weight.text,Price1,Price2,Price3,EachCategoryPageTitle)
        else:
            Laptop.Update_Price(CurrentProduct, Price1,Price2,Price3)
        driver.close()    
        

# Product Phones Page
class ProductPhonesPage(QDialog):
    def __init__(self):
        super(ProductPhonesPage, self).__init__()
        loadUi("Final Presentatiosn/ProductMobilePageFinal.ui", self)
        self.PictureFlag = 0
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png'))
            self.PictureFlag = 1
        except:
            self.Image.setText(_translate("Dialog", 'Image Have Not been downloaded yet.')) 
        Done = Phone.Check_For_Product(CurrentProduct, False)
        if Done == 1:
            Details = Phone.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate('Dialog',Details[0]))
            self.RAM_Label.setText(_translate('Dialog',Details[1]))
            self.Storage_Label.setText(_translate('Dialog',Details[2]))
            self.Camera_Label.setText(_translate('Dialog',Details[3]))
            self.SimCard_Label.setText(_translate('Dialog',Details[4]))
            self.Battery_Label.setText(_translate('Dialog',Details[5]))
            self.Size_Label.setText(_translate('Dialog',Details[6]))
            self.Weight_Label.setText(_translate('Dialog', Details[7]))
            self.Digikala_Label.setText(_translate('Dialog',Details[8]))
            self.Mobile_Label.setText(_translate('Dialog', Details[9]))
            self.MeghdadIT_Label.setText(_translate('Dialog', Details[10]))
            widget.update()
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        self.UpdateButton.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(self.Compare)

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

    def Compare(self):
        global Compare_List
        Compare_List.append(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Update(self, Done):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)
        
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{CurrentProduct}.png'))
        
        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:                                          
            Price1 = 'Not Available'
        if Price1 == 'Not Available':
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
            except:                                             
                Price1 = 'Not Available'
        self.Digikala_Label.setText(_translate('Dialog',Price1))
        driver.get(Site3)
        time.sleep(10)
        try: 
            Price3_tmp = driver.find_element(By.XPATH, '//*[@id="lblPrice"]').text
            Price3 = Price3_tmp.split(' ')[0]
        except:
            Price3 = 'Not Available'
        self.MeghdadIT_Label.setText(_translate('Dialog',Price3))


        driver.get(Site2)
        Price2 = translator.translate(driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div[3]/div[2]/div[1]/div[1]/div[1]/ul/li[2]/a').text)
        self.Mobile_Label.setText(_translate('Dialog',Price2.text))
        if Done == 0:
            Storage_and_RAM = driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[5]/div/ul/li[2]/strong/span').text
            Storage_and_RAM = Storage_and_RAM.split(', ')[0]
            Storage , Ram = Storage_and_RAM.split(' ')[0] , Storage_and_RAM.split(' ')[1]
            self.RAM_Label.setText(_translate('Dialog',Ram))
            self.Storage_Label.setText(_translate('Dialog',Storage))
            Camera = translator.translate(driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[6]/div/ul/li[1]/strong/span').text)
            Camera = Camera.text
            Camera = Camera.split(',')[0]
            self.Camera_Label.setText(_translate('Dialog',Camera))
            try:
                SimCard = translator.translate(driver.find_element(By.XPATH,'//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[1]/div/ul/li[4]/strong/span').text)
            except:
                SimCard = translator.translate(driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[1]/div/ul/li[11]/strong/span').text)
            self.SimCard_Label.setText(_translate('Dialog',SimCard.text))
            Battery = translator.translate(driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[10]/div/ul/li[1]/strong/span').text)
            self.Battery_Label.setText(_translate('Dialog',Battery.text))
            Size = translator.translate(driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[2]/div/ul/li[1]/strong/span').text)
            self.Size_Label.setText(_translate('Dialog',Size.text))
            Weight = translator.translate(driver.find_element(By.XPATH, '//*[@id="maincolumn"]/div[3]/div[2]/div[2]/div[2]/div[2]/div/ul/li[2]/strong/span').text)
            self.Weight_Label.setText(_translate('Dialog',Weight.text))
            Phone.Get_Product(CurrentProduct, Ram, Storage, Camera, SimCard.text, Battery.text, Size.text, Weight.text, Price1, Price2.text, Price3, EachCategoryPageTitle)
        else:
            Phone.Update_Price(CurrentProduct, Price1,Price2,Price3)
        driver.close()


# Product TV Page
class ProductTVPage(QDialog):
    def __init__(self):
        super(ProductTVPage, self).__init__()
        loadUi("Final Presentatiosn/ProductTVPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        Done = TV.Check_For_Product(CurrentProduct,False)
        if Done == 1:
            Details = TV.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate('Dialog', Details[0]))
            self.Size_Label.setText(_translate('Dialog', Details[1]))
            self.Resolution_Label.setText(_translate('Dialog', Details[2]))
            self.Quality_Label.setText(_translate('Dialog', Details[3]))
            self.ScreenTech_Label.setText(_translate('Dialog', Details[4]))
            self.DigiKala_Label.setText(_translate('Dialog', Details[5]))
            self.HyperKhanegi_Label.setText(_translate('Dialog', Details[6]))
            self.TechnoLife_Label.setText(_translate('Dialog', Details[7]))
            widget.update()
        try:
            self.Image_TV.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/TVImage{CurrentProduct}.png'))
            self.PictureFlag = 1
        except:
            self.Image_TV.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text())) 
        self.UpdateButton.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(self.Compare)
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

    def Compare(self):
        global Compare_List
        Compare_List.add(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Update(self, Done):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/TVImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.Image_TV.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/TVImage{CurrentProduct}.png'))
        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:                                          
            Price1 = 'Not Available'
        if Price1 == 'Not Available':
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
            except:
                Price1 = 'Not Available'
        self.DigiKala_Label.setText(_translate('Dialog',Price1))
        
        driver.get(Site2)
        time.sleep(7)
        Price2 = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div/span').text
        Price2 = Price2.split(' ')[0]
        self.HyperKhanegi_Label.setText(_translate('Dialog', Price2))
        driver.get(Site3)
        try:
            Price3 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[3]/div[2]/h6/span[1]').text)
        except:                                             
            Price3 = 'Not Available'
        if Price3 == 'Not Available':
            try:
                Price3 = unidecode(driver.find_element(By.XPATH, '//*[@id="productP1"]/div[3]/div[2]/div').text)
                Price3 = Price3.split(' ')[0]
            except:                                              
                pass
            self.TechnoLife_Label.setText(_translate('Dialog', Price3))
        if Done == 0:
            Size = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-0"]/li[2]/div[2]').text)
            self.Size_Label.setText(_translate('Dialog', Size.text))
            Resolution = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[2]/div[2]').text)
            self.Resolution_Label.setText(_translate('Dialog',Resolution.text))
            Quality = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-1"]/li[1]/div[2]').text)
            self.Quality_Label.setText(_translate('Dialog',Quality.text))
            ScreenTech = translator.translate(driver.find_element(By.XPATH, '//*[@id="accordion__panel-0"]/li[3]/div[2]').text)
            self.ScreenTech_Label.setText(_translate('Dialog',ScreenTech.text))
            TV.Get_Product(CurrentProduct,Size.text, Resolution.text, Quality.text,ScreenTech.text, Price1, Price2, Price3, EachCategoryPageTitle)
        else:
            TV.Update_Price(CurrentProduct, Price1, Price2, Price3)

        driver.close()
        

# Product USB Page
class ProductUSBPage(QDialog):
    def __init__(self):
        super(ProductUSBPage, self).__init__()
        self.PictureFlag = 0
        loadUi("Final Presentatiosn/ProductUSBPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)  
        self.ProfileButton.clicked.connect(self.GoToProfile)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        try:
            self.USB_Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/USBImage{CurrentProduct}.png'))
            self.PictureFlag = 1
        except:
            self.USB_Image.setText(_translate("Dialog", 'Image Have Not been downloaded yet.'))
        Done = USB.Check_For_Product(CurrentProduct, False)
        if Done == 1:
            Details = USB.Show_Details(CurrentProduct)
            self.Name_Label.setText(_translate('Dialog', Details[0]))
            self.Storage_Label.setText(_translate('Dialog', Details[1]))
            self.Speed_Label.setText(_translate('Dialog',Details[2]))
            self.Version_Label.setText(_translate('Dialog', Details[3]))
            self.DigiKala_Label.setText(_translate('Dialog', Details[4]))
            self.MeghdadITLabel.setText(_translate('Dialog', Details[5]))
            self.TechnoSun_Label.setText(_translate('Dialog', Details[6]))
        self.SearchButton.clicked.connect(partial(Search, self.SearchBox.text()))
        self.UpdateButton.clicked.connect(partial(self.Update, Done))
        self.CompareButton.clicked.connect(self.Compare)
        
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

    def Compare(self):
        global Compare_List
        Compare_List.append(CurrentProduct)
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Update(self, Done):
        _translate = QtCore.QCoreApplication.translate
        self.Name_Label.setText(_translate('Dialog', CurrentProduct))
        driver = webdriver.Chrome()
        driver.get(Site1)
        time.sleep(10)
        
        Image = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img')
        Image_Source = Image.get_property('src')
        respond = requests.get(Image_Source)

        if respond.status_code:
                filepic = open(f'Final Presentatiosn/Images/USBImage{CurrentProduct}.png', 'wb')
                filepic.write(respond.content)
                filepic.close()
        self.USB_Image.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/USBImage{CurrentProduct}.png'))
        
        try:
            Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[8]/div/div/div[1]/div[2]/div[2]/span').text)
        except:
            try:
                Price1 = unidecode(driver.find_element(By.XPATH, '//*[@id="sellerSection"]/div/div[2]/div[1]/div[2]/div[1]/div/div/span').text)
            except:
                Price1 = 'Not Available'
        self.DigiKala_Label.setText(_translate('Dialog',Price1))
        driver.get(Site3)
        time.sleep(15)
        try: 
            Price2_tmp = driver.find_element(By.XPATH, '//*[@id="lblPrice"]').text
            Price2 = Price2_tmp.split(' ')[0]
        except:
            Price2 = 'Not Available'
        self.MeghdadITLabel.setText(_translate('Dialog',Price2))
        driver.get(Site2)
        try:
            Price3 = unidecode(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[1]/div/div[2]/div[2]/div[2]/div/span[1]').text)
        except:
            Price3 = 'Not Available'
        self.TechnoSun_Label.setText(_translate('Dialog',Price3))
        if Done == 0:
            _ = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div/div/div[1]/div[1]/button[2]').click()
            try:
                Storage = translator.translate(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div/div/div[1]/div[3]/div/div[2]/div[5]/div/span[2]').text)
                Storage = Storage.text
                Storage = Storage.split(' - ')[0]
            except:
                Storage = CurrentProduct.split(' ')[-2]
            self.Storage_Label.setText(_translate('Dialog', Storage))
            try:
                Speed = translator.translate(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div/div/div[1]/div[3]/div/div[2]/div[4]/div/span[2]').text)
                Speed = Speed.text
            except:
                Speed = 'Not Available'
            
            self.Speed_Label.setText(_translate('Dialog', Speed)) 
            try:
                Version = translator.translate(driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div/div/div[1]/div[3]/div/div[2]/div[2]/div/span[2]').text)
                Version = Version.text
            except:
                Version = 'Not Available'
            self.Version_Label.setText(_translate('Dialog', Version))
            USB.Get_Product(CurrentProduct,Storage, Speed, Version, Price1,Price2,Price3,EachCategoryPageTitle)
        else:
            USB.Update_Price(CurrentProduct,Price1,Price2,Price3)    
        time.sleep(10)
        
        
        driver.close()
        
#Search Result Page       
class SearchResult(QDialog):
    def __init__(self):
        global Search_Matching_list
        super(SearchResult, self).__init__()
        loadUi("Final Presentatiosn/SearchResultPageFinal.ui", self)
        self.HomeButton.clicked.connect(self.GoToHomePage)
        self.CategoriesButton.clicked.connect(self.GoToCategories)
        self.LoginButton.clicked.connect(self.GoToLogin)
        self.ProfileButton.clicked.connect(self.GoToProfile)
        _translate = QtCore.QCoreApplication.translate
        self.Search_Dict = {}
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        for i in self.Search_Dict:
            temp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            font = QtGui.QFont()
            font.setFamily("Cooper Black")
            font.setPointSize(20)
            temp.setFont(font)
            self.verticalLayout.addWidget(temp)
            temp.clicked.connect(partial(self.Pressed_For_Details,i))
            self.Search_Dict[i] = temp
        for i in self.Search_Dict:
            self.search_Dict[i].setText(_translate("Dialog", i))
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
        
         

def Search(text):
    global Matching_list
    Tv_check_Match = TV.Check_For_Product(text, True)
    Headphone_check_Match = Headphone.Check_For_Product(text, True)
    Hard_check_Match = Hard.Check_For_Product(text, True)
    USB_check_Match = USB.Check_For_Product(text,True)
    Phone_check_Match = Phone.Check_For_Product(text,True)
    Laptop_check_Match = Laptop.Check_For_Product(text,True)
    for m in Tv_check_Match:
        Matching_List.append(m)
    for m in Headphone_check_Match:
        Matching_List.append(m)
    for m in Hard_check_Match:
        Matching_List.append(m)
    for m in USB_check_Match:
        Matching_List.append(m)
    for m in Phone_check_Match:
        Matching_List.append(m)
    for m in Laptop_check_Match:
        Matching_List.append(m)
    
    search = SearchResult()
    widget.addWidget(search)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    
    
    
# Headphone Compare Page
class HeadphonesComparePage(QDialog):
    def __init__(self):
        super(HeadphonesComparePage, self).__init__()
        loadUi("Final Presentatiosn/HeadphoneComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HeadPhoneImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HeadPhoneImage{Compare_List[2]}.png'))
        Details1 = Headphone.Show_Details(Compare_List[0])
        Details2 = Headphone.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.Version_Label.setText(_translate('Dialog', Details1[1]))
        self.Connection_Label.setText(_translate('Dialog', Details1[2]))
        self.USBPort_Label.setText(_translate('Dialog', Details1[3]))
        self.Battery_Label.setText(_translate('Dialog', Details1[4]))
        self.Digikala_Label.setText(_translate('Dialog',Details1[6]))
        self.TechnoLife_Label.setText(_translate('Dialog', Details1[7]))
        self.MeghdadIT_Label.setText(_translate('Dialog', Details1[8]))
        self.Name_Label_2.setText(_translate('Dialog', Details2[0]))
        self.Version_Label_2.setText(_translate('Dialog', Details2[1]))
        self.Connection_Label_2.setText(_translate('Dialog', Details2[2]))
        self.USBPort_Label_2.setText(_translate('Dialog', Details2[3]))
        self.Battery_Label_2.setText(_translate('Dialog', Details2[4]))
        self.Digikala_Label_2.setText(_translate('Dialog',Details2[6]))
        self.TechnoLife_Label_2.setText(_translate('Dialog', Details2[7]))
        self.MeghdadIT_Label_2.setText(_translate('Dialog', Details2[8]))

    def GoToEachCategoryPage(self):
        global Compare_List
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        Compare_List = []
        
        
        
# phone Compare Page
class PhoneComparePage(QDialog):
    def __init__(self):
        super(PhoneComparePage, self).__init__()
        loadUi("Final Presentatiosn/phoneComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/PhoneImage{Compare_List[2]}.png'))
        Details1 = Phone.Show_Details(Compare_List[0])
        Details2 = Phone.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.RAM_Label.setText(_translate('Dialog', Details1[1]))
        self.Storage_Label.setText(_translate('Dialog', Details1[2]))
        self.Camera_Label.setText(_translate('Dialog', Details1[3]))
        self.SimCard_Label.setText(_translate('Dialog', Details1[4]))
        self.Digikala_Label.setText(_translate('Dialog', Details1[8]))
        self.Mobile_Label.setText(_translate('Dialog', Details1[9]))
        self.MeghdadIT_Label.setText(_translate('Dialog', Details1[10]))
        self.Name_Label_2.setText(_translate('Dialog', Details2[0]))
        self.RAM_Label_2.setText(_translate('Dialog', Details2[1]))
        self.Storage_Label_2.setText(_translate('Dialog', Details2[2]))
        self.Camera_Label_2.setText(_translate('Dialog', Details2[3]))
        self.SimCard_Label_2.setText(_translate('Dialog', Details2[4]))
        self.Digikala_Label_2.setText(_translate('Dialog', Details2[8]))
        self.Mobile_Label_2.setText(_translate('Dialog', Details2[9]))
        self.MeghdadIT_Label_2.setText(_translate('Dialog', Details2[10]))
        
    def GoToEachCategoryPage(self):
        global Compare_List
        Compare_List = [] 
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
# Hard Compare Page
class HardComparePage(QDialog):
    def __init__(self):
        super(HardComparePage, self).__init__()
        loadUi("Final Presentatiosn/HardComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/HardImage{Compare_List[2]}.png'))
        Details1 = Hard.Show_Details(Compare_List[0])
        Details2 = Hard.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.Storage_Label.setText(_translate('Dialog', Details1[1]))
        self.Speed_Label.setText(_translate('Dialog', Details1[2]))
        self.Connection_Label.setText(_translate('Dialog', Details1[3]))
        self.DigiKala_Label.setText(_translate('Dialog', Details1[4]))
        self.MeghdadITLabel.setText(_translate('Dialog', Details1[5]))
        self.TechnoLife_Label.setText(_translate('Dialog', Details1[6]))
        self.Name_Label_2.setText(_translate('Dialog', Details2[0]))
        self.Storage_Label_2.setText(_translate('Dialog', Details2[1]))
        self.Speed_Label_2.setText(_translate('Dialog', Details2[2]))
        self.Connection_Label_2.setText(_translate('Dialog', Details2[3]))
        self.DigiKala_Label_2.setText(_translate('Dialog', Details2[4]))
        self.MeghdadITLabel_2.setText(_translate('Dialog', Details2[5]))
        self.TechnoLife_Label_2.setText(_translate('Dialog', Details2[6]))
        
    def GoToEachCategoryPage(self):
        global Compare_List
        Compare_List = []
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
# Laptop Compare Page
class LaptopComparePage(QDialog):
    def __init__(self):
        super(LaptopComparePage, self).__init__()
        loadUi("Final Presentatiosn/LaptopComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/LaptopImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/LaptopImage{Compare_List[2]}.png'))
        Details1 = Laptop.Show_Details(Compare_List[0])
        Details2 = Laptop.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.RAM_Label.setText(_translate('Dialog', Details1[1]))
        self.Storage_Label.setText(_translate('Dialog', Details1[2]))
        self.CPU_Label.setText(_translate('Dialog', Details1[3]))
        self.Digikala_Label.setText(_translate('Dialog', Details1[8]))
        self.Techon_Life.setText(_translate('Dialog', Details1[9]))
        self.MeghdadIT_Label.setText(_translate('Dialog', Details1[10]))
        self.Name_Label_2.setText(_translate('Dialog', Details2[0]))
        self.RAM_Label_2.setText(_translate('Dialog', Details2[1]))
        self.Storage_Label_2.setText(_translate('Dialog', Details2[2]))
        self.CPU_Label_2.setText(_translate('Dialog', Details2[3]))
        self.Digikala_Label_2.setText(_translate('Dialog', Details2[8]))
        self.Techon_Life_2.setText(_translate('Dialog', Details2[9]))
        self.MeghdadIT_Label_2.setText(_translate('Dialog', Details2[10]))
        
    def GoToEachCategoryPage(self):
        global Compare_List
        Compare_list = []
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
# TV Compare Page
class TVComparePage(QDialog):
    def __init__(self):
        super(TVComparePage, self).__init__()
        loadUi("Final Presentatiosn/TVComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/TVImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/TVImage{Compare_List[2]}.png'))
        Details1 = TV.Show_Details(Compare_List[0])
        Details2 = TV.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.Size_Label.setText(_translate('Dialog', Details1[1]))
        self.Resolution_Label.setText(_translate('Dialog', Details1[2]))
        self.Quality_Label.setText(_translate('Dialog', Details1[3]))
        self.ScreenTech_Label.setText(_translate('Dialog', Details1[4]))
        self.DigiKala_Label.setText(_translate('Dialog', Details1[5]))
        self.HyperKhanegi_Label.setText(_translate('Dialog', Details1[6]))
        self.TechnoLife_Label.setText(_translate('Dialog', Details1[7]))
        self.Name_Label1_2.setText(_translate('Dialog', Details2[0]))
        self.Size_Label_2.setText(_translate('Dialog', Details2[1]))
        self.Resolution_Label_2.setText(_translate('Dialog', Details2[2]))
        self.Quality_Label_2.setText(_translate('Dialog', Details2[3]))
        self.ScreenTech_Label_2.setText(_translate('Dialog', Details2[4]))
        self.DigiKala_Label_2.setText(_translate('Dialog', Details2[5]))
        self.HyperKhanegi_Label_2.setText(_translate('Dialog', Details2[6]))
        self.TechnoLife_Label_2.setText(_translate('Dialog', Details2[7]))
        
    def GoToEachCategoryPage(self):
        global Compare_List
        Compare_List = []
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
# USB Compare Page
class USBComparePage(QDialog):
    def __init__(self):
        super(USBComparePage, self).__init__()
        loadUi("Final Presentatiosn/USBComparePageFinal.ui", self)
        self.BackButton.clicked.connect(self.GoToEachCategoryPage)
        _translate = QtCore.QCoreApplication.translate
        self.Image1.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/USBImage{Compare_List[0]}.png'))
        self.Image2.setPixmap(QtGui.QPixmap(f'Final Presentatiosn/Images/USBImage{Compare_List[2]}.png'))
        Details1 = USB.Show_Details(Compare_List[0])
        Details2 = USB.Show_Details(Compare_List[2])
        self.Name_Label.setText(_translate('Dialog', Details1[0]))
        self.Storage_label.setText(_translate('Dialog', Details1[1]))
        self.Speed_Label.setText(_translate('Dialog', Details1[2]))
        self.Weight_Label.setText(_translate('Dialog', Details1[3]))
        self.DigiKala_Label.setText(_translate('Dialog', Details1[4]))
        self.MeghdadITLabel.setText(_translate('Dialog', Details1[5]))
        self.TechnoSun_Label.setText(_translate('Dialog', Details1[6]))
        self.Name_Label_2.setText(_translate('Dialog', Details2[0]))
        self.Storage_label_2.setText(_translate('Dialog', Details2[1]))
        self.Speed_Label_2.setText(_translate('Dialog', Details2[2]))
        self.Weight_Label_2.setText(_translate('Dialog', Details2[3]))
        self.DigiKala_Label_2.setText(_translate('Dialog', Details2[4]))
        self.MeghdadITLabel_2.setText(_translate('Dialog', Details2[5]))
        self.TechnoSun_Label_2.setText(_translate('Dialog', Details2[6]))
    
    def GoToEachCategoryPage(self):
        global Compare_List
        Compare_List = []
        each_category_page = EachCategoryPage()
        widget.addWidget(each_category_page)
        widget.setCurrentIndex(widget.currentIndex()+1)    
    
    


        
# a function for reading csv files   
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
