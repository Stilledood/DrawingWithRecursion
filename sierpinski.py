import turtle

my_points = [[-200, -50], [50, 100], [200, -50]]
print(my_points[0][0],my_points[0][1])

def draw_triangle(points,t,color):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def find_middle(pointA,pointB):
    return (pointA[0]+pointB[0])/2,(pointA[1]+pointB[1])/2


def sierpinski(points,turtle,degree):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points,turtle,color_map[degree])
    if degree > 0:
        sierpinski([points[0],
                    find_middle(points[0],points[1]),
                    find_middle(points[0],points[2])],
                   turtle,
                   degree-1)
        sierpinski([points[1],
                    find_middle(points[0],points[1]),
                    find_middle(points[1],points[2])],
                    turtle,degree-1)
        sierpinski([points[2],
                    find_middle(points[2],points[1]),
                    find_middle(points[0],points[2])],turtle,degree-1)




t= turtle.Turtle()
my_win = turtle.Screen()
sierpinski(my_points,t,3)
my_win.exitonclick()



