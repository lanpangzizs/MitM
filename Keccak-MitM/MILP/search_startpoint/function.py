import gurobipy as gp
from gurobipy import GRB
import turtle
from PIL import Image, EpsImagePlugin
gama = [[0, 36, 3, 41, 18],
        [1, 44, 10, 45, 2],
        [62, 6, 43, 15, 61],
        [28, 55, 25, 21, 56],
        [27, 20, 39, 8, 14]
        ]


def variable_1(m,R):
    X = []
    for r in range(R):
        X.append(m.addVar(vtype=GRB.BINARY))
    return X
def variable_2(m,R,x):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t.append(m.addVar(vtype=GRB.BINARY))
        X.append(t)
    return X
def variable_3(m,R,x,y):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t1.append(m.addVar(vtype=GRB.BINARY))
            t.append(t1)
        X.append(t)
    return X
def variable_4(m,R,x,y,z):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t2 = []
                for k in range(z):
                    t2.append(m.addVar(vtype=GRB.BINARY))
                t1.append(t2)
            t.append(t1)
        X.append(t)
    return X
def variable_5(m,R,x,y,z,d):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t2 = []
                for k in range(z):
                    t3 = []
                    for l in range(d):
                        t3.append(m.addVar(vtype=GRB.BINARY))
                    t2.append(t3)
                t1.append(t2)
            t.append(t1)
        X.append(t)

    return X

def create_variable(m,rounds):
    S = variable_4(m, 5, 5, 64, 2)
    X = variable_5(m, rounds + 1, 5, 5, 64, 3)
    C = variable_4(m, rounds, 5, 64, 2)
    D = variable_4(m, rounds, 5, 64, 2)
    Y = variable_5(m, rounds, 5, 5, 64, 3)
    condition=variable_3(m,4,5,64)
    fb_0 = variable_3(m, 5, 5, 64)
    fr_0 = variable_3(m, 5, 5, 64)
    fr_c = variable_3(m, rounds, 5, 64)
    fr_d = variable_3(m, rounds, 5, 64)
    fr_y = variable_4(m, rounds, 5, 5, 64)
    match1=variable_1(m,64)
    match2=variable_1(m,64)
    return [S,X,C,D,Y,fb_0,fr_0,fr_c,fr_d,fr_y,match1,match2,condition]

def constr(m,x,eq):
    for i in range(len(eq)):
        t = gp.LinExpr()
        for j in range(len(x)):
            t+=x[j]*eq[i][j]
        t+=eq[i][len(x)]
        m.addConstr(t>=0)
    return m


def f_data1(X,r,x,z):
    for y in range(5):
        if X[r][x][y][z][1].X==0:
            return 0
    return 1

def f_data2(X,r,x,z):
    for y in range(5):
        if X[r][(x-1)%5][y][z][1].X==0:
            return 0
        if X[r][(x+1)%5][y][(z-1)%64][1].X==0:
            return 0
    return 1

