# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('21_Checkboxes.kv')

class MyLayout(Widget):
    checks = []
    def checkbox_click(self, instance, value,food):
        # print(value)
        if value == True:
            MyLayout.checks.append(food)
            foods = ''
            for x in MyLayout.checks:
                foods = f'{foods} {x}'
                print(foods)
            self.ids.output_label.text = f'you selected {foods}'
        else:
            MyLayout.checks.remove(food)
            foods = ''
            for x in MyLayout.checks:
                foods = f'{foods} {x}'
            self.ids.output_label.text = f'you selected {foods}'

class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()