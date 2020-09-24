from kivymd.app import MDApp


class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"


if __name__ == '__main__':
    TestApp().run()
