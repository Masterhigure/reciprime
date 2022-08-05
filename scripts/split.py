import manim as m
from background import add_background

class Split(m.Scene):
    def construct(self):
        add_background(self)
        text1 = m.Tex(r"Let $n\in \Bbb N$.")
        text2 = m.Tex(r"$N = \{1, 2, \ldots, n\}$ splits into")
        text3 = m.Tex(r"$N_{\textrm{small}}$ with only small prime factors")
        text4 = m.Tex(r"$N_{\textrm{large}}$ with at least one large prime factor")
        text5 = m.Tex("Let's estimate their sizes")
        texts = [text1, text2, text3, text4, text5]

        text1.shift(3*m.UP)
        text2.next_to(text1, m.DOWN)
        text3.next_to(text2, m.DOWN)
        text4.next_to(text3, m.DOWN)
        text5.next_to(text4, m.DOWN)

        self.play(m.AnimationGroup(*[m.Write(text) for text in texts], lag_ratio=1))
        self.wait()
