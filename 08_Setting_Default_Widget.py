# Author    :   Lila

import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('08_Setting_Default_Widget.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
