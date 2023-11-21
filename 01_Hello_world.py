# Author    :   Lila

import kivy
from kivy.app import App 
from kivy.uix.label import Label

class Myapp(App):
    def build(self):
        # Return text
        return Label(text="Hello world",font_size = 65)
    
if __name__ == '__main__':
    Myapp().run()