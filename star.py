import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
spiral.speed(20)
sc.bgcolor('black')
col=['yellow','blue','white','green']
c=0
for i in range(60):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c==3:
            c+=1
            turtle.done