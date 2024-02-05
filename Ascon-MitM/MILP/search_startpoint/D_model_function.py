

import turtle
from PIL import Image, EpsImagePlugin

def print_loc(Y):
    loc_R = []
    loc_B = []
    for x in range(64):
        for y in range(5):
            if [Y[x][y][0].X,Y[x][y][1].X]==[1,0]:
                loc_B.append([x,y])
            if [Y[x][y][0].X,Y[x][y][1].X]==[0,1]:
                loc_R.append([x,y])
    print("loc_R=",loc_R)
    print("loc_B=",loc_B)
    return 0

def printresult(m, X, Y, fr_y, match1, rounds, p_c):


    x0=-450
    y0=400

    w = 14
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(False)

    for r in range(rounds):
        for x in range(64):
            for y in range(5):
                t.up()
                t.goto(x * w + x0, -r * 12 * w - y * w + y0)
                t.down()
                t.pencolor("black")
                t.begin_fill()
                if r==0:
                    if y==0:
                        tt=[int(Y[r][x][1][0].X), int(Y[r][x][1][1].X), int(Y[r][x][1][2].X)]
                    else:
                        tt=[1,1,1]
                else:
                    tt = [int(X[r][x][y][0].X), int(X[r][x][y][1].X), int(X[r][x][y][2].X)]
                if tt == [1, 0, 1]:
                    t.fillcolor('blue')
                elif tt == [0, 1, 1]:
                    t.fillcolor('red')
                elif tt == [0, 0, 1]:
                    t.fillcolor('green')
                elif tt == [1, 1, 1]:
                    t.fillcolor('gray')
                elif tt == [0, 0, 0]:
                    t.fillcolor('white')
                else:
                    t.fillcolor('cyan')
                    print("X[" + str(r) + "][" + str(x) + "][" + str(y) + "]=" + str(tt))
                for i in range(4):
                    t.forward(w)
                    t.right(90)
                t.end_fill()


    for r in range(rounds):
        for x in range(64):
            for y in range(5):
                t.up()
                t.goto(x * w + x0, -r * 12 * w - y * w -6*w+ y0)
                t.down()
                t.begin_fill()
                t.pencolor("black")
                tt = [int(Y[r][x][y][0].X), int(Y[r][x][y][1].X),
                      int(Y[r][x][y][2].X)]
                if tt == [1, 0, 1]:
                    t.fillcolor('blue')
                elif tt == [0, 1, 1]:
                    t.fillcolor('red')
                elif tt == [0, 0, 1]:
                    t.fillcolor('green')
                elif tt == [1, 1, 1]:
                    t.fillcolor('gray')
                elif tt == [0, 0, 0]:
                    t.fillcolor('white')
                else:
                    t.fillcolor('cyan')
                    print("Y["+str(r)+"]["+str(x)+"]["+str(y)+"]="+str(tt))
                for i in range(4):
                    t.forward(w)
                    t.right(90)
                t.end_fill()
                t.up()
                t.forward(w)
                t.down()


    for r in range(rounds):
        for x in range(64):
            for y in range(5):
                t.up()
                t.goto(x * w + x0, -r * 12 * w - y * w + y0)
                t.down()
                if r >= 1:
                    if int(fr_y[r - 1][x][y].X) == 1:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
        if r == rounds:
            if int(match1[x].X) == 1:
                t.pencolor("cyan")
                t.up()
                t.goto(x * w + x0, -r * 12 * w+ y0)
                t.down()
                for i in range(2):
                    t.forward(w)
                    t.right(90)
                    t.forward(5 * w)
                    t.right(90)


    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="work" + str(p_c) + ".eps")
    EpsImagePlugin.gs_windows_binary = r'E:\tool\gs\gs10.01.1\bin\gswin32c.exe'
    with open("work" + str(p_c) + ".eps", 'rb') as file:
        img = Image.open(file)
        img.save('p' + str(p_c) + '.png')

def print_condition(C_r, C_b):
    count = 0;loc_cb1=[];loc_cb2=[]
    for i in range(64):
        if C_b[i][0].X == 1:
            loc_cb1.append(i)
            count += 1
        if C_b[i][1].X == 1:
            loc_cb2.append(i)
            count += 1
        if C_r[i][0].X == 1:
            count += 1
        if C_r[i][1].X == 1:
            count += 1
    print("loc_cb1=",loc_cb1)
    print("loc_cb2=",loc_cb2)
    print("condition_num=",count)
    return 0

def print_test(X,Y,match,rounds):
    for r in range(rounds):
        for x in range(64):
            if match[r][x].X==1:
                print(r,x)
