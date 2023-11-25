# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('28_Images_As_Buttons.kv')

class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_image.source = 'assets/login_press.png'

    def hello_off(self):
        self.ids.my_image.source = 'assets/login.png'
        self.ids.my_label.text = "You pressed the button"


class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()