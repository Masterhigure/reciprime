import manim as m
from background import add_background

class Primesize(m.Scene):
    def construct(self):
        add_background(self)
        fs = 45
        text1 = m.Tex(r"\centering Assuming the limit is $L$,\\we can split the sum into two parts:", font_size=fs)
        orig_sum = m.MathTex(r"\sum_{p\textrm{ prime}} \frac1{p}", "", "{} = L", font_size=fs)
        split_sum = m.MathTex(
                r"\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p}",
                r"{} + \sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p}", 
                "{} = L",
                font_size=fs)
        text2 = m.Tex("in such a way that", font_size=fs)
        split_explain = m.MathTex(r"\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p} &\geq L - \frac12\\" + \
                r"\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p} &< \frac12", font_size=fs)
        enh_split_sum = m.MathTex(
                r"\underbrace{\sum_{\substack{p\textrm{ prime}\\p < K}} \frac1{p}}_{{}\geq L-\frac12}",
                r"{} + \underbrace{\sum_{\substack{p\textrm{ prime}\\p \geq K}} \frac1{p}}_{{}< \frac12}", 
                "{} = L",
                font_size=fs)
        text3 = m.Tex(r"Call all the primes below $K$ \emph{small primes},\\and all primes larger than $K$ \emph{large primes}", font_size=fs)

        split_sum.next_to(text2, m.UP)
        orig_sum.next_to(text2, m.UP)
        text1.next_to(split_sum, m.UP)
        split_explain.next_to(text2, m.DOWN)
        enh_split_sum.next_to(text1, m.DOWN)
        text3.next_to(enh_split_sum, m.DOWN)

        self.play(m.Write(text1))
        self.play(m.Write(orig_sum))
        self.play(m.ReplacementTransform(orig_sum, split_sum))
        self.play(m.Write(text2))
        self.play(m.Write(split_explain))
        
        self.wait(1)
        self.play(m.Unwrite(m.VGroup(text2, split_explain)))
        self.play(m.ReplacementTransform(split_sum, enh_split_sum))
        self.play(m.Write(text3))
        self.wait(1)
        self.play(m.Unwrite(m.VGroup(text1, split_sum, enh_split_sum, text3)))

