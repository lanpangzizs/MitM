import gurobipy as gp
from gurobipy import GRB
import turtle
from PIL import Image, EpsImagePlugin
from functools import reduce
import time
gama = [[0, 36, 3, 41, 18],
        [1, 44, 10, 45, 2],
        [62, 6, 43, 15, 61],
        [28, 55, 25, 21, 56],
        [27, 20, 39, 8, 14]
        ]



def variable_1(m,x,n):
    X=[]
    for i in range(x):
        X.append(n+i)
    return [X,n+x]
def variable_2(m,x,y,n):
    X=[]
    for i in range(x):
        X.append([])
        for j in range(y):
            X[i].append(n+j+i*y)
    return [X,n+x*y]
def variable_3(m,x,y,z,n):
    X=[]
    for i in range(x):
        X.append([])
        for j in range(y):
            X[i].append([])
            for k in range(z):
                X[i][j].append(n+k+j*z+i*y*z)
    return [X,n+x*y*z]
def variable_4(m,x1,x2,x3,x4,n):
    X=[]
    for i1 in range(x1):
        X.append([])
        for i2 in range(x2):
            X[i1].append([])
            for i3 in range(x3):
                X[i1][i2].append([])
                for i4 in range(x4):
                    X[i1][i2][i3].append(n+i4+i3*x4+i2*x3*x4+i1*x2*x3*x4)
    return [X,n+x1*x2*x3*x4]
def variable_5(m,x1,x2,x3,x4,x5,n):
    X=[]
    for i1 in range(x1):
        X.append([])
        for i2 in range(x2):
            X[i1].append([])
            for i3 in range(x3):
                X[i1][i2].append([])
                for i4 in range(x4):
                    X[i1][i2][i3].append([])
                    for i5 in range(x5):
                        X[i1][i2][i3][i4].append(n+i5+i4*x5+i3*x4*x5+i2*x3*x4*x5+i1*x2*x3*x4*x5)
    return [X,n+x1*x2*x3*x4*x5]


def create_variable(m,rounds,num):
    [S,num]= variable_4(m, 5, 5, 64, 2,num)
    [X,num] = variable_5(m, rounds + 1, 5, 5, 64,3,num)
    [C,num] = variable_4(m, rounds, 5, 64, 2,num)
    [D,num] = variable_4(m, rounds, 5, 64, 2,num)
    [Y,num] = variable_5(m, rounds, 5, 5, 64, 3,num)
    [condition,num]=variable_3(m,4,5,64,num)
    [fr_c,num] = variable_3(m, rounds, 5, 64,num)
    [fr_d,num] = variable_3(m, rounds, 5, 64,num)
    [fr_y,num] = variable_4(m, rounds, 5, 5, 64,num)
    [match1,num]=variable_1(m,64,num)
    [match2,num]=variable_1(m,64,num)
    return [S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,num]


def constr(m,X,Y):
    for j in range(len(Y)):
        T = []
        for i in range(len(Y[j])):
            if Y[j][i]==1:
                T.append(X[i])
            if Y[j][i]==-1:
                T.append(-X[i])
        m.append(T)


def f_data1(result,X,r,x,z):
    for y in range(5):
        if result[X[r][x][y][z][1]]<0:
            return 0
    return 1

def f_data2(result,X,r,x,z):
    for y in range(5):
        if result[X[r][(x-1)%5][y][z][1]]<0:
            return 0
        if result[X[r][(x+1)%5][y][(z-1)%64][1]]<0:
            return 0
    return 1

def data_f(result,Y):
    X=[result[Y[0]],result[Y[1]],result[Y[2]]]
    if X[0]>0 and X[1]<0 and X[2]>0:
        return [1,0,1]
    if X[0]<0 and X[1]>0 and X[2]>0:
        return [0,1,1]
    if X[0]<0 and X[1]<0 and X[2]>0:
        return [0,0,1]
    if X[0]>0 and X[1]>0 and X[2]>0:
        return [1,1,1]
    if X[0]<0 and X[1]<0 and X[2]<0:
        return [0,0,0]

def data(result,Y):
    if result[Y]>0:
        return 1
    if result[Y]<0:
        return 0


def printresult(result,rounds,S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,L1,L3):

    w=11

    start_x=-400+10*w;start_y=400-w*22-w/2

    Y0=[];Z0=[]

    for x in range(5):
        t0=[]
        for y in range(5):
            t1=[]
            for z in range(64):
                t2=[data(result,S[x][y][z][0]),data(result,S[x][y][z][1])]+[1]
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
                    if result[condition[x][y][z]]>0:
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
                        tt = data_f(result,X[r][x][y][z])
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
                    tt = [data(result,C[r][x][z][0]),f_data1(result,X,r,x,z),data(result,C[r][x][z][1])]
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
                    tt = [data(result,D[r][x][z][0]),f_data2(result,X,r,x,z),data(result,D[r][x][z][1])]
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
                        tt = data_f(result,Y[r][x][y][z])
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
                        tt = data_f(result,Y[r][L1[x*320+64*y+z][0]][L1[x*320+64*y+z][1]][L1[x*320+64*y+z][2]])
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
                    if result[fr_c[r][x][z]]>0:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")

                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + x * w, start_y - 8 * w - r * 22 * w)
                    t.down()
                    if result[fr_d[r][x][z]]>0:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
                        t.pencolor("black")

                    for y in range(5):
                        t.up()
                        t.goto(start_x + (z % 8) * 6 * w+x*w, -y * w + start_y - 10 * w - r * 22 * w)
                        t.down()
                        if result[fr_y[r][x][y][z]] > 0:
                            t.pencolor("yellow")
                            for i in range(4):
                                t.forward(w)
                                t.right(90)
                            t.pencolor("black")


        for r in range(rounds):
            for z in range(0 + p_c * 8, 8 + p_c * 8):
                if result[match1[(z+gama[3][0])%64]]>0:
                    t.pencolor("cyan")
                    t.up()
                    t.goto(start_x + (z % 8) * 6 * w + 3 * w, start_y - rounds * 22 * w)
                    t.down()
                    for i in range(4):
                        t.forward(w)
                        t.right(90)
                if result[match2[(z + gama[4][1])%64]] >0 :
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

    x=1;y=0;z=1
    print(L3[x*320+y*64+z])

    eq=[];C=[]

    for x in range(4):
        for y in range(5):
            for z in range(64):
                if result[condition[x][y][z]]>0:
                    if x!=3:
                        eq.append(str(L1[x*320+y*64+z]))
                    else:
                        eq.append(str(L1[4 * 320 + y * 64 + z]))

    for x in range(5):
        for z in range(64):
            if Z0[x][0][z][0]+Z0[x][0][z][1]==1:
                C.append([x,0,z])

    f=open("eq.txt", "w")
    for i in eq:
        f.write(i+"\n")
    f.close()

    f=open("C.txt", "w")
    for i in C:
        f.write(str(i)+"\n")
    f.close()



