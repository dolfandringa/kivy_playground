from kivymd.app import MDApp
from kivymd.theming import ThemeManager


class TestApp(MDApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"


if __name__ == '__main__':
    TestApp().run()
