from kivy.app import App
from kivy.metrics import dp
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'window_icon', '/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg')
Config.write()
Window.set_icon('/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg')


KV = """
Screen:
    canvas:
        Color:
            rgba: 0.9764705882352941, 0.9764705882352941, 0.9764705882352941, 1
        Rectangle:
            pos: self.pos
            size: self.size
"""

class MyKivyTestApp(App):
    def build(self):
        self.title = "MyKivyTestApp"
        self.icon = '/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg'
        screen = Builder.load_string(KV)
        screen.add_widget(
            Button(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size_hint=(None, None),
                size=(dp(110), dp(35)),
            )
        )
        return screen


MyKivyTestApp().run()
