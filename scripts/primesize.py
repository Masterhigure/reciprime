import manim as m
from background import add_background

class Primesize(m.Scene):
    def construct(self):
        add_background(self)
        title = m.Tex(r"\underline{For contradiction:}", font_size=72).to_edge(m.UP)
        text1 = m.Tex(r"\centering Assuming the limit is $L$,\\we can split the sum into two parts:")
        orig_sum = m.MathTex(r"\sum_{p\textrm{ prime}} \frac1{p}", "{} = L")
        split_sum = m.MathTex(
                r"\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p}",
                r"{} + \sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p}", 
                "{} = L")
        text2 = m.Tex("in such a way that")
        split_explain = m.MathTex(r"\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p} \geq L - \frac12\qquad",
                r"\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p} < \frac12")
        enh_split_sum = m.MathTex(
                r"\underbrace{\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p}}_{{}\geq L-\frac12}",
                r"{} + \underbrace{\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p}}_{{}< \frac12}", 
                "{} = L")
        text3 = m.Tex(r"Call all the primes below $K$ \emph{small primes},\\and all primes larger than $K$ \emph{large primes}")

        text1.next_to(title, m.DOWN)
        split_sum.next_to(text1, m.DOWN)
        orig_sum.next_to(text1, m.DOWN)
        enh_split_sum.next_to(text1, m.DOWN)
        text2.next_to(split_sum, m.DOWN)
        split_explain.next_to(text2, m.DOWN)
        text3.next_to(enh_split_sum, m.DOWN)

        #self.add(enh_split_sum, m.index_labels(enh_split_sum[0]), m.index_labels(enh_split_sum[1]))
        #self.wait(3)

        self.play(m.Write(title))
        self.play(m.Write(text1))
        self.play(m.Write(orig_sum))


        s = orig_sum[0].copy()

        self.play(s.animate.move_to(split_sum[0][0:7] + split_sum[0][10:13]),
                orig_sum[0].animate.move_to(split_sum[1][1:8] + split_sum[1][11:14]),
                m.Write(split_sum[1][0]),
                orig_sum[1].animate.move_to(split_sum[2]))
        self.play(m.Write(split_sum[0][7:10] + split_sum[1][8:11]))
        self.play(m.Write(split_explain))
        
        self.wait(1)
        self.play(split_explain[0][13:].animate.move_to(enh_split_sum[0][19:25]).scale(0.6),
                m.FadeIn(enh_split_sum[0][13:19]),
                m.FadeOut(split_explain[0][:13]))
        self.play(split_explain[1][13:].animate.move_to(enh_split_sum[1][20:24]).scale(0.6),
                m.FadeIn(enh_split_sum[1][14:20]),
                m.FadeOut(split_explain[1][:13]))
        self.play(m.Write(text3))
        self.wait(1)
        self.play(m.Unwrite(m.VGroup(title, text1, s, split_sum[1][0], orig_sum,
            split_sum[0][7:10], split_sum[1][8:11],
            enh_split_sum[0][13:19], split_explain[0][13:], enh_split_sum[1][14:20],
            split_explain[1][13:], text3)))

