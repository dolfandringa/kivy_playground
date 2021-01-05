"""Defines a selectbox widget"""
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.stacklayout import MDStackLayout

Builder.load_string("""
<SelectBox>
    adaptive_height: True
    dd_item: drop_item
    MDDropDownItem:
        id: drop_item
        color: app.theme_cls.primary_color
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: self.parent.label
""")


class SelectBox(MDStackLayout):
    """An html style select box"""
    label = StringProperty('Select an option')
    value = StringProperty()
    options = ListProperty()
    dd_item = ObjectProperty()
    dropdown = None

    def on_dd_item(self, _instance, item):
        """Runs after setting the MDDropDownItem"""
        app = MDApp.get_running_app()
        print(f"Theme class {app.theme_cls.primary_color}")
        self.dropdown = MDDropdownMenu(
            caller=item,
            items=self.options,
            position="auto",
            width_mult=4,
            callback=self.select_option,
        )
        item.bind(on_release=self.open_dropdown)

    def open_dropdown(self, *_args, **_kwargs):
        """Open the dropdown."""
        self.dropdown.open()

    def on_options(self, _instance, options):
        """Change the selectbox items."""

        if self.dropdown is not None:
            self.dropdown.items = options
            self.dropdown.create_menu_items()

    def on_label(self, _instance, value):
        """When the selectbox label changes, change the button text"""
        self.dd_item.text = value

    def select_option(self, option):
        """Selected the option of the SelectBox"""
        self.dropdown.dismiss()
        self.dd_item.set_item(option.text)
        self.value = option.text
