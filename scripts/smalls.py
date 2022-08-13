import manim as m
from background import add_background

class Smalls(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex(r"\underline{Estimating $n_s = |N_s|$", font_size=72)
        title.to_edge(m.UP)
        self.play(m.Write(title))

        text1 = m.MathTex("r = ", r"p_1^{e_1}\cdot p_2^{e_2}\cdot p_3^{e_3}\cdots p_k^{e_k}", r"0\leq e_i")
        # terms: text1[1][0:4] + text1[1][5:9] + text1[1][10:14] + text1[1][17:21]
        text2 = m.MathTex("r = ", r"x^2\cdot", r"p_1^{e_1}\cdot p_2^{e_2}\cdot p_3^{e_3}\cdots p_k^{e_k}", r"0\leq e_i", r"\leq 1, \quad x^2\leq n")
        one = m.MathTex(r"1\cdot{}")
        text1[0:2].next_to(title, m.DOWN, buff=1)
        text1[2].next_to(text1[0:2], m.DOWN)
        text2[:3].move_to(text1[0:2])
        text2[3:].next_to(text2[:3], m.DOWN)
        one[0].move_to(m.Group(text2[1][0], text2[1][2]))

        self.play(m.Write(text1))
        self.wait()
        self.play(text1[0].animate.move_to(text2[0]),
                text1[1].animate.move_to(text2[2]))
        self.play(m.FadeIn(one))
        self.wait()

        x_center = text2[1][0:2].get_corner(m.RIGHT + m.DOWN)

        self.play(one[0][1].animate.move_to(text2[1][2]),
                m.Transform(one[0][0], text2[1][0:2].scale(1/(1.3**3), about_point=x_center)),
                text1[1][0:4].copy().animate.move_to(text2[1][0]).fade(1))
        self.wait()
        self.play(m.AnimationGroup(text1[1][5:9].copy().animate.move_to(text2[1][0]).fade(1),
                                   m.AnimationGroup(one[0][0].animate.scale(1.3, about_point=x_center), run_time=0.3),
                                   lag_ratio=0.6))
        self.wait()
        self.play(m.AnimationGroup(text1[1][10:14].copy().animate.move_to(text2[1][0]).fade(1),
                                   m.AnimationGroup(one[0][0].animate.scale(1.3, about_point=x_center), run_time=0.3),
                                   lag_ratio=0.6))
        self.wait()
        self.play(m.AnimationGroup(text1[1][17:21].copy().animate.move_to(text2[1][0]).fade(1),
                                   m.AnimationGroup(one[0][0].animate.scale(1.3, about_point=x_center), run_time=0.3),
                                   lag_ratio=0.6))
        self.wait()
        self.play(text1[2].animate.move_to(text2[3]), m.FadeIn(text2[4]))

        text3 = m.MathTex(r"\textrm{Possibilities for }x\textrm{: }", r"\left\lfloor\sqrt{n}\right\rfloor\leq ", r"\sqrt{n}")
        text4 = m.Tex(r"Possibilities for all the $e_i$: ", r"at most ", r"$2^k$")
        text5 = m.Tex("Possibilities for $r$: ", r"at most ", r"$2^k\cdot \sqrt n$")
        
        text3[0].move_to(text4, aligned_edge=m.LEFT)
        text5[0].move_to(text4, aligned_edge=m.LEFT)
        text5[1:].next_to(text4[0])
        text4[1:].move_to(text5, aligned_edge=m.RIGHT)
        text3[1:].move_to(text5, aligned_edge=m.RIGHT)

        text4.next_to(text3, m.DOWN, aligned_edge=m.LEFT)
        text5.next_to(text4, m.DOWN, aligned_edge=m.LEFT)
        m.Group(text3, text4, text5).next_to(text2, m.DOWN)

        self.play(m.Write(text3))
        self.wait()
        self.play(m.Write(text4))
        self.wait()
        self.play(m.Write(text5))
        self.wait()

        smalls = m.MathTex(r"n_s \leq 2^k\cdot \sqrt{n}")
        smalls.move_to(text5, aligned_edge=m.RIGHT)

        self.play(m.FadeOut(text5),
                m.FadeIn(smalls))
        self.play(m.Indicate(smalls))
        self.wait()
        self.play(smalls.animate.to_corner(m.DOWN + m.LEFT),
                m.FadeOut(m.Group(title, text1, text3, text4, one, text2[4])))
        self.wait()
