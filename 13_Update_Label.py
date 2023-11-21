from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.properties import ObjectProperty

Builder.load_file('13_Update_Label.kv')

# Root class
class MyLayout(Widget):
    def press(self):
        # Creating variables for our widget
        name = self.ids.name_input.text
        # print(name)

        # Updating the label
        self.ids.name_label.text = f'Hello {name}'

        # Clearing the text box
        self.ids.name_input.text = ''

class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()
