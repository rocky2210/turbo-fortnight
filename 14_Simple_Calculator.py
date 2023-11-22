# Author    :   Lila

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Setting app size
Window.size = (400,600)

Builder.load_file('14_Simple_Calculator.kv')

class MyLayout(Widget):
    
    # Clearing function
    def clear(self):
        self.ids.calc_input.text = '0'

    # Creating a button pressing function
    def button_press(self, button):
        # Creating a variable that contains whatever in the text box
        prior = self.ids.calc_input.text

        # Test for error 
        if "Error" in prior:
            prior =''

        # Determining if 0 is there
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Creating decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split out text box by +
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # Creating function to remove last character
    def remove(self):
        prior = self.ids.calc_input.text
        # Removing last item in the textbox
        prior = prior[:-1]
        # Text box output
        self.ids.calc_input.text = prior

    # Creating function for postive and negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'


    # Creating sign function
    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        #  a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # Creating equal to function
    def equal(self):
        prior = self.ids.calc_input.text
        
        #Error handling for divisible by zero
        try:
            # Evaluate the math from the text box
            answer = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = str("Error")
        '''
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            # print(num_list)
            answer = 0.0
            # Looping through this num_list
            for number in num_list:
                answer = answer + float(number)
            
            # print(answer)
            # Printing answer
            self.ids.calc_input.text = str(answer)
        '''

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()