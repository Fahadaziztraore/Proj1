from kivy.app import App
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # Crée une étiquette avec le texte "Bonjour, Kivy!"
        label = Label(text="Bonjour, Kivy!")
        return label

if __name__ == '__main__':
    SimpleApp().run()
