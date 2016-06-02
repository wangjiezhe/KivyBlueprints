from kivy.app import App
from kivy.uix.widget import Widget


class CanvasWidget(Widget):
    pass


class PaintApp(App):

    def build(self):
        return CanvasWidget()


def main():
    PaintApp().run()


if __name__ == '__main__':
    main()
