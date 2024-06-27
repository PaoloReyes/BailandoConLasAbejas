import typing as t
from typing import Callable, Generator
from contextlib import contextmanager

from manim.mobject.mobject import Mobject
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.base import SpeechService
from manim_voiceover.tracker import VoiceoverTracker

class SubScene(VoiceoverScene):
    def __init__(self, main_scene = None):
        super().__init__()
        
        if main_scene is None: raise Exception('SubScene must be initialized with a main_scene')
        self.main_scene = main_scene

    def play(self, *args, subcaption=None, subcaption_duration=None, subcaption_offset=0, **kwargs):
        self.main_scene.play(*args, subcaption=subcaption, subcaption_duration=subcaption_duration, subcaption_offset=subcaption_offset, **kwargs)

    def add(self, *mobjects: Mobject):
        self.main_scene.add(*mobjects)

    def wait(self, duration: float = ..., stop_condition: Callable[[], bool] | None = None, frozen_frame: bool | None = None):
        self.main_scene.wait(duration, stop_condition, frozen_frame)

    def wait_until_bookmark(self, mark: str) -> None:
        self.main_scene.wait_until_bookmark(mark)

    def set_speech_service(self, speech_service: SpeechService, create_subcaption: bool = True) -> None:
        self.main_scene.set_speech_service(speech_service, create_subcaption)

    @contextmanager
    def voiceover(self, text: t.Optional[str] = None, ssml: t.Optional[str] = None, **kwargs) -> Generator[VoiceoverTracker, None, None]:
        if text is None and ssml is None:
            raise ValueError("Please specify either a voiceover text or SSML string.")

        try:
            if text is not None:
                yield self.main_scene.add_voiceover_text(text, **kwargs)
            elif ssml is not None:
                yield self.main_scene.add_voiceover_ssml(ssml, **kwargs)
        finally:
            self.main_scene.wait_for_voiceover()

    def get_mobjects(self) -> list:
        return self.main_scene.mobjects