import manim as m
from background import add_background

class Plan(m.Scene):
    def main_idea(self):
        title = m.Tex("Main idea:", font_size=144).shift(2*m.UP)
        subtitle1 = m.Tex("(It might seem a little random,").next_to(title, m.DOWN, buff=1)
        subtitle2 = m.Tex("but I promise it will work out.)").next_to(subtitle1, m.DOWN)
        self.play(m.Write(title))
        self.play(m.Write(m.VGroup(subtitle1, subtitle2)))
        self.wait(2)
        self.play(m.Unwrite(m.VGroup(title, subtitle1, subtitle2)))

    def more_details(self):
        true_limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = {}", "", r"\infty")
        headline = m.Tex("We want to prove", font_size=72).next_to(true_limit, m.UP)
        idea1 = m.Tex("For contradiction, we will", font_size=72)
        idea2 = m.Tex("assume the limit is finite:", font_size=72).next_to(true_limit, m.UP)
        idea1.next_to(idea2, m.UP)
        limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = {}", "L < {}", r"\infty")
        conclusion1 = m.Tex(r"We will conclude that some set $\{1, 2, \ldots, N\}$", font_size=72).next_to(limit, m.DOWN)
        conclusion2 = m.Tex("has fewer than $N$ elements.", font_size=72).next_to(conclusion1, m.DOWN)
        self.play(m.Write(headline))
        self.play(m.Write(true_limit))
        self.play(m.Unwrite(headline))
        self.play(m.Write(m.VGroup(idea1, idea2)))
        self.play(m.ReplacementTransform(true_limit, limit))
        self.play(m.Write(m.VGroup(conclusion1, conclusion2)))
        self.play(m.Unwrite(m.VGroup(idea1, idea2, limit, conclusion1, conclusion2)))
        self.wait(1)

    def construct(self):
        add_background(self)
        self.main_idea()
        self.more_details()
