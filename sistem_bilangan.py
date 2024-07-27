from manim import *


class SistemBilangan(Scene):
    def construct(self):
        # JUDUL

        def renderJudul(self):
            title_sistem_bilangan = Text(
                "Sistem Bilangan", font_size=72, color=YELLOW)
            self.play(Write(title_sistem_bilangan))
            title_sistem_bilangan_target = title_sistem_bilangan.copy().scale(0.5).to_corner(UL)
            self.play(Transform(title_sistem_bilangan,
                                title_sistem_bilangan_target))

            return title_sistem_bilangan

        def renderPenjelasan(self, judul):
            title_radix = Text("Radix", font_size=36)
            desc_radix = Text(
                "Jumlah lambang yang menjadi dasar dalam suatu sistem bilangan.", font_size=24).next_to(title_radix, DOWN)

            self.play(Write(title_radix))
            self.play(FadeIn(desc_radix))

            radix_title_target = title_radix.copy().next_to(judul, DOWN).to_edge(LEFT)
            radix_description_target = desc_radix.copy().next_to(
                radix_title_target, DOWN).to_edge(LEFT)
            self.play(Transform(title_radix, radix_title_target), Transform(
                desc_radix, radix_description_target))

            radix_title_and_desc = VGroup(title_radix, desc_radix)

            self.play(radix_title_and_desc.animate.fade(0.8))

            return radix_title_and_desc

        def radix_box(radix):
            square = Rectangle(width=0.6, height=0.6, color=WHITE)
            text = Text(f"{radix}", font_size=36, color=WHITE)
            text.move_to(square.get_center())
            return VGroup(square, text)

        def renderRadix(self, title, number_of_radix, element_before):
            title = Text(f"Radix {title}", font_size=36)

            self.play(Write(title))

            radix = []
            for i in range(number_of_radix):
                radix.append(radix_box(i))

            radix_group = VGroup(*radix).arrange(RIGHT,
                                                 buff=0.5).next_to(title, DOWN)

            for i in range(number_of_radix):
                self.play(FadeIn(radix[i]))

            title_target = title.copy().next_to(element_before, DOWN).to_edge(LEFT)
            radix_group_target = radix_group.copy().next_to(
                title_target, DOWN).to_edge(LEFT)

            self.play(Transform(title, title_target), Transform(
                radix_group, radix_group_target))

            group = VGroup(title, radix_group)

            self.play(group.animate.fade(0.8))

            return group

        judul = renderJudul(self)
        radix_description = renderPenjelasan(self, judul)
        radix_2 = renderRadix(self, "Biner", 2, radix_description)
        radix_8 = renderRadix(self, "Oktal", 8, radix_2)
        radix_10 = renderRadix(self, "Desimal", 10, radix_8)
        radix_16 = renderRadix(self, "Heksadesimal", 16, radix_10)

        self.wait(3)
