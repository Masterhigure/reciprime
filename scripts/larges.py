import manim as m
from background import add_background

class Larges(m.Scene):
    def construct(self):
        add_background(self)
        smalltext = m.MathTex(r"n_s \leq \sqrt K\cdot 2^k")
        smalltext.to_corner(m.UP + m.LEFT)
        self.add(smalltext)

        text1 = m.Tex(r"Now we estimate $n_l = |N_l|$.")
        text2 = m.Tex(r"Pick a prime $p$ that is large (greater than $K$).")
        text3 = m.Tex(r"How many numbers in $N$ are divisible by $p$?")
        text4 = m.Tex(r"It's $\left\lfloor\frac np\right\rfloor$")

        text1.to_edge(m.UP).shift(m.DOWN)
        text2.next_to(text1, m.DOWN)
        text3.next_to(text2, m.DOWN)
        text4.next_to(text3, m.DOWN)

        self.play(m.Write(text1))
        self.play(m.Write(text2))
        self.play(m.Write(text3))
        self.wait()
        self.play(m.Write(text4))
        self.wait()
        self.play(m.Unwrite(text1), m.Unwrite(text2))
        self.play(text3.animate.shift(2*m.UP), text4.animate.shift(2*m.UP))
