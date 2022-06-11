import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign='right', font_size=55, input_filter='float')
        main_layout.add_widget(self.solution)

        buttons = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "*"],
            [".", "0", "C", "/"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_soluction)
        #equals_button.bind(on_press=self.on_soluction)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""
        else:
            if self.solution.text == "Error":
                self.solution.text = ""
                self.solution.text += instance.text
            else:
                self.solution.text += instance.text

    def on_soluction(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"

    # def clear_error(self, instance):
    #     if self.solution == "Error":
    #         if instance == "1":
    #             self.solution.text = ""
    #             self.solution.text += instance.text




if __name__ == '__main__':
    MainApp().run()