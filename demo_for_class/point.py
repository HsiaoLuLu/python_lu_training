# 類別 (class) -> 物件 (object)
# 這個行為被稱作實體化

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self):
        return((self.x)**2+(self.y)**2)**0.5

    def minus(self):
        return self.y - self.x

class Point_old:
    def __init__(self):
        pass

    def distance(self, x, y):
        return((x)**2+(y)**2)**0.5

    def minus(self, x, y):
        return y - x