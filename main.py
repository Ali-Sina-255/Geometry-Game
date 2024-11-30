class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y <= self.y <= rectangle.point2.y
        ):
            return True
        return False


class Rectangle:
    def __init__(self, rectangle) -> None:
        pass


class Rectangle:
    def __init__(self, point1: float, point2: float) -> None:
        self.point1 = point1
        self.point2 = point2
