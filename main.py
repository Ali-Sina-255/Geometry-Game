import turtle
from random import randint


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
    def __init__(self, point1: float, point2: float) -> None:
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        # got the the certain coordinates
        canvas.goto(self.point1.x, self.point1.y)
        # for darwing the
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def draw(self, canvas, size=10, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400))
)

# Print rectangle coordinates
print(
    "Rectangle Coordinates: ",
    rectangle.point1.x,
    ",",
    rectangle.point1.y,
    "and",
    rectangle.point2.x,
    ",",
    rectangle.point2.y,
)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
my_turtle = turtle.Turtle()
rectangle.draw(my_turtle)
print(rectangle.area())
user_point.draw(my_turtle)
turtle.done()
