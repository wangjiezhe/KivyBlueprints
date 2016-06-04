from kivy.app import App
from kivy.uix.widget import Widget
from kivy.base import EventLoop
from kivy.utils import get_color_from_hex
from kivy.config import Config
from kivy.graphics import Color, Line


CURSOR = (
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '@@@@@@ @@@@ @@@@@@      ',
    '@----@ @--@ @----@      ',
    '@----@ @--@ @----@      ',
    '@@@@@@ @@@@ @@@@@@      ',
    '                        ',
    '       @@@@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @--@             ',
    '       @@@@             ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
    '                        ',
)


class CanvasWidget(Widget):

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            Color(*get_color_from_hex('#0080FF80'))
            Line(circle=(touch.x, touch.y, 25), width=4)

    def clear_canvas(self):
        # self.canvas.clear()
        # self.canvas.children = [widget.canvas for widget in self.children]
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)


class PaintApp(App):

    def build(self):
        EventLoop.ensure_window()
        if EventLoop.window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse
                from pygame import cursors
                a, b = cursors.compile(CURSOR, black='@', white='-')
                mouse.set_cursor((24, 24), (9, 9), a, b)
            except:
                pass
        return CanvasWidget()


def main():
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    # Config.set('graphics', 'resizable', '0')
    # Config.set('input', 'mouse', 'mouse,disable_multitouch')

    from kivy.core.window import Window

    Window.clearcolor = get_color_from_hex('#FFFFFF')

    PaintApp().run()


if __name__ == '__main__':
    main()
