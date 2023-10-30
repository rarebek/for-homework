import turtle

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def move(self, x, y):
        pass

    def change_color(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        turtle.color(self.color)
        turtle.circle(self.radius)

    def move(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        turtle.color(self.color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
        turtle.end_fill()

    def move(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

circle = Circle("red", 50)
rectangle = Rectangle("blue", 100, 50)

circle.move(-100, 0)
circle.draw()

rectangle.move(100, 0)
rectangle.draw()

turtle.done()

##GPTda Turtle ishlatish uchun yordam so`raldi
