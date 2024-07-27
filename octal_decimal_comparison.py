from manim import *


class OctalDecimalComparison(Scene):
    def construct(self):
        title = Text("Oktal vs Desimal", font_size=72, color=YELLOW)

        self.play(Write(title))
        self.wait()

        # move with animation the title to left top
        title_target = title.copy().to_corner(UL)
        self.play(Transform(title, title_target))

        # create text objects for "Decimal" and "octal"
        decimal_text = Text("Desimal", font_size=42)
        decimal_number = Text("0", font_size=144, color=WHITE)
        octal_text = Text("Oktal", font_size=42)
        octal_number = Text("0", font_size=144, color=WHITE)

        # position the texts
        octal_text.next_to(title, DOWN).to_edge(RIGHT)
        octal_number.next_to(octal_text, DOWN*2).to_edge(RIGHT)
        decimal_text.next_to(octal_number, DOWN*3).to_edge(RIGHT)
        decimal_number.next_to(decimal_text, DOWN*2).to_edge(RIGHT)

        # display the texts
        self.play(Write(octal_text))
        self.play(Write(octal_number))
        self.play(Write(decimal_text))
        self.play(Write(decimal_number))

        # define the counting range
        start_number = 0
        end_number = 50

        # create an update function to change the text
        def update_text(text_mobject, count):
            text_mobject.become(Text(f"{count}", font_size=144, color=WHITE).move_to(
                text_mobject.get_center()).align_to(text_mobject, RIGHT))

        # animate the counting from start_number to end_number
        for number in range(start_number, end_number + 1):
            self.play(
                UpdateFromFunc(
                    octal_number, lambda t: update_text(t, oct(number)[2:])),
                UpdateFromFunc(
                    decimal_number, lambda t: update_text(t, number)),
                run_time=0.5
            )
