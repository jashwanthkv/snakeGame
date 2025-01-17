from turtle import Screen
import time
from body import Body
from food import Food
from score import Score
sc=Screen()
sc.bgcolor("black")
sc.setup(800,800)
b=Body()

sc.tracer(0)
f=Food()
s=Score()
sc.listen()
sc.onkey(b.up,"Up")
sc.onkey(b.down,"Down")
sc.onkey(b.l,"Left")
sc.onkey(b.r,"Right")

game=True
while game:
    sc.update()
    time.sleep(0.1)
    b.move()
    if(b.head.xcor()>=380 or b.head.ycor()<=-380 or b.head.xcor()<=-380 or b.head.ycor()>=380):
        game=False
        s.over()
        print("out")

    if b.head.distance(f) <=15:
        f.refresh()
        s.update()
        b.add_segment()
    for i in b.segments[1::]:
        if b.head.distance(i)<=10:
            game=False
            s.over()
            print("out")
























sc.exitonclick()