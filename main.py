from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.toolbar import MDTopAppBar

class NeDoTaxiApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        Screen = MDScreen()

        bar = MDTopAppBar()
        bar.title = "APP"

        bar.pos_hint = {"center_x":0.5,"top":1}

        print(bar.get_top())

        button = MDRectangleFlatButton()
        button.pos_hint = {"center_x":0.5,"center_y":0.5}

        Screen.add_widget(button)
        Screen.add_widget(bar)
        return Screen


if __name__ == '__main__':
    NeDoTaxiApp().run()