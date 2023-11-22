# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('15_Rounded_Buttons.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()