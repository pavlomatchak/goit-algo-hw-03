import turtle

def snowflake(t, order, size):
  if order == 0:
    t.forward(size)
  else:
    for angle in [60, -120, 60, 0]:
      snowflake(t, order - 1, size / 3)
      t.left(angle)

def draw(order, size=300):
  window = turtle.Screen()
  window.bgcolor("white")

  t = turtle.Turtle()
  t.speed(0)
  t.penup()
  t.goto(-size / 2, size / 2 / 3**0.5)
  t.pendown()

  for _ in range(3):
    snowflake(t, order, size)
    t.right(120)

  window.mainloop()

draw(2)
