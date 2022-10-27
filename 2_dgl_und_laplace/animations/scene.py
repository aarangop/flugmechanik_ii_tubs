from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.rotate(PI / 6)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle(fill_color=PINK)
        square = Square(fill_color=BLUE)

        square.next_to(circle, RIGHT, buff=1)

        self.play(Create(circle), Create(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=1))


class AnimationWithSections(Scene):
    def construct(self):
        self.next_section("Section 1")
        circle = Circle()
        self.play(Create(circle))
        self.play(FadeOut(circle))
        self.next_section("Section 2")
        square = Square()
        self.play(Create(square))
        self.play(FadeOut(square))


class AnAxis(Scene):
    def construct(self):
        axes = Axes()
        cos_fn = FunctionGraph(
            lambda t: np.cos(t)
        )
        self.add(axes)
        l1 = Arrow([0, 0, 0], [2, 1.5, 0])
        self.play(Create(l1))
        self.play(Create(cos_fn))
        self.play(cos_fn.animate.move_to(LEFT * 2))
        self.wait(2)


class FuncionLinear(Scene):
    def construct(self):
        axes = Axes()
        lin_fn = FunctionGraph(
            lambda x: 3 / 2 * x + 1
        )
        self.add(axes)
        self.play(Create(lin_fn))
        self.wait(3)


class FederMasse(Scene):
    def construct(self):
        rect = Rectangle(height=2, width=0.5)
        square = Square(side_length=1.5)
        square.next_to(rect, DOWN, buff=0.1)
        numberplane = NumberPlane()
        self.add(numberplane, square, rect)


class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 3, 1],
                    x_length=6, y_length=3,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}
                    ).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label='x', y_label='f(x)')
        self.play(DrawBorderThenFill(axes), Write(axis_labels))

        graph = axes.plot(lambda x: 0.5 * x, x_range=[0, 4])
        graphing_stuff = VGroup(axes, graph, axis_labels)
        self.play(Create(graph))


class SpringBaseScene(Scene):
    def get_spring_system(self, height=1, n_spring_revs=15, mass_radius=0.5, spring_radius=0.2):
        mass_circ = Circle(radius=mass_radius, fill_color=BLUE, stroke_color=BLUE, fill_opacity=1)
        mass_text = MathTex('m')
        mass_text.next_to(mass_circ, LEFT)
        ceil = Line([-mass_radius, height, 0], [mass_radius, height, 0])
        l_spring_step = height / n_spring_revs
        spring_lines = [
            Line([0, 0, 0], [spring_radius, l_spring_step, 0])
        ]
        for i in range(1, n_spring_revs - 1):
            spring_lines.append(Line(spring_lines[-1].get_end(), [
                spring_radius if i % 2 == 0 else -spring_radius, (i + 1) * l_spring_step, 0
            ]))
        spring_lines.append(Line(spring_lines[-1].get_end(), [0, height, 0]))
        spring_gr = VGroup(ceil, *spring_lines)
        mass = VGroup(mass_circ, mass_text)
        return VGroup(mass, spring_gr)

    def construct(self):
        self.next_section('Feder-Masse-(Dämpfer)-Schwinger')
        height = 4
        spring_mass = self.get_spring_system(height=height)
        self.play(FadeIn(spring_mass))
        self.play(spring_mass.animate.shift(LEFT * 2))


class OscilatingSpring(SpringBaseScene):
    def construct(self):
        height = 4
        spring_mass_system = self.get_spring_system(height=4)
        mass = spring_mass_system[0]
        spring = spring_mass_system[1]
        
        self.play(FadeIn(spring_mass_system))

