import turtle
from PIL import Image, EpsImagePlugin
from SAT import *
def printresult(result,X,Y,fr_y,C_r,C_b,match,rounds,num):


    x0 = -450
    y0 = 400

    w = 14
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(False)
    

    for r in range(rounds+1):
        for x in range(64):
            for y in range(5):
                t.up()
                t.goto(x * w + x0, -r * 12 * w - y * w + y0)
                t.down()
                t.pencolor("black")
                t.begin_fill()
                if r == 0:
                    if y == 0:
                        tt = [data(result,Y[r][x][1][0]), data(result,Y[r][x][1][1]), data(result,Y[r][x][1][2])]
                    else:
                        tt = [1, 1, 1]
                else:

                    tt = [data(result,X[r][x][y][0]), data(result,X[r][x][y][1]), data(result,X[r][x][y][2])]
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
                t.goto(x * w + x0, -r * 12 * w - y * w - 6 * w + y0)
                t.down()
                t.begin_fill()
                t.pencolor("black")
                tt = [data(result,Y[r][x][y][0]), data(result,Y[r][x][y][1]),data(result,Y[r][x][y][2])]
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
                    print("Y[" + str(r) + "][" + str(x) + "][" + str(y) + "]=" + str(tt))
                for i in range(4):
                    t.forward(w)
                    t.right(90)
                t.end_fill()
                t.up()
                t.forward(w)
                t.down()
    

    for r in range(rounds+1):
        for x in range(64):
            for y in range(5):
                t.up()
                t.goto(x * w + x0, -r * 12 * w - y * w + y0)
                t.down()
                if r >= 1:
                    if data(result,fr_y[r - 1][x][y]) == 1:
                        t.pencolor("yellow")
                        for i in range(4):
                            t.forward(w)
                            t.right(90)
        if r == rounds:
            for x in range(64):
                if data(result,match[x]) == 1:
                    t.pencolor("cyan")
                    t.up()
                    t.goto(x * w + x0-2, -r * 12 * w+ y0+2)
                    t.down()
                    for i in range(2):
                        t.forward(w+4)
                        t.right(90)
                        t.forward(5 * w+4)
                        t.right(90)
                    t.up()
    
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="Z_fig" + str(num) + ".eps")
    EpsImagePlugin.gs_windows_binary = r'E:\tool\gs\gs10.01.1\bin\gswin32c.exe'
    with open("Z_fig" + str(num) + ".eps", 'rb') as file:
        img = Image.open(file)
        img.save('R_fig' + str(num) + '.png')

    return 0


def print_condition(result,C_r,C_b,Y):
    count=0
    for x in range(64):
        for i in range(2):
            if data(result,C_r[x][i])==1:
                count+=1
            if data(result,C_b[x][i])==1:
                count+=1
    f=open("R_condition.txt", "w")
    print("条件数量为：",count)

    count=0
    for x in range(64):
        if [data(result,Y[x][0][0]),data(result,Y[x][1][0]),data(result,Y[x][3][0]),data(result,Y[x][4][0])]==[1,0,1,0] or [data(result,Y[x][0][1]),data(result,Y[x][1][1]),data(result,Y[x][3][1]),data(result,Y[x][4][1])]==[1,0,1,0]:
            f.write("$A_{\{ "+str(x)+","+str(1)+"\}}^{(0)} = 1,$")
            f.write("$A_{\{ "+str(x)+","+str(3)+"\}}^{(0)} + A_{\{ "+str(x)+","+str(4)+"\} }^{(0)} = 1$,")
            count += 2
        if [data(result,Y[x][0][0]),data(result,Y[x][1][0]),data(result,Y[x][3][0]),data(result,Y[x][4][0])]==[0,0,1,1] or [data(result,Y[x][0][1]),data(result,Y[x][1][1]),data(result,Y[x][3][1]),data(result,Y[x][4][1])]==[0,0,1,1]:
            f.write("$A_{\{ "+str(x)+","+str(1)+"\}}^{(0)} = 0$,")
            f.write("$A_{\{ "+str(x)+","+str(3)+"\}}^{(0)} + A_{\{ "+str(x)+","+str(4)+"\} }^{(0)} = 1$,")
            count += 2
        if [data(result,Y[x][0][0]),data(result,Y[x][1][0]),data(result,Y[x][3][0]),data(result,Y[x][4][0])]==[1,0,0,0] or [data(result,Y[x][0][1]),data(result,Y[x][1][1]),data(result,Y[x][3][1]),data(result,Y[x][4][1])]==[1,0,0,0]:
            f.write("$A_{\{ "+str(x)+","+str(1)+"\}}^{(0)} = 1$,")
            count += 1
        if [data(result,Y[x][0][0]),data(result,Y[x][1][0]),data(result,Y[x][3][0]),data(result,Y[x][4][0])]==[0,0,0,1] or [data(result,Y[x][0][1]),data(result,Y[x][1][1]),data(result,Y[x][3][1]),data(result,Y[x][4][1])]==[0,0,0,1]:
            f.write("$A_{\{ "+str(x)+","+str(1)+"\}}^{(0)} = 0$,")
            count += 1
        if [data(result,Y[x][0][0]),data(result,Y[x][1][0]),data(result,Y[x][3][0]),data(result,Y[x][4][0])]==[0,0,1,0] or [data(result,Y[x][0][1]),data(result,Y[x][1][1]),data(result,Y[x][3][1]),data(result,Y[x][4][1])]==[0,0,1,0]:
            f.write("$A_{\{ "+str(x)+","+str(3)+"\}}^{(0)} + A_{\{ "+str(x)+","+str(4)+"\} }^{(0)} = 1$,")
            count += 1
        if count>=4:
            count=0
            f.write("\n\\\\")
    f.close()

