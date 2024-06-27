from manim import *

import manim_ml
from manim_ml.utils.colorschemes.colorschemes import ColorScheme
manim_ml.config.color_scheme = ColorScheme(
                                    primary_color=BLUE,
                                    secondary_color=BLACK,
                                    active_color=RED,
                                    text_color=BLACK,
                                    background_color=WHITE
                                )

from manim_ml.neural_network import FeedForwardLayer, NeuralNetwork

from utils.subscene import SubScene

class Scene2(SubScene):
    def construct(self):

        # Fully Connected Neural Network Creation
        nn = NeuralNetwork([
                            FeedForwardLayer(3), 
                            FeedForwardLayer(5),
                            FeedForwardLayer(3),
                            FeedForwardLayer(7),
                            FeedForwardLayer(1)
                            ], layer_spacing=0.3, edge_width=4.0)
        nn.scale(2.5)
        
        with self.voiceover('Una mejor y más moderna solución <bookmark mark="fade_prev_scene"/> es usar redes neuronales. <bookmark mark="nn"/>'
                            'Comenzaremos tratando de identificar si hay o no una abeja en una imagen.') as tracker:
            if len(self.get_mobjects()): self.play(*[FadeOut(mobject) for mobject in self.get_mobjects()], run_time=tracker.time_until_bookmark('fade_prev_scene'))

            self.play(Create(nn), run_time=tracker.time_until_bookmark('nn'))
            self.play(nn.make_forward_pass_animation(), run_time=tracker.get_remaining_duration())
            