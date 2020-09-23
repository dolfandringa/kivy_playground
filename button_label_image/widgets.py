from pathlib import Path

from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

ICON = Path(__file__).parent.resolve() / 'caret-down-solid.png'


class MyWidget(StackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_y = None
        self.height = '32dp'
        self.button = Button()
        button_layout = StackLayout()
        self.button.add_widget(button_layout)
        label1 = Label(text="[color=000000]text1[/color]",
                       markup=True)

        icon = Image(source=str(ICON), size=(16, 16))
        button_layout.add_widget(label1)
        button_layout.add_widget(icon)
        self.add_widget(self.button)
