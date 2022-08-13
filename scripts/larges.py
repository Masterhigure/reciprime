import manim as m
from background import add_background

class Larges(m.Scene):
    def construct(self):
        add_background(self)
        smalltext = m.MathTex(r"n_s \leq \sqrt k\cdot 2^k")
        smalltext.to_corner(m.DOWN+ m.LEFT)
        self.add(smalltext)

        text1 = m.Tex(r"\underline{Estimating $n_l = |N_l|$}", font_size = 72)
        text4 = m.Tex(r"$\left\lfloor\frac np\right\rfloor$ numbers in $N$ are divisible by $p$")

        text1.to_edge(m.UP)
        text4.next_to(text1, m.DOWN)

        self.play(m.Write(text1))
        self.play(m.Write(text4))
        self.wait()
        
        text5a = m.Tex(r"So how many numbers in $N$ are divisble")
        text5b = m.Tex(r"by \emph{at least one} large prime?")
        text6 = m.Tex(r"Add the contribution from each large prime:")
        text7a = m.MathTex(r"n_l\leq\sum_{\substack{p\textrm{ prime}\\p \geq K}} \left\lfloor\frac n{p}\right\rfloor")
        text7b = m.MathTex(r"n_l\leq\sum_{\substack{p\textrm{ prime}\\p \geq K}} \left\lfloor\frac n{p}\right\rfloor",
                r"{}\leq\phantom{n\mkern-10mu} \sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac n{p}")
        text7c = m.MathTex(r"n_l\leq\sum_{\substack{p\textrm{ prime}\\p \geq K}} \left\lfloor\frac n p\right\rfloor",
                r"{} = n\mkern-10mu\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac 1{p}")
        text7d = m.MathTex(r"n_l\leq\sum_{\substack{p\textrm{ prime}\\p \geq K}} \left\lfloor\frac n p\right\rfloor",
                r"{} = n\mkern-10mu\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac 1{p}",
                r"{} < n\cdot \frac12")
        text7e = m.MathTex(r"{}<\frac n2")
        larges = m.MathTex(r"n_l\leq\frac n2")

        text5a.next_to(text4, m.DOWN)
        text5b.next_to(text5a, m.DOWN)
        text6.next_to(text5b, m.DOWN)
        text7a.next_to(text6, m.DOWN)
        text7b.next_to(text6, m.DOWN)
        text7c.next_to(text6, m.DOWN)
        text7d.next_to(text6, m.DOWN)
        text7d.move_to(text7c, aligned_edge=m.LEFT)
        text7e.move_to(text7d[2], aligned_edge=m.LEFT)

        self.play(m.Write(text5a), m.Write(text5b))
        self.play(m.Write(text6))
        self.play(m.Write(text7a))
        self.play(text7a.animate.move_to(text7b, aligned_edge=m.LEFT), m.Write(text7b[1]))
        self.remove(text7a)
        self.add(text7b)
        self.wait()
        self.play(m.Transform(text7b[1][11], text7c[1][1]),
                m.Write(text7c[1][12]))
        self.wait()
        self.play(m.Write(text7d[2]))
        self.wait()
        self.play(m.FadeOut(text7d[2][2:4]),
                m.ReplacementTransform(text7d[2][:2], text7e[0][:2]),
                m.ReplacementTransform(text7d[2][4:], text7e[0][2:]))
        self.wait()
        self.play(m.Indicate(text7b[0][:3]),
            m.Indicate(text7b[1][0]),
            m.Indicate(text7e),
            run_time=2)
        self.wait()
        self.play(m.ReplacementTransform(text7b[0][:2], larges[0][:2]),
                m.ReplacementTransform(text7b[1][0], larges[0][2]),
                m.ReplacementTransform(text7e[0][1:], larges[0][3:]),
                m.FadeOut(m.Group(text4, text5a, text5b, text6,
                    text7b[0][2:], text7b[1][1:], text7c[1][12], text7e[0][0])))
        self.wait()
        l = larges.copy().to_corner(m.LEFT + m.DOWN)
        self.play(smalltext.animate.next_to(l, m.UP, aligned_edge=m.LEFT),
                larges.animate.to_corner(m.LEFT + m.DOWN))
        self.play(m.FadeOut(text1))
