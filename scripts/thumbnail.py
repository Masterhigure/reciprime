import manim as m

class Thumbnail(m.Scene):
    def construct(self):
        t = m.MathTex(r"\sum_{p\textrm{ prime}}\frac 1p \to \infty", font_size=144).rotate(0.2)

        self.play(m.Write(t))
        self.wait()
