import manim as m
from background import add_background

class Summary(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex(r"\underline{Conclusion}", font_size=70)
        title.to_edge(m.UP)
        cdict = m.MathTex(r"2^{2k+4} < 2^{2k+4}")
        self.add(title, cdict)
        self.play(cdict.animate.scale(2))
        self.play(m.Circumscribe(cdict, time_width=2, run_time=2, buff=0.5))
        self.wait(10)
        ass = m.MathTex(r"\sum_{p\textrm{ prime}}\frac1p < \infty").next_to(cdict, m.DOWN, buff=0.75)
        self.play(m.Write(ass))
        self.wait(3)
        l1 = m.Line(ass.get_corner(m.UP + m.LEFT), ass.get_corner(m.DOWN + m.RIGHT), color=m.PURE_RED, stroke_width=7)
        l2 = m.Line(ass.get_corner(m.UP+ m.RIGHT), ass.get_corner(m.DOWN + m.LEFT), color=m.PURE_RED, stroke_width=7)
        self.play(m.Create(m.VGroup(l1, l2)))

        self.wait(3)
        erdos = m.ImageMobject("media/images/Erdos.jpg").shift(5*m.LEFT + 2*m.UP).rotate(0.5)
        self.play(m.FadeIn(erdos))
        self.wait(6)

        book = m.ImageMobject("media/images/book.jpg").scale(0.5).shift(4.5*m.RIGHT + 1.7*m.DOWN).rotate(-0.5)
        self.play(m.FadeIn(book))
        self.wait(10)
