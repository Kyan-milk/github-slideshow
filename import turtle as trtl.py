import turtle as trtl

score = 0 

font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000 
timer_up = False

def countdown():
  global timer, timer_up
  trtl.clear()
  if timer <= 0:
    trtl.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    trtl.penup()
    trtl.goto(100,100)
    trtl.pendown()
    trtl.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    trtl.getscreen().ontimer(countdown, counter_interval) 

import random as rand


spot = trtl.Turtle()
spot.shape("circle")

def size_change():
  spot.shapesize(rand.randint(1,7))

def number1():
  rand.randint(-200, 200)

def number2():
  rand.randint(-200, 200)

def change_position(x,y):
  spot.penup()
  spot.setposition(number1, number2)

def update_score_for_spot(x,y):
  global score
  score += 1
  print(score)

spot.onclick(change_position)
spot.onclick(size_change)
spot.onclick(update_score_for_spot)
trtl.write(score)
wn = trtl.Screen()
wn.bgcolor("yellow")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()