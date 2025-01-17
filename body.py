from turtle import Turtle

# Constants for snake creation
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_COLOR = "white"
SEGMENT_SHAPE = "square"

class Body(Turtle):
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position=None):
       if position is None:
            last_segment = self.segments[-1]
            x, y = last_segment.position()
            heading = last_segment.heading()
            if heading == 0:
                position = (x - 20, y)
            elif heading == 180:
                position = (x + 20, y)
            elif heading == 90:
                position = (x, y - 20)
            elif heading == 270:
                position = (x, y + 20)
       segment = Turtle(shape=SEGMENT_SHAPE)
       segment.penup()
       segment.color(SEGMENT_COLOR)
       segment.shapesize(1, 1)
       segment.goto(position)
       self.segments.append(segment)

    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def l(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def r(self):

        if self.head.heading() != 180:
            self.head.setheading(0)
