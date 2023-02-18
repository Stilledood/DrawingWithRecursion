import turtle

def tree(branch_length,t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        tree(branch_length-20,t)
        t.left(40)
        tree(branch_length - 20, t)
        t.right(20)
        t.backward(branch_length)

t = turtle.Turtle()
my_win = turtle.Screen()
t.color('red')
t.left(90)
t.up()
t.backward(100)
t.down()
tree(100,t)
my_win.exitonclick()