import manim as m
from background import add_background

class Split(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex(r"\underline{The sets to be estimated}", font_size=72)
        text1 = m.Tex(r"Let $n\in \Bbb N$.")
        text2 = m.Tex(r"$N = \{1, 2, \ldots, n\}$", " splits into")
        text3 = m.MathTex(r"\begin{array}{lr}N_{s}& \textrm{ with only small prime factors}\\" + \
                r"N_{l}&\textrm{ with at least one large prime factor}\end{array}")
        text5 = m.Tex("We will now estimate their sizes")

        title.to_edge(m.UP)
        text1.next_to(title, m.DOWN)
        text2.next_to(text1, m.DOWN)
        text3.next_to(text2, m.DOWN)
        text5.next_to(text3, m.DOWN, buff=0.75)

        self.play(m.Write(title))
        self.play(m.Write(text1))
        self.wait()
        self.play(m.Write(text2[0]))
        self.wait(4)
        self.play(m.Write(text2[1]))
        self.wait()
        self.play(m.Write(text3[0][:2]))
        self.wait()
        self.play(m.Write(text3[0][2:27]))
        self.wait(3)
        self.play(m.Write(text3[0][27:29]))
        self.wait()
        self.play(m.Write(text3[0][29:]))
        self.wait(3)
        self.play(m.Write(text5))
        self.wait()

        self.play(m.FadeOut(m.Group(title, text1, text3, text2, text5)))
