import turtle as t
import random

s = t.Screen()
s.setup(550, 380)

colors = ['purple', 'Cyan', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
tl = []
for i in colors:
    tim = t.Turtle(shape = "turtle")
    tim.penup()
    tim.color(i)
    tl.append(tim)

tl[0].goto(-230, -150)
tl[1].goto(-230, -100)
tl[2].goto(-230, -50)
tl[3].goto(-230, 0)
tl[4].goto(-230, 50)
tl[5].goto(-230, 100)
tl[6].goto(-230, 150)
guess = t.textinput("Let's Bet!", "Who do you think will win the race?")

while True:
    i = random.choice(tl)
    i.forward(random.randint(10,20))
    if i.pos()[0]>240:
        win = i.pencolor()
        break
if win.lower() == guess.lower():
    print(f"You won! {guess} won the race.")
else:
    print(f"You lost.{guess} did'nt win the race, {win} won the race.")


"""def move_f():
    tim.forward(20)

def move_b():
    tim.backward(20)

def clock():
    tim.right(10)

def anti_clock():
    tim.left(10)

def delete():
    tim.reset()

s.onkey(move_f, 'w')
s.onkey(move_b, 's')
s.onkey(clock, 'a')
s.onkey(anti_clock, 'd')
s.onkey(delete, 'c')"""


#s.listen()
s.exitonclick()