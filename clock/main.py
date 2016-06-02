from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
# from kivy.properties import ObjectProperty
# from kivy.uix.boxlayout import BoxLayout

from time import strftime

LabelBase.register(
    name='Roboto',
    fn_regular='fonts/Roboto-Thin.ttf',
    fn_bold='fonts/Roboto-Medium.ttf'
)


# class ClockLayout(BoxLayout):
#     time_prop = ObjectProperty(None)


class ClockApp(App):

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        # self.root.time_prop.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)


def main():
    Window.clearcolor = get_color_from_hex('#101216')
    ClockApp().run()


if __name__ == '__main__':
    main()
