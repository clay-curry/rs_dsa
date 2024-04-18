from manim import *


FONTS = ['C059', 'D050000L', 'DejaVu Sans',  'DejaVu Sans Mono', 'DejaVu  Serif', 'Droid Sans Fallback',  'Inconsolata', 'Lato',  'Monospace', 'Nimbus Mono PS',  'Nimbus Roman', 'Nimbus Sans',  'Nimbus Sans Narrow', 'Noto  Mono', 'Noto Sans Mono',  'P052', 'Sans', 'Serif',  'Source Code Pro', 'Standard  Symbols PS', 'System-ui', 'URW  Bookman', 'URW Gothic',  'Ubuntu', 'Ubuntu Condensed',  'Ubuntu Mono', 'Z003']


class InsertionSort(Scene):
    def construct(self):
        self._pivot = None
        self._insertion_point = None
        self.numbers = [7, 6, 5, 3, 2, 0, 1, 9, 10, 8, 4]
        self.insertionSort()
    
    def insertionSort(self):
        self.pivot = 0
        self.insertion_point = 1
        while self.insertion_point < len(self.numbers):
            left = self.numbers[self.pivot]
            right = self.numbers[self.pivot + 1]

            while self.pivot >= 0 and left > right:
                if left > right:
                    self._numbers.swap(self.pivot, self.pivot + 1)                    
                if self.pivot == 0:
                    break
                self.pivot -= 1
                left = self.numbers[self.pivot]
                right = self.numbers[self.pivot + 1]

                
                            
            self.play(
                self._numbers._numbers[self.pivot].animate.set_color(GREEN),
                self._numbers._numbers[self.pivot].animate.set_color(GREEN)
            )
            self.insertion_point += 1
            self.pivot = self.insertion_point - 1
            print(self.insertion_point, self.pivot, len(self.numbers))

        self.play(self._numbers._numbers[-1].animate.set_color(GREEN))
        self.wait(2)

    @property
    def insertion_point(self):
        return None if self._insertion_point is None else int(self._insertion_point.text)

    @insertion_point.setter
    def insertion_point(self, idx):
        if (self._insertion_point is None):
                self._insertion_point = Text(str(idx), font=FONTS[0], font_size = DEFAULT_FONT_SIZE * 0.9).shift(UP * 2 + LEFT * 4)
                self.add(self._insertion_point)
         
        elif int(idx) != self.insertion_point:
            # only update if the value is different
            new_insertion_point = Text(str(idx), font=FONTS[0], font_size = DEFAULT_FONT_SIZE * 0.9).shift(UP * 2 + LEFT * 4)
            self.play(Transform(self._insertion_point, new_insertion_point))
            self._insertion_point.text = new_insertion_point.text

    @property
    def pivot(self):
        return None if self._pivot is None else int(self._pivot.text)

    @pivot.setter
    def pivot(self, idx):
        if (self._pivot is None):
            self._pivot = Text(str(idx), font=FONTS[0], font_size = DEFAULT_FONT_SIZE * 0.9).shift(UP * 2 + LEFT * 5)
            self.add(self._pivot)
         
        elif int(idx) != self.pivot:
            # only update if the value is different
            new_pivot = Text(str(idx), font=FONTS[0], font_size = DEFAULT_FONT_SIZE * 0.9).shift(UP * 2 + LEFT * 5)
            self.play(Transform(self._pivot, new_pivot))
            self._pivot.text = new_pivot.text

    
    @property
    def numbers(self):
        return [int(k.text) for k in self._numbers._numbers]
    
    @numbers.setter
    def numbers(self, numbers):
        self._numbers = NumberList(numbers, self)



class NumberList:
    def __init__(self, numbers, scene, **kwargs):
        super().__init__(**kwargs)
        scene.add(*[
            Square(side_length=1).set_stroke(color=WHITE, width=3).shift(DOWN * 2 + LEFT * len(numbers) / 2 + RIGHT * idx) for idx, _ in enumerate(numbers)
        ])
        self._numbers = [
            Text(str(i), font=FONTS[0], font_size = DEFAULT_FONT_SIZE * 0.9).shift(DOWN * 2 + LEFT * len(numbers) / 2 + RIGHT * idx) for idx, i in enumerate(numbers)
        ]
        scene.add(*self._numbers)
        self.scene = scene

    
    def swap(self, idx_l, idx_r):
        self.scene.play(
            self._numbers[idx_l].animate.shift(DOWN * 1.2), 
            self._numbers[idx_r].animate.shift(DOWN * 1.2), 
            run_time=0.2
        )
        self.scene.wait(0.1)
        self.scene.play(
            self._numbers[idx_l].animate.shift(RIGHT * (idx_r - idx_l)), 
            self._numbers[idx_r].animate.shift(LEFT * (idx_r - idx_l)), 
            run_time=1.1 * abs(idx_r - idx_l) / len(self._numbers)
        )
        self.scene.wait(0.1)
        self.scene.play(
            self._numbers[idx_l].animate.shift(UP * 1.2), 
            self._numbers[idx_r].animate.shift(UP * 1.2),
            run_time=0.2
        )

        temp = self._numbers[idx_l]
        self._numbers[idx_l] = self._numbers[idx_r]
        self._numbers[idx_r] = temp

