from kivy.app import App
from kivy.uix.label import Label

class Max(App):
    def build(self):
        return Label(text='Loading...')


if __name__ == '__main__':
    Max().run()
