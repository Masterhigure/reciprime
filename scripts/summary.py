import manim as m
from background import add_background

class Summary(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex(r"\undeline{Conclusion)", font_size=70)
        title.to_edge(m.UP)
        cdict = m.MathTex(r"2^{2k+4} < 2^{2k+4}")

        self.play(m.Write(title), m.Write(cdict))
