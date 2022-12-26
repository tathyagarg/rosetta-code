from PIL import Image

sand_pile = [
    [2, 0, 0, 0, 0, 0, 0],
    [0, 0, 12, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

class AbelianModel:
    def __init__(self, pile):
        self.pile = pile

    def flatten(self):
        c = []
        for row in self.pile:
            c.extend(row)
        return c

    def collapse(self):
        if all(i < 4 for i in self.flatten() if i):
            return self

        for ri, row in enumerate(self.pile):
            for ii, item in enumerate(row):
                if item >= 4:
                    each = item // 4
                    self.pile[ri + 1][ii] += each
                    self.pile[ri - 1][ii] += each
                    self.pile[ri][ii + 1] += each
                    self.pile[ri][ii - 1] += each
                    self.pile[ri][ii] = 0
        return self.collapse()

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.pile)

    def make_image(self, name: str = 'file.png'):
        with Image.new('HSV', (len(self.pile),)*2) as f:
            for i, val in enumerate(self.flatten()):
                print((50 - (10 * val), 75, 100))
                f.putpixel(divmod(i, len(self.pile)), (50 - (10 * val), 200, 255, 255))
        f = f.convert('RGB').resize((len(self.pile)*8,)*2, resample=Image.BOX)
        f.save(name)
def main():
    AbelianModel(sand_pile).make_image('before.png')
    AbelianModel(sand_pile).collapse().make_image('after.png')

if __name__ == "__main__""
    main()
    
