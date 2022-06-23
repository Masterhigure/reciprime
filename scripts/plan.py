import manim as m

def add_background(scene):
    bg = m.ImageMobject("media/images/penrose.png")
    scene.add(bg)

class Plan(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex("Main idea:", font_size=144).shift(2*m.UP)
        subtitle1 = m.Tex("Seems a little random,").next_to(title, m.DOWN)
        subtitle2 = m.Tex("but I promise it will work out").next_to(subtitle1, m.DOWN)
        self.play(m.Write(title))
        self.play(m.Write(m.VGroup(subtitle1, subtitle2)))
        self.wait(2)
        self.play(m.Unwrite(m.VGroup(title, subtitle1, subtitle2)))

        headline = m.Tex("We want to prove", font_size=72).to_edge(m.UP).shift(0.2*m.UP)
        true_limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = \infty").next_to(headline, m.DOWN)
        idea1 = m.Tex("For contradiction, we will", font_size=72).next_to(true_limit, m.DOWN)
        idea2 = m.Tex("assume the limit is finite:", font_size=72).next_to(idea1, m.DOWN)
        limit = m.MathTex(r"\sum_{p \textrm{ prime}}\frac1p = L < \infty").next_to(idea2, m.DOWN)
        conclusion1 = m.Tex(r"We will conclude that $\{1, 2, \ldots, N\}$", font_size=72).next_to(limit, m.DOWN)
        conclusion2 = m.Tex("has fewer than $N$ elements.", font_size=72).next_to(conclusion1, m.DOWN)
        self.play(m.Write(headline))
        self.play(m.Write(true_limit))
        self.play(m.Write(m.VGroup(idea1, idea2)))
        self.play(m.Write(limit))
        self.play(m.Write(m.VGroup(conclusion1, conclusion2)))
        self.play(m.Wait(3))
