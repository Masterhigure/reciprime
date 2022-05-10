import manim as m

def add_background(scene):
    bg = m.ImageMobject("media/images/penrose.png")
    scene.add(bg)


class Image(m.Scene):
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

class Problem(m.Scene):
    def construct(self):
        add_background(self)
        self.box_numbers()
        self.stretch_boxes()
        self.align_boxes()
        self.pile_boxes(14)
        self.fadeout_boxes(14, 17)
        self.faded_boxes(17, 30, 35)

    def box_numbers(self):
        numbers = []
        for i in range(1, 26):
            numbers.append(m.Tex(i).shift(3*m.UP + 7*m.LEFT + (0.65*i)*m.RIGHT))
        self.play(*[m.Create(number) for number in numbers])
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        composites = [i for i in range(1, 26) if i not in primes]
        onscreen_boxes = [m.Rectangle(width=0.52, height=0.52).shift(3*m.UP + 7*m.LEFT + (0.65*p)*m.RIGHT) for p in primes]
        self.play(m.AnimationGroup(*[m.Create(box) for box in onscreen_boxes]))
        self.play(*[m.FadeOut(numbers[c-1]) for c in composites],
                *[numbers[p-1].animate.move_to(m.DOWN + 7*m.LEFT + (1.5*i+1)*m.RIGHT) for i, p in enumerate(primes)],
                *[b.animate.move_to(7*m.LEFT + (1.5*i+1)*m.RIGHT) for i, b in enumerate(onscreen_boxes)])
        self.onscreen_boxes = onscreen_boxes
        self.primes = primes
        self.numbers = numbers

    def stretch_boxes(self):
        onscreen_boxes = self.onscreen_boxes
        primes = self.primes
        numbers = self.numbers
        braces = []
        squish_animations = []
        brace_and_number_anims = []
        for p, b in zip(primes, onscreen_boxes):
            b2 = m.Rectangle(width=0.52/p, height=0.52*p).move_to(b)
            brace = m.Brace(b2, m.LEFT)
            braces.append(brace)
            squish_animations.append(m.Transform(b, b2))
            brace_and_number_anims.append(m.AnimationGroup(numbers[p-1].animate.next_to(brace, m.LEFT, buff=0.15), m.FadeIn(brace)))
        squish_anim_group = m.AnimationGroup(*squish_animations, lag_ratio=0.8)
        brace_num_anim_group = m.AnimationGroup(*brace_and_number_anims, lag_ratio=0.8)
        self.play(squish_anim_group, brace_num_anim_group)
        self.braces = braces

    def align_boxes(self):
        braces = self.braces
        numbers = self.numbers
        primes = self.primes
        onscreen_boxes = self.onscreen_boxes
        align_animations = []
        for p, box, brace in zip(primes, onscreen_boxes, braces):
            brace2 = m.Brace(box, m.DOWN, buff=0.1).shift(0.52*p/2*m.UP + 2*m.DOWN)
            align_animations.append(m.AnimationGroup(
                box.animate.shift(0.52*p/2*m.UP + 2*m.DOWN),
                m.Transform(brace, brace2),
                m.Transform(numbers[p-1], m.MathTex(r"\frac1{" + str(p) + "}").next_to(brace2, m.DOWN))))
        align_anim_group = m.AnimationGroup(*align_animations, lag_ratio=1)
        self.play(align_anim_group)
        self.play(*[m.FadeOut(b) for b in braces],
                *[m.FadeOut(numbers[p-1]) for p in primes])

    def pile_boxes(self, stop):
        primes = self.primes
        onscreen_boxes = self.onscreen_boxes
        s = 0

        for i, (b, p) in enumerate(zip(onscreen_boxes, primes)):
            self.play(b.animate.shift((1.5*i - 0.52*s)*m.LEFT), run_time=0.3*(i/8) + (1-i/8))
            s += 1/p
        more_primes = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
                337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                503, 509, 521, 523, 541, 547, 557]
        l = onscreen_boxes[-1].copy().shift((20 - 0.52*(s-1/primes[-1]))*m.RIGHT)
        offscreen_animations = []
        offscreen_boxes = []
        for p in more_primes:
            l2 = l.copy()
            offscreen_animations.append(l2.animate.shift((20-0.52*s)*m.LEFT))
            s += 1/p
            offscreen_boxes.append(l2)

        offscreen_boxes_group = m.Group(*offscreen_boxes)
        self.add(offscreen_boxes_group)
        clear_animations = m.AnimationGroup(*offscreen_animations[:stop], lag_ratio=0.8, group=offscreen_boxes_group)
        self.play(clear_animations, run_time=0.3*stop)
        self.offscreen_animations = offscreen_animations
        self.offscreen_boxes = offscreen_boxes
        self.offscreen_boxes_group = offscreen_boxes_group
        self.l = l
        self.more_primes = more_primes
        self.s = s

    def fadeout_boxes(self, start, stop):
        offscreen_animations = self.offscreen_animations
        offscreen_boxes_group = self.offscreen_boxes_group
        text1 = m.Tex(r"About \(10^{60\,000\,000}\) primes", font_size=100)
        text2 = m.Tex("to reach the end of the screen", font_size=100)
        bg = m.ImageMobject("media/images/penrose.png")
        bg.fade(1)
        self.add(bg)
        text1.shift(m.UP)
        text2.next_to(text1, m.DOWN)
        fading_animations = m.AnimationGroup(*offscreen_animations[start:stop], lag_ratio=0.8, group=offscreen_boxes_group)
        self.play(bg.animate.fade(0.3),
                m.Write(text1),
                m.Write(text2),
                fading_animations,
                run_time=0.3*(stop-start))
        self.text1, self.text2 = text1, text2
        self.bg = bg

    def faded_boxes(self, start, stop, end):
        bg = self.bg.copy()
        bg.fade(1)
        self.add(bg)
        offscreen_animations = self.offscreen_animations
        offscreen_boxes_group = self.offscreen_boxes_group
        faded_animations = m.AnimationGroup(*offscreen_animations[start:stop], lag_ratio=0.8, group=offscreen_boxes_group)
        self.play(faded_animations, run_time=0.3*(stop-start))
        end_animations = m.AnimationGroup(*offscreen_animations[stop:end], lag_ratio=0.8, group=offscreen_boxes_group)
        self.play(end_animations, bg.animate.fade(0), run_time=0.3*(end - stop))
