import manim as m
from background import add_background

class Smalls(m.Scene):
    def construct(self):
        add_background(self)
        text1 = m.Tex("First we look at the small primes")
        self.play(m.Write(text1))
        self.wait()
        self.play(m.Unwrite(text1))
        self.wait()
