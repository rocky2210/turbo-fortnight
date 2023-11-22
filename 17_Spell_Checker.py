# Author    :   Lila

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling

Builder.load_file('17_Spell_Checker.kv')

class MyLayout(Widget):
    def press(self):
        # Creating instance of spelling
        s = Spelling()
        # Select the language
        s.select_language('en_US')
        # See the language options
        # print(s.list_languages())

        # Grabing the word from the textbox
        word = self.ids.word_input.text

        option = s.suggest(word)
        x = ''
        for item in option:
            x = f'{x} {item}'
        # Updating the label
        self.ids.word_label.text = f'{option}'



class Myapp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    Myapp().run()