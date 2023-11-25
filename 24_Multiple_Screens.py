# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Defining multiple classes
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('24_Multiple_Screens.kv')

class Myapp(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    Myapp().run()