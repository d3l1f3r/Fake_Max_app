from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

class Max(App):
    def build(self):
        content = GridLayout(cols=1, padding=10, spacing=10)
        label = Label(text='Приложение не может быть запущено.\n Error code: 0JzQsNC60YEg0LjQtNC4INC90LDRhdGD0Lk=',valign='middle',halign='center')
        close_btn = Button(text='Закрыть', size_hint_y=None, height=100)

        content.add_widget(label)
        content.add_widget(close_btn) 
        
        self.popup = Popup(
            title='Fatal Error',
            content=content,
            size_hint=(0.8, 0.6),
            auto_dismiss=True
        )

        close_btn.bind(on_press=self.crash_app)
        self.popup.open()

        return Label(text='') # This asshole must to return something
    
    def crash_app(self, instance):
        self.popup.dismiss()
        Clock.schedule_once(self.do_crash, 0.25)

    def do_crash(self, dt=None):
        1 / 0 # do impossible things, yeaaahhhhhh

if __name__ == '__main__':
    Max().run()
