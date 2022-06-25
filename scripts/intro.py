import manim as m
from background import add_background

class Intro(m.Scene):
    def intro(self):
        text1 = m.Text("26th of June, 2009")
        text2 = m.Text("xkcd.com/602")
        text1.shift(m.UP*0.75)
        text2.next_to(text1, m.DOWN)
        self.play(m.FadeIn(text1))
        self.wait()
        self.play(m.FadeIn(text2))
        self.wait(2)
        self.play(m.FadeOut(text1, text2))
        self.wait()

    def motivation(self):
        image = m.ImageMobject("media/images/overstimulated.png")
        scale = 3
        image.scale(scale)
        dist = scale*6.5 - 4
        image.shift(dist*m.DOWN)
        self.play(m.FadeIn(image))
        self.play(image.animate.shift(2*dist*m.UP), run_time=8)
        self.wait()
        self.play(image.animate.shift(0.514*dist*m.DOWN), run_time=2)
        self.wait(2)
        self.play(m.FadeOut(image))
        
    def construct(self):
        add_background(self)
        self.intro()
        self.motivation()

