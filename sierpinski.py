import turtle

my_points = [[-100, -50], [0, 100], [100, -50]]
print(my_points[0][0],my_points[0][1])

def draw_triangle(points,t):
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


t= turtle.Turtle()
my_win = turtle.Screen()
t.color('green')
draw_triangle(my_points,t)
my_win.exitonclick()



