from kivy.app import App
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget


class DrawCanvasWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class PaintApp(App):
    def build(self):
        self.draw_canvas_widget = DrawCanvasWidget()

        return self.draw_canvas_widget  # 返回root控件

if __name__ == "__main__":
    PaintApp().run()
