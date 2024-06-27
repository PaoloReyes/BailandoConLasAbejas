from manim import *

from utils.subscene import SubScene

class Scene2(SubScene):
    def construct(self):
        self.title = Square()

        self.play(*[FadeOut(mobject) for mobject in self.get_mobjects()], run_time=2)