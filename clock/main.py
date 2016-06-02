from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex('#101216')

LabelBase.register(
    name='Roboto',
    fn_regular='fonts/Roboto-Thin.ttf',
    fn_bold='fonts/Roboto-Medium.ttf'
)


class ClockApp(App):
    pass


if __name__ == '__main__':
    ClockApp().run()
