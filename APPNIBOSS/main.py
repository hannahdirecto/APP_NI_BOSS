from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 650)

class MagigingLayout(BoxLayout):
    pass

class AppNiBoss(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("App_ni_Boss.kv")

if __name__ == "__main__":
    AppNiBoss().run()