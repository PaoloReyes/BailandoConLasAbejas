from manim import *

from utils.subscene import SubScene

class Scene1(SubScene):
    def construct(self):
        # Showing the raw bee image
        raw_bee = ImageMobject('assets/scene1/raw_bee.webp')
        raw_bee.z_index = 10

        with self.voiceover('El primer intento para <bookmark mark="wait_time"/> tratar de identificar algun elemento'
                            'en una imagen es a traves del uso de visión computacional tradicional.') as tracker:
            self.wait_until_bookmark('wait_time')
            self.play(FadeIn(raw_bee), 
                      run_time=tracker.get_remaining_duration())

        # Showing the segmentated bee image
        just_bee = ImageMobject('assets/scene1/just_bee.jpg')

        with self.voiceover('En este caso, se tiene una imagen de una abeja y se desea excluirla del fondo.') as tracker:
            self.play(FadeOut(raw_bee), 
                      FadeIn(just_bee), 
                      run_time=tracker.duration)

        # Going back to the raw bee image
        with self.voiceover('Para ello, se pueden aplicar diferentes técnicas, una de ellas la aplicación de máscaras de color.') as tracker:
            self.play(FadeOut(just_bee), 
                      FadeIn(raw_bee), 
                      run_time=tracker.duration)

        # Showing the yellow mask
        yellow_mask = ImageMobject('assets/scene1/yellow_mask.png').shift(3.5*LEFT).scale(0.3)
        yellow_mask.z_index = 20

        yellow_mask_arrow = Arrow(color=YELLOW, buff=0.1, max_tip_length_to_length_ratio=0.15)
        yellow_mask_arrow.z_index = -1
        yellow_mask_arrow.add_updater(lambda m: m.put_start_and_end_on(raw_bee.get_right(), yellow_mask.get_left()))

        with self.voiceover('Por ejemplo, <bookmark mark="wait_time"/> tomemos la imagen y extraigamos solo un rango de pixeles amarillos') as tracker:
            self.play(raw_bee.animate.shift(3.5*LEFT).scale(0.3), run_time=tracker.time_until_bookmark('wait_time'))
            self.add(yellow_mask, yellow_mask_arrow)
            self.play(yellow_mask.animate.shift(7*RIGHT), run_time=tracker.get_remaining_duration())

        # Showing the black, white and wings masks
        black_mask = ImageMobject('assets/scene1/black_mask.png').shift(3.5*RIGHT+0.75*UP).scale(0.3)
        white_mask = ImageMobject('assets/scene1/white_mask.png').shift(3.5*RIGHT+0.75*DOWN).scale(0.3)
        wings_mask = ImageMobject('assets/scene1/wings_mask.png').shift(3.5*RIGHT+2.25*DOWN).scale(0.3)

        yellow_mask.z_index = 0
        black_mask_arrow = Arrow(color=BLACK, buff=0.1, max_tip_length_to_length_ratio=0.15).put_start_and_end_on(raw_bee.get_right(), black_mask.get_left())
        white_mask_arrow = Arrow(color=GRAY, buff=0.1, max_tip_length_to_length_ratio=0.15).put_start_and_end_on(raw_bee.get_right(), white_mask.get_left())
        wings_mask_arrow = Arrow(color=PURPLE, buff=0.1, max_tip_length_to_length_ratio=0.15).put_start_and_end_on(raw_bee.get_right(), wings_mask.get_left())

        with self.voiceover('Y hagamos lo mismo para pixeles negros, blancos y algunos tonos transparentes para las alas.') as tracker:
            self.play(yellow_mask.animate.shift(2.25*UP), 
                      FadeIn(black_mask), 
                      FadeIn(white_mask), 
                      FadeIn(wings_mask),
                      GrowArrow(black_mask_arrow), 
                      GrowArrow(white_mask_arrow), 
                      GrowArrow(wings_mask_arrow), 
                      run_time=tracker.duration)
            
        # Merging the masks into one
        masks = Group(yellow_mask, black_mask, white_mask, wings_mask)
        arrows = VGroup(yellow_mask_arrow, black_mask_arrow, white_mask_arrow, wings_mask_arrow)
        for mask_idx, arrow in enumerate(arrows):
            if mask_idx == 0: continue
            arrow.add_updater(lambda m, i=mask_idx: m.put_start_and_end_on(raw_bee.get_right(), masks[i].get_left()))

        with self.voiceover('Si mezclamos todas estas máscaras en una sola obtendremos los pixeles '
                            'que contienen colores que generalmente pertencen a una abeja.') as tracker:
            self.play(*[mask.animate.move_to(3.5*RIGHT).scale(0.5/0.3) for mask in masks], 
                      raw_bee.animate.scale(0.5/0.3), 
                      FadeOut(arrows), 
                      run_time=tracker.duration)
            
        self.wait(0.5)

        # Superposing the masks to the image
        non_removed_green = ImageMobject('assets/scene1/non_removed_green.jpg')
        raw_bee.z_index = -1
        
        with self.voiceover('Y si usamos esta máscara para extraer los pixeles de la imagen original obtendremos a nuestra <bookmark mark="wait_for_fusion"/>'
                            'abeja completamente separada del fondo. O algo así...') as tracker:
            self.play(raw_bee.animate.move_to(ORIGIN).scale(1.0/0.5), 
                      masks.animate.move_to(ORIGIN).scale(1.0/0.5), 
                      run_time=tracker.time_until_bookmark('wait_for_fusion'))
            self.play(FadeOut(raw_bee), 
                      FadeOut(masks), 
                      FadeIn(non_removed_green),
                      run_time=tracker.get_remaining_duration())

        # Explaining the problem with this approach
        pointing_arrow = Arrow(color=RED, start=2.0*RIGHT, end=1.0*DOWN, buff=0.1)

        with self.voiceover('Podemos ver que segmentamos correctamente a la abeja <bookmark mark="segmentation"/>, ' 
                            'pero aun hay gran cantidad de pixeles de la hoja en la que estaba parada.') as tracker:
            self.play(GrowArrow(pointing_arrow), run_time=tracker.time_until_bookmark('segmentation'))
            self.play(pointing_arrow.animate.shift(5.0*RIGHT+2.0*DOWN), run_time=tracker.get_remaining_duration()*0.75)
            self.play(FadeOut(pointing_arrow), run_time=tracker.get_remaining_duration())

        # Substracting the green pixels
        green_mask = ImageMobject('assets/scene1/green_mask.png')

        with self.voiceover('Es posible mejorar nuestra segmentación añadiendo una máscara de pixeles verdes <bookmark mark="green_pixels"/>, '
                            'y substrayendola de la imagen. <bookmark mark="subtracting_mask"/> De esta forma tendremos una segmentación más limpia; '
                            'Aunque no perfecta.') as tracker:
            self.play(FadeIn(green_mask), run_time=tracker.time_until_bookmark('green_pixels'))
            self.play(FadeOut(green_mask), FadeOut(non_removed_green), FadeIn(just_bee), run_time=tracker.time_until_bookmark('subtracting_mask'))

        # Why this is not a good approach
        complex_image = ImageMobject('assets/scene1/complex_image.webp').scale(1.25)
        masked_complex_image = ImageMobject('assets/scene1/masked_complex_image.jpg').scale(1.25)

        with self.voiceover('Este método es efectivo en casos sencillos <bookmark mark="waiting_for_complex_image"/>, pero en imágenes más complejas, '
                            'como la que estamos viendo <bookmark mark="complex_image"/>, aplicar las mismas máscaras nos lleva a un muy mal resultado '
                            '<bookmark mark="apply_masks"/> porque el amarillo que debería pertenecer solo a las abejas, ahora está tambien en el fondo.') as tracker:
            self.wait_until_bookmark('waiting_for_complex_image')
            self.play(FadeOut(just_bee), FadeIn(complex_image), run_time=tracker.time_until_bookmark('complex_image'))
            self.play(FadeIn(masked_complex_image), run_time=tracker.time_until_bookmark('apply_masks'))