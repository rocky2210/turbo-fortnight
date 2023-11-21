# Author    :   Lila

import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.image import Image

Builder.load_file('11_Images.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
