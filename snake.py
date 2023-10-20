from turtle import  Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #capitalized cuz cte
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.new_snake=[]
        self.create_snake()
        self.head= self.new_snake[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)


    def add_segment(self,i):
        snake = Turtle("square")
        snake.color("pink")
        snake.penup()
        snake.goto(i)
        self.new_snake.append(snake)

    def reset(self):
        for seg in self.new_snake:
            seg.goto(1000,1000)
        self.new_snake.clear()
        self.create_snake()
        self.head=self.new_snake[0]
    def extend(self):
        self.add_segment(self.new_snake[-1].position())
    def move(self):
            for i in range(len(self.new_snake) - 1, 0, -1):
                new_x = self.new_snake[i - 1].xcor()
                new_y = self.new_snake[i - 1].ycor()
                self.new_snake[i].goto(new_x, new_y)
            self.new_snake[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

