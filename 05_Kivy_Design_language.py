import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('05_Kivy_Design_language.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    food = ObjectProperty(None)
    anime = ObjectProperty(None)

    def press(self):
        name = self.name.text
        food = self.food.text
        anime = self.anime.text

        print(f"hello {name}, you like {food} food , and your favorite anime is {anime}")
        # self.add_widget(Label(text=f"hello {name}, you like {food} food , and your favorite anime is {anime}"))

        # Clear the input boxes
        self.name.text = ""
        self.food.text = ""
        self.anime.text = ""

class Myapp(App):
    def build(self):
        # Return text
        return MyGridLayout()
    
if __name__ == '__main__':
    Myapp().run()
