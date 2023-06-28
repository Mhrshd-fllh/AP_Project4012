import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
#from kivy.graphics import Rectangle
#from kivy.graphics import Color
#from kivy.graphics import Line



'''
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
'''
#from kivy.uix.floatlayout import FloatLayout
'''
class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    def btn(self):
        print("Name:", self.name.text, "Email: ", self.email.text)
        self.name.text = ""
        self.email.text = ""
'''
'''
class Touch(Widget):
    #btn = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)        

        with self.canvas:
            Line(points= (30, 20, 150 ,200 , 900 , 100))
            Color(255,0,0, mode='rgb')
            self.rect = Rectangle(pos = (0,0),size=(50,70))
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)
        #self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)

    #def on_touch_up(self, touch):
        #print("Mouse Up", touch)
        #self.btn.opacity = 1
'''
class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Kivy Tutorial/my.kv')

class MyApp(App):
    def build(self):
        return kv
    
    
if __name__ == '__main__':
    MyApp().run()