def printresult(m,rounds,S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,L1,L3):

    w=15

    start_x=-450;start_y=400-w*22

    Y0=[];Z0=[];C0=[];D0=[]

    for x in range(5):
        t0=[]
        for y in range(5):
            t1=[]
            for z in range(64):
                t2=[S[x][y][z][i].X for i in range(2)]+[1]
                t1.append(t2)
            t0.append(t1)
        Y0.append(t0)

    for x in range(5):
        t0=[]
        for y in range(5):
            t1=[]
            for z in range(64):
                t2=[]
                for i in range(3):
                    t2.append(Y0[L3[x*320+y*64+z][0]][L3[x*320+y*64+z][1]][L3[x*320+y*64+z][2]][i])
                t1.append(t2)
            t0.append(t1)
        Z0.append(t0)


    for p_c in range(8):
        t = turtle.Turtle()
        t.speed(0)
        turtle.tracer(False)
        turtle.screensize(10000,8000, "white")

        for z in range(0 + p_c * 8, 8 + p_c * 8):
            for y in range(5):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, -y * w + start_y + 22 * w)
                    t.down()
                    t.begin_fill()
                    tt = [Z0[x][y][z][i] for i in range(3)]
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y + 16 * w)
                    t.down()
                    tt = [1,1,1]
                    t.begin_fill()
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()

                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y + 16 * w)
                    t.down()
                    if Z0[x][0][z][0]==0:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")
                    elif Z0[x][0][z][1]==0:
                        t.pencolor("blue")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y + 14 * w)
                    t.down()
                    t.begin_fill()
                    tt = [1,1,1]
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()
                    t.up()
                    t.forward(w)
                    t.down()


        for z in range(0 + p_c * 8, 8 + p_c * 8):
            for y in range(5):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, -y * w + start_y + 12 * w)
                    t.down()
                    t.begin_fill()
                    tt = [Z0[x][y][z][i] for i in range(3)]
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()


        for z in range(0 + p_c * 8, 8 + p_c * 8):
            for y in range(5):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y +6*w)
                    t.down()
                    t.begin_fill()
                    tt = [Y0[x][y][z][i] for i in range(3)]
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()


        for z in range(0 + p_c * 8, 8 + p_c * 8):
            for y in range(5):
                for x in range(4):
                    if condition[x][y][z].X==1:
                        t.up()
                        if x!=3:
                            t.goto(start_x + (z % 8) * 6 * w + x * w+w/2, -y * w + start_y + 6 * w-w*3/4)
                        else:
                            t.goto(start_x + (z % 8) * 6 * w + x * w + w / 2+w, -y * w + start_y + 6 * w - w * 3 / 4)
                        t.down()
                        if x in [0,3]:
                            t.write("1", move=False, align='center', font=('Times New Roman', 10, 'normal'))
                        else:
                            t.write("0", move=False, align='center', font=('Times New Roman', 10, 'normal'))

        for r in range(rounds + 1):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for y in range(5):
                    for x in range(5):
                        t.up()
                        t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y - r * 22 * w)
                        t.down()
                        t.begin_fill()
                        tt = [X[r][x][y][z][i].X for i in range(3)]
                        if tt == [1, 0, 1]:
                            t.fillcolor('blue')
                        if tt == [0, 1, 1]:
                            t.fillcolor('red')
                        if tt == [0, 0, 1]:
                            t.fillcolor('green')
                        if tt == [1, 1, 1]:
                            t.fillcolor('gray')
                        if tt == [0, 0, 0]:
                            t.fillcolor('white')
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.end_fill()


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w+x*w, start_y - 6 * w - r * 22 * w)
                    t.down()
                    tt = [C[r][x][z][0].X,f_data1(X,r,x,z),C[r][x][z][1].X]
                    t.begin_fill()
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w+x*w, start_y - 8 * w - r * 22 * w)
                    t.down()
                    t.begin_fill()
                    tt = [D[r][x][z][0].X ,f_data2(X,r,x,z),D[r][x][z][1].X]
                    if tt == [1, 0, 1]:
                        t.fillcolor('blue')
                    if tt == [0, 1, 1]:
                        t.fillcolor('red')
                    if tt == [0, 0, 1]:
                        t.fillcolor('green')
                    if tt == [1, 1, 1]:
                        t.fillcolor('gray')
                    if tt == [0, 0, 0]:
                        t.fillcolor('white')
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                    t.end_fill()
                    t.up()
                    t.forward(w)
                    t.down()

        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for y in range(5):
                    for x in range(5):
                        t.up()
                        t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y - 10 * w - r * 22 * w)
                        t.down()
                        t.begin_fill()
                        tt = [Y[r][x][y][z][i].X for i in range(3)]
                        if tt == [1, 0, 1]:
                            t.fillcolor('blue')
                        if tt == [0, 1, 1]:
                            t.fillcolor('red')
                        if tt == [0, 0, 1]:
                            t.fillcolor('green')
                        if tt == [1, 1, 1]:
                            t.fillcolor('gray')
                        if tt == [0, 0, 0]:
                            t.fillcolor('white')
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.end_fill()
                        t.up()
                        t.forward(w)
                        t.down()

        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for y in range(5):
                    for x in range(5):
                        t.up()
                        t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y - 16 * w - r * 22 * w)
                        t.down()

                        t.begin_fill()
                        tt = [Y[r][L1[x*320+64*y+z][0]][L1[x*320+64*y+z][1]][L1[x*320+64*y+z][2]][i].X for i in range(3)]
                        if tt == [1, 0, 1]:
                            t.fillcolor('blue')
                        if tt == [0, 1, 1]:
                            t.fillcolor('red')
                        if tt == [0, 0, 1]:
                            t.fillcolor('green')
                        if tt == [1, 1, 1]:
                            t.fillcolor('gray')
                        if tt == [0, 0, 0]:
                            t.fillcolor('white')
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.end_fill()


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                for x in range(5):
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y - 6 * w - r * 22 * w)
                    t.down()
                    if fr_c[r][x][z].X==1:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")

                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y - 8 * w - r * 22 * w)
                    t.down()
                    if fr_d[r][x][z].X==1:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")

                    for y in range(5):
                        t.up()
                        t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y - 10 * w - r * 22 * w)
                        t.down()
                        if fr_y[r][x][y][z].X == 1:
                            t.pencolor("yellow")
                            for i in range(4):
                                t.forward(w)
                                t.right(90)
                            t.pencolor("black")


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                if match1[(z+gama[3][0])%64].X==1:
                    t.pencolor("cyan")
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + 3 * w, start_y - rounds * 22 * w)
                    t.down()
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                if match2[(z + gama[4][1])%64].X == 1:
                    t.pencolor("cyan")
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + 4 * w,-w+start_y - rounds * 22 * w)
                    t.down()
                    for i in range(4):
                        t.forward(w)
                        t.right(90)

        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="work_z" + str(p_c*8)+"-z" +str(p_c*8+7) + ".eps")
        EpsImagePlugin.gs_windows_binary = r'E:\tool\gs\gs10.01.1\bin\gswin32c.exe'
        with open("work_z" + str(p_c*8)+"-z" +str(p_c*8+7)+".eps", 'rb') as file:
            img = Image.open(file)
            img.save("p_z" + str(p_c*8)+"-z" +str(p_c*8+7)+ '.png')


def print_weak(m,rounds,S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,L1,L3):
    t=[]
    for x in range(5):
        for y in range(5):
            for z in range(64):
                if [S[x][y][z][0].X,S[x][y][z][1].X]==[1,0]:
                    t.append([x,y,z])
    print("loc_B=",t)

    t=[]
    for x in range(5):
        for y in range(5):
            for z in range(64):
                if [S[x][y][z][0].X,S[x][y][z][1].X]==[0,1]:
                    t.append([x,y,z])
    print("loc_R=",t)

    t=[]
    for x in range(4):
        for y in range(5):
            for z in range(64):
                if condition[x][y][z].X==1:
                    t.append([x,y,z])
    print("loc_condition=", t)
