ths = [1, 2, 4, 2, 0, 1, 3, 1, 2]
peaks = []


class Tower:
    def __init__(self, height, index):
        self.height = height
        self.index = index


for index, tower in enumerate(ths):
    tower = Tower(tower, index)
    print(tower.height, tower.index)
    print(tower.peak(tower, index))