def print_DOF(result,fr,rounds):
    count=0
    for r in range(rounds):
        for x in range(64):
            for y in range(5):
                if data(result,fr[r][x][y])==1:
                    count+=1
    print("红色自由度消耗：",count)

def print_match(result,match,X,match_all):
    if match_all==None:
        match_all=[]
    t=[]
    for x in range(64):
        if data(result,match[x])==1:
            t.append(x)
    print("匹配器数量：",len(t))
    print("")
    print("match_all=",t+match_all)
    f = open("R_match.txt", "w")
    for x in range(64):
        if data(result, match[x]) == 1:
            t = "\\theta _{\{ x,0\} }^3 =& " \
                "\\textcolor{blue}{A_{\{ x,4\} }^3}\cdot " \
                "\\textcolor{blue}{A_{\{ x,1\} }^3}+ " \
                "\\textcolor{blue}{A_{\{ x,3\} }^3}+" \
                "\\textcolor{blue}{A_{\{ x,2\} }^3}\cdot " \
                "\\textcolor{blue}{A_{\{ x,1\} }^3} + \\\\& " \
                "\\textcolor{blue}{A_{\{ x,2\} }^3}+ " \
                "\\textcolor{blue}{A_{\{ x,1\} }^3} \cdot" \
                "\\textcolor{blue}{A_{\{ x,0\} }^3} +" \
                "\\textcolor{blue}{A_{\{ x,1\} }^3}+" \
                "\\textcolor{blue}{A_{\{ x,0\} }^3}\\\\"
            t=t.replace("x,",str(x)+",")
            for y in range(5):
                if [data(result, X[x][y][0]),data(result, X[x][y][1]),data(result, X[x][y][2])] == [0,1,1]:
                    t = t.replace("{blue}{A_{\{ " + str(x) + "," + str(y), "{red}{A_{\{ " + str(x) + "," + str(y))
                if [data(result, X[x][y][0]),data(result, X[x][y][1]),data(result, X[x][y][2])] == [1,1,1]:
                    t = t.replace("{blue}{A_{\{ "+str(x)+","+str(y),"{gray}{A_{\{ "+str(x)+","+str(y))
                if [data(result, X[x][y][0]),data(result, X[x][y][1]),data(result, X[x][y][2])] == [1,0,1]:
                    t = t.replace("{blue}{A_{\{ "+str(x)+","+str(y),"{blue}{A_{\{ "+str(x)+","+str(y))
                if [data(result, X[x][y][0]),data(result, X[x][y][1]),data(result, X[x][y][2])] == [0,0,1]:
                    t = t.replace("{blue}{A_{\{ " + str(x) + "," + str(y), "{green}{A_{\{ " + str(x) + "," + str(y))
            f.write(t+"\n")

    f.close()
    return 0

def print_start(result, Y,start_red,start_blue,rounds):
    t1=[];t2=[]
    for x in range(64):
        for y in range(5):
            if [data(result,Y[x][y][0]),data(result,Y[x][y][1]),data(result,Y[x][y][2])]==[1,0,1]:
                t1.append([x,y])
            elif [data(result,Y[x][y][0]),data(result,Y[x][y][1]),data(result,Y[x][y][2])]==[0,1,1]:
                t2.append([x, y])
    print("loc_B=",t1)
    print("loc_R=",t2)
    print("start_red=",start_red)
    print("start_blue=",start_blue)
    print("rounds=",rounds)


