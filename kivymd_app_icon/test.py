from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'window_icon', '/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg')
Config.write()
Window.set_icon('/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg')


class MyTestApp(MDApp):
    def build(self):
        self.title = "MyTestApp"
        self.icon = '/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg'

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )

        return screen


MyTestApp().run()
