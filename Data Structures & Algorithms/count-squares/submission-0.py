class CountSquares:

    def __init__(self):
        self.points = {}


    def add(self, point: List[int]) -> None:
        x, y = point
        if y not in self.points:
            self.points[y] = {}
        if x not in self.points[y]:
            self.points[y][x] = 0
        self.points[y][x] +=1

    def count(self, point: List[int]) -> int:
        r = 0
        x, y = point
        for x2, freq in self.points.get(y, {}).items():
            if x2 == x:
                continue
            dist = abs(x - x2)
            r += freq * self.points.get(y+dist, {}).get(x, 0) * self.points.get(y+dist, {}).get(x2, 0)
            r += freq * self.points.get(y-dist, {}).get(x, 0) * self.points.get(y-dist, {}).get(x2, 0)
        return r
