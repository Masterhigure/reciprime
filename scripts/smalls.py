import manim as m
from background import add_background

class Smalls(m.Scene):
    def construct(self):
        add_background(self)
        text1 = m.Tex(r"First we estimate $n_{s} = |N_{s}|$")
        text2 = m.Tex(r"Take an $x\in N_{\textrm s}$")

        text3a = m.MathTex(r"x = {}", "", r"p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}")
        text3b = m.MathTex(r"x = {}", r"x_s^2\cdot {}", r"p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}")
        text4a = m.MathTex(r"0\leq e_i", "", "")
        text4b = m.MathTex(r"0\leq e_i", r"{}\leq 1\hphantom{al}", r"\\ 1\leq x_s\leq \sqrt K")
        text5a = m.Tex(r"How many possibilities are there for the")
        text5b = m.Tex(r"different parts of the right-hand side?")
        text6a = m.Tex(r"$x_s$ has $\lfloor \sqrt K\rfloor$ possibilities")
        text6b = m.Tex(r"Each $e_i$ has 2 possibilities")
        text7a = m.Tex(r"Thus: ", r"$n_s \leq \sqrt K\cdot 2^k$")
        text7b = m.Tex("", r"$n_s \leq \sqrt K\cdot 2^k$")

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
        self.play(m.Unwrite(text1), m.Unwrite(text2))
        self.play(m.Group(text3b, text4b, text5b, text5a).animate.shift(2*m.UP))
        self.wait()
        text6a.next_to(text5b, m.DOWN)
        text6b.next_to(text6a, m.DOWN)
        text7a.next_to(text6b, m.DOWN)
        text7b.to_corner(m.UP + m.LEFT)
        self.play(m.Write(text6a))
        self.play(m.Write(text6b))
        self.wait()
        self.play(m.Write(text7a))
        self.play(m.Unwrite(text3b),
                m.Unwrite(text4b),
                m.Unwrite(text5a),
                m.Unwrite(text5b),
                m.Unwrite(text6a),
                m.Unwrite(text6b))
        self.play(m.Unwrite(text7a[0]))
        self.play(text7a[1].animate.to_corner(m.UP + m.LEFT))
        self.wait()
