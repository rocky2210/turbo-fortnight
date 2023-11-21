import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Builder.load_file('10_Background_Color.kv')

class MyLayout(Widget):
    pass

class Myapp(App):
    def build(self):
        Window.clearcolor = (1,0,1,1) # Second way to use color but less priority
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
