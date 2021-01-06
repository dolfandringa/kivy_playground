from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.utils import platform

if platform == 'linux':
    from Xlib.display import Display
    from Xlib import X

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
        self.icon = '/usr/share/icons/hicolor/apps/48x48/apps/idle3.png'
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

    def set_wm_class(self):
        """
        Set the X11 WM_CLASS. This is used to link the window to the X11
        application (menu entry from the .desktop file). Gnome-shell won't
        display the application icon correctly in the dash with the default
        value of `python3, python3`.
        """
        display = Display()
        root = display.screen().root
        windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value
        for windowID in windowIDs:
            window = display.create_resource_object('window', windowID)
            title = window.get_wm_name()
            if title == self.title:
                window.set_wm_class("MyKivyTestApp", "python3")
                display.sync()

    def on_start(self):
        if platform == 'linux':
        #    pass
             self.set_wm_class()



MyKivyTestApp().run()
