from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# pip install PyEnchant
from kivy.core.spelling import Spelling

# Loading UG file
Builder.load_file('ug.kv')


class MyLayout(Widget):

    def press(self):
        # create instance of Spelling
        s = Spelling()

        # Select the language
        s.select_language('en_US')

        # See the language options
        # print(s.list_languages())

        # Grab the word from the chatbox
        word = self.ids.word_input.text

        options = s.suggest(word)

        x = ''

        for item in options:
            x = f"{x} {item}"
            # update the label
            self.ids.word_label.text = x


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
