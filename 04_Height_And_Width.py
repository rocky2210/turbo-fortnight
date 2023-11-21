import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Calling grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Setting columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # Creating a second gridlayout
        self.top_grid = GridLayout(
                            row_force_default=True,
                            row_default_height=40,  # Corrected typo in this line
                            col_force_default=True,
                            col_default_width=100)  # Corrected typo in this line
        self.top_grid.cols = 2

        # Adding Widgets
        self.top_grid.add_widget(Label(text="Name : "))
        # Adding input box
        self.name = TextInput(multiline=True) 
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Food : "))
        self.food = TextInput(multiline=False)
        self.top_grid.add_widget(self.food)

        self.top_grid.add_widget(Label(text="Favorite Anime : "))
        self.anime = TextInput(multiline=False)
        self.top_grid.add_widget(self.anime)

        # Adding the new top_grid to our app
        self.add_widget(self.top_grid)
        

        # Creating submit button
        self.submit = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None,  # Corrected typo in this line
                             height=50,
                             size_hint_x=None,
                             width=200)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        food = self.food.text
        anime = self.anime.text

        # print(f"hello {name}, you like {food} food , and your favorite anime is {anime}")
        self.add_widget(Label(text=f"hello {name}, you like {food} food , and your favorite anime is {anime}"))

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
