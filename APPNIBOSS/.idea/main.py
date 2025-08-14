from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.animation import Animation

# Try import with fallback
try:
    from kivymd.uix.list.items import OneLineListItem
except ImportError:
    from kivymd.uix.list import OneLineListItem

Window.size = (400, 650)

class MagigingLayout(BoxLayout):
    pass

class AppNiBoss(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        root = Builder.load_file("App_ni_Boss.kv")
        self.load_recommendations(root)
        return root

    def say_hi(self):
        print("Hi there!")

    def filter_items(self, text):
        item_list = self.root.ids.item_list
        welcome_card = self.root.ids.welcome_card

        if text.strip():
            Animation(opacity=0, d=0.3).start(welcome_card)
        else:
            Animation(opacity=1, d=0.3).start(welcome_card)

        item_list.clear_widgets()

        menu_items = ["Mami Special", "Mami Beef", "Mami Chicken", "Lomi", "Pancit Canton"]

        for item in menu_items:
            if text.lower() in item.lower():
                item_list.add_widget(OneLineListItem(text=item))

    def load_recommendations(self, root):
        recommendation_box = root.ids.recommendation_box

        recommendations = [
            "https://via.placeholder.com/120x120.png?text=Mami",
            "https://via.placeholder.com/120x120.png?text=Lomi",
            "https://via.placeholder.com/120x120.png?text=Canton"
        ]

        for url in recommendations:
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("120dp", "120dp"),
                padding=5,
                radius=[12],
                md_bg_color=(1, 1, 1, 0.1),
                elevation=4
            )
            image = Image(
                source=url,
                allow_stretch=True,
                keep_ratio=False
            )
            card.add_widget(image)
            recommendation_box.add_widget(card)

if __name__ == "__main__":
    AppNiBoss().run()
