from manim import *


class WriteExtendByte(Scene):
    def construct(self):
        text = Text("ExtendByte", font_size=114)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))
        self.wait(1)
