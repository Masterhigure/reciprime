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

        erdos = m.ImageMobject("media/images/Erdos.jpg").shift(5*m.LEFT + 2*m.UP).rotate(0.5)
        self.add(erdos)
        self.wait()

        book = m.ImageMobject("media/images/book.jpg").scale(0.5).shift(4.5*m.RIGHT + 1.7*m.DOWN).rotate(-0.5)
        self.add(book)
        self.wait()
