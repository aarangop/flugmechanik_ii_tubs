from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.rotate(PI / 6)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