def multiply(a, b):
    return a * b



def data_transform(result,Y):
    X=[result[i]for i in Y]
    a=[]
    for i in X:
        if i>0:
            a.append(1)
        else:
            a.append(0)
    return a

def  print_condition(D2):
    f=open("condition.txt","w")
    t=[]
    for x in range(4):
        for y in range(3):
            for z in range(32):
                if D2[x][y][z][1].X==1:
                    t.append([x,y,z,int(D2[x][y][z][2].X)])
                    f.write("Z0"+str([x,y,z])+"=")
                    f.write(str(int(D2[x][y][z][2].X))+"\n")
    f.close()
    t2=[]
    for i in t:
        if i[1]==0:
            t2.append(i)
        if i[1]==1:
            t2.append([(i[0]-1)%4,i[1],i[2],i[3]])
        if i[1]==2:
            t2.append([i[0],i[1],(i[2]-11)%32,i[3]])
    t1=t2;t3=[];t4=[]
    for i in t1:
        t3.append([(i[0]-1)%4,(i[2]-5)%32])
        t4.append([(i[0]-1)%4,(i[2]-14)%32])
    f=open("condition2.txt","w")
    for i in range(len(t1)):
        f.write("X0"+str(t1[i][0:3]))
        f.write("+")
        for j in range(3):
            f.write("X0" + str([t3[i][0],j,t3[i][1]]))
            f.write("+")
        for j in range(3):
            f.write("X0" + str([t4[i][0],j,t4[i][1]]))
            if j!=2:
                f.write("+")
        f.write("="+str(t1[i][3])+"\n")

def print_match(result,match1,match2):
    t1=[];t2=[]
    rounds=3
    for z in range(64):
        if result[match1[z]]>0:
            t1.append(z)
            print("&\\textcolor{green}{A_{\{ 3,0,"+str((z -gama[3][0])%64)+"\}}^{(3)}} \oplus \\textcolor{green}{A_{\{ 3,3,"+str((z - gama [3][0])%64)+"\}}^{(3)}} \oplus (A_{\{ 1,1,"+str(z)+"\}}^{(4)} \oplus 1) \cdot \\textcolor{green}{(A_{\{ 0,2,"
                  +str((z -gama[0][2])%64)+"\}}^{(3)}} \oplus \\textcolor{green}{A_{\{ 0,0,"+str((z -gama [0][2])%64)+"\}}^{(3)}})\\\\"
                  +"=&A_{\{ 0,1,"+str(z)+"\}}^{(4)} \oplus \\theta _{\{ 4,4,"+str((z - gama [4][1])%64)+"\}}^{(3)} \oplus (A_{\{ 1,1,"
                                           +str(z)+"\}}^{(4)} \oplus 1) \cdot \\theta _{\{ 0,0,"+str((z - gama [0][2])%64)+"\}}^{(3)}\\\\")
        if result[match2[z]] > 0:
            t2.append(z)
            print("&\\textcolor{green}{A_{\{ 4,1," + str((z - gama[4][1])%64) + "\}}^{(3)}} \oplus \\textcolor{green}{A_{\{ 4,4," + str((z - gama[4][1])%64) + "\}}^{(3)}} \oplus (A_{\{ 2,1," + str(z) + "\}}^{(4)} \oplus 1) \cdot \\textcolor{green}{(A_{\{ 1,3,"
                  + str((z - gama[1][3])%64) + "\}}^{(3)}} \oplus \\textcolor{green}{A_{\{ 1,1," + str(z - gama[1][3]) + "\}}^{(3)}})\\\\"
                  + "=&A_{\{ 1,1," + str(z) + "\}}^{(4)} \oplus \\theta _{\{ 4,4," + str((z - gama[4][1])%64) + "\}}^{(3)} \oplus (A_{\{ 2,1,"
                  + str(z) + "\}}^{(4)} \oplus 1) \cdot \\theta _{\{ 1,1," + str((z - gama[1][3])%64) + "\}}^{(3)}\\\\")
    print("match1_find=", t1)
    print("match2_find=", t2)
def print_start(X):
    f=open("start.txt","w")
    f.write("red：")
    for x in range(4):
            for z in range(32):
                if [X[0][x][2][z][i].X for i in range(3)]==[0,1,1]:
                    f.write("X0"+str([x])+str([2])+str([z])+" ")
    f.write("\nblue：")
    for x in range(4):
            for z in range(32):
                if [X[0][x][2][z][i].X for i in range(3)]==[1,0,1]:
                    f.write(str([x,2,z])+",")






