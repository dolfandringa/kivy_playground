"""Defines a selectbox widget"""
from pathlib import Path

from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.menu import MDDropdownMenu

ASSET_DIR = (Path(__file__).parent/'..').resolve()/'assets'


Builder.load_string("""
<SelectBox>
    height: '32dp'
    size_hint_y: None
    dd_item: drop_item
    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: self.parent.label
        on_release: self.parent.dropdown.open()
""")


class SelectBox(StackLayout):
    """An html style select box"""
    label = StringProperty('Select an option')
    value = StringProperty()
    options = ListProperty()
    dd_item = ObjectProperty()
    dropdown = None

    def on_dd_item(self, _instance, _item):
        """Runs after setting the MDDropDownItem"""
        print(f"On dd_item, options: {self.options}")
        self.dropdown = MDDropdownMenu(
            caller=self.dd_item,
            items=self.options,
            position="auto",
            width_mult=4
        )
        self.dropdown.bind(on_release=self.select_option)

    def on_options(self, _instance, options):
        """Change the selectbox items."""
        print("On options")

        if self.dropdown is not None:
            self.dropdown.items = options

    def on_label(self, _instance, value):
        """When the selectbox label changes, change the button text"""
        print("Label changed")
        self.dd_item.text = value

    def select_option(self, dropdown, option):
        """Selected the option of the SelectBox"""
        print("Selected the value")
        dropdown.dismiss()
        self.dd_item.set_item(option.text)
