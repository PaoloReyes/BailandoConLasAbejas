from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

from scenes.scene1 import Scene1

class MainScene(VoiceoverScene):
    def setup(self):
        self.scenes = [Scene1]
        self.set_speech_service(CoquiService(model_name='tts_models/es/css10/vits', transcription_model='base', gpu=True))

    def construct(self):
        if not self.scenes: raise Exception("No scenes to render")
        
        for scene in self.scenes:
            scene(self).construct()

if __name__ == "__main__":
    MainScene().render()