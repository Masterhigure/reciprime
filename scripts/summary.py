import manim as m
from background import add_background

class Summary(m.Scene):
    def construct(self):
        add_background(self)
<<<<<<< HEAD
        title = m.Tex(r"\underline{Conclusion}", font_size=70)
        title.to_edge(m.UP)
        cdict = m.MathTex(r"2^{2k+4} < 2^{2k+4}")

        self.add(title, cdict)
        self.play(cdict.animate.scale(2))
        self.play(m.Circumscribe(cdict, time_width=2, run_time=2, buff=0.5))
        
=======
        title = m.Tex(r"\undeline{Conclusion)", font_size=70)
        title.to_edge(m.UP)
        cdict = m.MathTex(r"2^{2k+4} < 2^{2k+4}")

        self.play(m.Write(title), m.Write(cdict))
>>>>>>> 3bf9e12a8c159b24be4ccd82b58f597fe7bd111c
