# Author    :   Lila

import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('07_Box_Layout.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        # Return text
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
