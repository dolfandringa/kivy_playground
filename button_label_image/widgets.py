from pathlib import Path

from kivy.graphics import Color, Line, Rectangle
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

ICON = Path(__file__).parent.resolve() / 'caret-down-solid.png'


class MyWidget(StackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_y = None
        self.height = '32dp'
        self.button = Button(
            text="text1",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1)
        )
        button_layout = RelativeLayout()
        self.add_widget(button_layout)
        button_layout.add_widget(self.button)
        icon = Image(source=str(ICON), size=(16, 16), size_hint=(None, None))
        icon.reload()
        icon.pos_hint = {'center_x': 0.95, 'center_y': 0.5}
        button_layout.add_widget(icon)
