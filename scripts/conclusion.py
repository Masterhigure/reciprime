import manim as m
from background import add_background

class Conclusion(m.Scene):
    def construct(self):
        add_background(self)
        smalls = m.MathTex(r"n_s \leq {}", r"2^k\sqrt{n}")
        larges = m.MathTex(r"n_l \leq {}", r"\frac n2")
        text0 = m.Tex(r"\underline{Conclusion}", font_size=70)
        text2 = m.MathTex(r"n = n_s + n_l \leq {}", r"2^k\sqrt n", "{} + {}", r"\frac n2")
        text3 = m.Tex(r"What if $n = {}$", "$2^{2k+4}$?")

        larges.to_corner(m.DOWN + m.LEFT)
        smalls.next_to(larges, m.UP, aligned_edge=m.LEFT)
        self.add(smalls, larges)
        text0.to_edge(m.UP)
        text2.next_to(text0, m.DOWN)
        text3.next_to(text2, m.DOWN)
        ppos = text3[1].get_center()

        def movimation(mob, pos): 
            return m.MoveAlongPath(mob, m.Line(pos, mob.get_center()))

        self.play(m.Write(text0))
        self.play(m.Indicate(m.Group(smalls, larges)))
        self.play(m.Write(text2[0]))
        self.play(movimation(text2[1], smalls[1].get_center()))
        self.play(movimation(text2[3], larges[1].get_center()),
                m.Write(text2[2]))
        self.play(m.Write(text3))
        self.wait()

        text4a = m.MathTex(r"n", r"\leq",  "2^k", r"\sqrt{", "n}", "+", r"n", r"\cdot\frac 12")
        text4b = m.MathTex(r"2^{2k+4}", r"\leq", "2^k", r"\sqrt{", "2^{2k+4}}", "+", r"2^{2k+4}", r"\cdot \frac 12")
        text4c = m.MathTex(r"2^{2k+4}", r"\leq", "2^k", r"\cdot", "2^{k+2}", "+", r"2^{2k +3}", r"")

        text4a.next_to(text3, m.DOWN, buff=0.75)
        text4b.move_to(text4a)
        text4c.move_to(text4b)
        centers4c = [mob.get_center() for mob in text4c]
        for i, mob in enumerate(text4c):
            mob.move_to(text4b[i])
        text4c[3].shift(0.55*m.LEFT + 0.1*m.DOWN)

        self.play(m.Write(text4a))
        self.play(m.FadeOut(text4a[0]),
                movimation(text4b[0], ppos),
                text4a[1].animate.move_to(text4b[1]),
                text4a[2].animate.move_to(text4b[2]),
                m.Transform(text4a[3][0], text4b[3][0]),
                m.Transform(text4a[3][1], text4b[3][1]),
                m.FadeOut(text4a[4]),
                movimation(text4b[4], ppos),
                text4a[5].animate.move_to(text4b[5]),
                m.FadeOut(text4a[6]),
                movimation(text4b[6], ppos),
                text4a[7].animate.move_to(text4b[7]))
                
        self.clear()
        add_background(self)
        self.add(text0, text2, text3, smalls, larges, text4b)
        self.wait()
        self.play(m.Transform(text4b[3:5], text4c[3:5]))
        self.play(m.ReplacementTransform(text4b[6:], text4c[6]))
        self.clear()
        add_background(self)
        self.add(text0, text2, text3, smalls, larges, text4c)
        self.play(*[mob.animate.move_to(centers4c[i]) for i, mob in enumerate(text4c)])

        self.wait(2)
        text5 = m.MathTex(r"{}= 2^{2k + 2} + 2^{2k+3}", "< 2^{2k+3} + 2^{2k+3}", r"= 2\cdot 2^{2k + 3}", " = 2^{2k+4}")
        text5[0:2].next_to(text4c, m.DOWN, buff=0.5)
        text5[2:4].next_to(text5[0:2], m.DOWN, buff=0.5)
        self.play(m.Indicate(text4c[2:5]))
        self.play(m.Write(text5[0]))
        self.wait()
        self.play(m.Indicate(text5[0][5]))
        self.play(m.Indicate(text5[0][11]))
        self.wait()
        self.play(m.Write(text5[1][0]))
        self.wait()
        self.play(m.Write(text5[1][1:]))
        self.play(m.Indicate(text5[1][1:6]), m.Indicate(text5[1][7:12]))
        self.wait()
        self.play(m.Write(text5[2]))
        self.wait()
        self.play(m.Write(text5[3]))
        self.wait()
        self.play(m.Indicate(text4c[0]), m.Indicate(text5[1][0]), m.Indicate(text5[3][1:]), run_time=2)
        self.wait()

        text6 = m.MathTex("2^{2k+4}", " < ", "2^{2k + 4}")
        text6.next_to(text5, m.DOWN, buff=0.5)
        self.play(movimation(text6[0], text4c[0].get_center()),
                movimation(text6[1], text5[1][0].get_center()),
                movimation(text6[2], text5[3][1:].get_center()))
        self.play(m.FadeOut(m.Group(text2, text3, text4c, text5, smalls, larges)),
                text6.animate.move_to(m.ORIGIN))
        self.wait()

