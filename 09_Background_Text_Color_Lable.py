import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('09_Background_Text_Color_Lable.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
