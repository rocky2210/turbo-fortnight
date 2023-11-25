# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('25_Spinner_Dropdowns.kv')

class MyLayout(Widget):
    def spinner_clicked(self,value):
        self.ids.click_label.text = f'You selected {value}'

class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()