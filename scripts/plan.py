import manim as m
from background import add_background

class Plan(m.Scene):
    def main_idea(self):
        title = m.Tex(r"\underline{Main idea:}", font_size=100).shift(2*m.UP)
        subtitle1 = m.Tex("(It might seem a little random,").next_to(title, m.DOWN, buff=1)
        subtitle2 = m.Tex("but I promise it will work out.)").next_to(subtitle1, m.DOWN)
        self.play(m.Write(title))
        self.play(m.Write(m.VGroup(subtitle1, subtitle2)))
        self.wait(2)
        self.play(m.Unwrite(m.VGroup(subtitle1, subtitle2)), title.animate.to_edge(m.UP))
        return title

    def more_details(self, title):
        true_limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = {}", "", r"\infty")
        headline = m.Tex("We want to prove").next_to(true_limit, m.UP)
        idea1 = m.Tex("For contradiction, we will")
        idea2 = m.Tex("assume the limit is finite:").next_to(true_limit, m.UP)
        idea1.next_to(idea2, m.UP)
        limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = {}", "L < {}", r"\infty")
        conclusion1 = m.Tex(r"We will conclude that").next_to(limit, m.DOWN, buff=0.75)
        conclusion1b = m.Tex(r"some set $N = \{1, 2, \ldots, n\}$").next_to(conclusion1, m.DOWN)
        conclusion2 = m.Tex("has fewer than $n$ elements.").next_to(conclusion1b, m.DOWN)
        self.play(m.Write(headline))
        self.play(m.Write(true_limit))
        self.play(m.Unwrite(headline))
        self.play(m.Write(m.VGroup(idea1, idea2)))
        self.play(m.ReplacementTransform(true_limit[0], limit[0]),
                m.FadeIn(limit[1]),
                m.ReplacementTransform(true_limit[1], limit[2]))
        self.play(m.Write(m.VGroup(conclusion1, conclusion1b, conclusion2)))
        self.play(m.Unwrite(m.VGroup(title, idea1, idea2, limit, conclusion1, conclusion1b, conclusion2)))
        self.wait(1)

    def construct(self):
        add_background(self)
        title = self.main_idea()
        self.more_details(title)
