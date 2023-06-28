'''
This is First Version of the Project That It's just the front of Project
And Just its Homepage
'''

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


kv = Builder.load_file('Versions/Version1/my.kv')

class HomePage(Screen):
    LoggedIn = True

class MenuPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass

sm = WindowManager()

screens = [HomePage(name= "HomePage"), MenuPage(name= "MenuPage")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "MenuPage"

class MyApp(App):
    def build(self):
        return sm
    

if __name__ == '__main__':
    MyApp().run()