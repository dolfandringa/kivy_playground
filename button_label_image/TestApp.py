from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


class MyLayout(GridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TestApp(MDApp):
    pass


if __name__ == '__main__':
    TestApp().run()
