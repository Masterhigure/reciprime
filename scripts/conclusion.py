import manim as m
from background import add_background

class Conclusion(m.Scene):
    def construct(self):
        add_background(self)
        smalls = m.MathTex(r"n_s \leq 2^k\sqrt{n}")
        larges = m.MathTex(r"n_l \leq \frac n2")
        text0 = m.Tex(r"\underline{Conclusion}", font_size=70)
        text1 = m.Tex(r"Clearly we have $n = n_s + n_l$",
                r"and our estimates say that")
        text2 = m.MathTex(r"n = n_s + n_l \leq 2^k\sqrt n + \frac n2")
        text3 = m.Tex(r"But what happens for large $n$?")

        smalls.to_corner(m.DOWN + m.LEFT)
        larges.next_to(smalls, m.UP, aligned_edge=m.LEFT)
        self.add(smalls, larges)
        text1[1].next_to(text1[0], m.DOWN)
        text0.to_edge(m.UP)
        text1.next_to(text0, m.DOWN)
        text2.next_to(text1, m.DOWN)
        text3.next_to(text2, m.DOWN)

        self.play(m.Write(text0))
        self.play(m.Write(text1))
        self.play(m.Write(text2))
        self.play(m.Write(text3))
        self.wait()
