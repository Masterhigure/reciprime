import manim as m
from background import add_background

class Smalls(m.Scene):
    def construct(self):
        add_background(self)
        text1 = m.Tex(r"First we estimate $n_{s} = |N_{s}|$")
        text2 = m.Tex(r"Take an $x\in N_{\textrm s}$")

        text3a = m.MathTex(r"x = {}", "", r"p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}")
        text3b = m.MathTex(r"x = {}", r"x_s^2\cdot {}", r"p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}")
        text4a = m.MathTex(r"0\leq e_i", "")
        text4b = m.MathTex(r"0\leq e_i", r"{}\leq 1")
        text5a = m.Tex(r"How many possibilities are there for the")
        text5b = m.Tex(r"different parts of the right-hand side?")

        text1.shift(3*m.UP)
        text2.next_to(text1, m.DOWN)
        text3a.next_to(text2, m.DOWN)
        text3b.next_to(text2, m.DOWN)
        text4a.next_to(text3a, m.DOWN)
        text4b.next_to(text3b, m.DOWN)
        text5a.next_to(text4b, m.DOWN)
        text5b.next_to(text5a, m.DOWN)

        self.play(m.Write(text1))
        self.play(m.Write(text2))
        self.play(m.AnimationGroup(m.Write(text3a), m.Write(text4a), lag_ratio = 0.8), run_time=3)
        self.wait()
        self.play(m.ReplacementTransform(text3a, text3b),
                  m.ReplacementTransform(text4a, text4b))
        self.wait()
        self.play(m.Write(text5a))
        self.play(m.Write(text5b))
        self.wait()

