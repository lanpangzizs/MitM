from SAT import *

def set_variable(num,rounds,X,Y,fr_y,match,C_r,C_b):
    num = variable_4(X,rounds+1,64,5, 3, num)
    num = variable_4(Y,rounds,64,5, 3, num)
    num = variable_3(fr_y, rounds, 64,5,num)
    num = variable_1(match, 64, num)
    num = variable_2(C_r,64,2,num)
    num = variable_2(C_b,64,2,num)
    return num

def set_start(m,num,X,start,C_r,C_b,stat_red,stat_blue):
    for x in range(64):
        if x==62 or x==63:
            for y in range(5):
                for i in range(3):
                    start.append(X[x][y][i])
        else:

            eq = [[0, 0, 1, 0, 0, -1], [0, -1, 1, 0, 0, 0], [0, -1, 0, 0, -1, 0], [0, 0, -1, 1, 1, 0], [-1, 0, 0, -1, 0, -1], [1, 0, 0, 1, 0, -1], [-1, 1, 0, 0, 1, 0], [1, 0, 0, -1, 1, 0], [-1, 1, 0, -1, 0, 0], [1, 0, 1, 1, -1, 0], [0, 1, -1, -1, 0, 1], [-1, 0, -1, 0, -1, 1]]
            constr(m,[X[x][0][0],X[x][1][0],X[x][3][0],X[x][4][0],C_r[x][0],C_r[x][1]],eq)
            constr(m,[X[x][0][1],X[x][1][1],X[x][3][1],X[x][4][1],C_b[x][0],C_b[x][1]],eq)
            for i in range(2):
                start.append(X[x][2][i])


        for y in range(5):
            eq = [[1, 1]]
            constr(m,[X[x][y][0],X[x][y][1]],eq)
            start.append(X[x][y][2])

    num=less_count_0(m,num,start,[X[x][1][0] for x in range(64)],stat_red ,1)
    num=less_count_0(m,num,start,[X[x][1][1] for x in range(64)],stat_blue,1)
    return num

def set_value(X,loc_R,loc_B,loc_cb1,loc_cb2,start,num,mode,C_b):
    if mode==1:
        for x in range(64):
            for y in range(5):
                if [x,y] in loc_B:
                    start.append(X[x][y][0])
                    start.append(-X[x][y][1])
                elif [x, y] in loc_R:
                    start.append(-X[x][y][0])
                    start.append(X[x][y][1])
                else:
                    start.append(X[x][y][0])
                    start.append(X[x][y][1])
    if mode==2:
        for x in range(64):
            if x in loc_cb1:
                start.append(C_b[x][0])
            if x in loc_cb2:
                start.append(C_b[x][1])
            for y in range(5):
                if [x,y] in loc_B:
                    start.append(X[x][y][0])
                    start.append(-X[x][y][1])
    return num

def set_condition(m,num,start,C_r,C_b,condition_num):
    num=less_count(m,num,start,[j for i in C_r for j in i]+[j for i in C_b for j in i],condition_num,0)
    return num

def set_DOF(m,num,start,DOF,fr):
    num=less_count(m,num,start,[k for i in fr for j in i for k in j],DOF,0)
    return num

def set_match(m,X,match1):
    for x in range(64):
        eq=[[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, 0, 1, 1, -1, 0, 0, 0, -1, 0, -1, -1, -1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, 1, 0, 0, -1, 0, 1, 0, -1, 0, -1, -1, -1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, 1, 0, 1, -1, 0, 0, 0, -1, 0, -1, -1, -1, 1], [0, -1, 0, 0, 1, 0, -1, 0, 0, 1, -1, 0, -1, -1, -1, 1], [0, 0, 0, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, -1, 0, 1], [1, -1, -1, -1, 0, 0, -1, 0, 0, 1, -1, 0, 0, 0, -1, 1], [0, -1, -1, -1, 1, 0, -1, 0, 1, 0, -1, 0, 0, 0, -1, 1], [1, -1, -1, -1, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, -1, 1], [0, -1, 0, 1, -1, -1, -1, -1, 0, 1, 0, 0, 0, -1, 0, 1], [0, -1, -1, 1, 0, 0, -1, 1, -1, 0, -1, 0, 0, 0, -1, 1], [0, -1, 1, 0, 0, 0, -1, -1, -1, 1, -1, 0, 0, 0, -1, 1], [0, -1, 1, 0, 0, 0, -1, -1, 1, 0, -1, 0, 0, -1, -1, 1], [0, -1, 1, 0, 0, 0, -1, 1, -1, -1, -1, 0, -1, 0, 0, 1], [0, -1, 1, 0, -1, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1], [0, -1, 1, 0, -1, 1, -1, -1, -1, 0, -1, 0, 0, 0, 0, 1], [-1, -1, -1, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 1], [0, -1, 0, -1, 1, 0, -1, 1, 0, -1, -1, 0, -1, 0, 0, 1], [0, 1, 0, -1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0, 1], [1, -1, -1, 0, 0, 0, -1, 1, -1, -1, -1, 0, 0, 0, 0, 1], [1, -1, -1, 0, 0, 1, -1, 0, -1, -1, -1, 0, 0, 0, 0, 1], [-1, 1, -1, 0, -1, -1, 1, -1, -1, -1, 0, -1, 0, 0, 0, 1], [-1, 1, -1, -1, -1, -1, 1, -1, 0, -1, 0, -1, 0, 0, 0, 1], [-1, 0, -1, 1, -1, -1, 0, -1, 1, -1, 0, -1, 0, -1, 0, 1]]
        constr(m,[X[x][y][0]for y in range(5)]+[X[x][y][1]for y in range(5)]+[X[x][y][2]for y in range(5)]+[match1[x]],eq)

def conunt_match(m,num,start,match,M,match_all):
    t=[]
    if match_all==None:
        match_all=[]
    for x in range(64):
        if x not in match_all:
            t.append(match[x])
    num = less_count(m, num, start,t, M, 1)
    return num

def f1(m,X,Y,rounds):
    for r in range(1,rounds):
        for x in range(64):

            for y in range(5):
                if y ==0:#b0 = a4a1 + a3 + a2a1 + a2 + a1a0 + a1 + a0
                    eq=eq=[[0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 1, -1], [0, 1, 1, 0, 0, 0, -1], [1, 0, 0, 1, 0, 0, -1], [0, 0, -1, -1, -1, -1, 1], [-1, 0, -1, 0, -1, -1, 1], [-1, -1, 0, 0, -1, -1, 1], [0, -1, 0, -1, -1, -1, 1]]
                    constr(m,[X[r][x][1][k] for k in range(2)]+[X[r][x][2][k] for k in range(2)]+[Y[r][x][4][2]]+[X[r][x][0][2]] + [Y[r][x][y][2]],eq)
                if y ==1:#b1 = a4 + a3a2 + a3a1 + a3 + a2a1 + a2 + a1 + a0
                    eq=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, -1], [0, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, -1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 1, 1, 0, 0, 0, 0, -1, 0, 0, -1, -1], [-1, 0, -1, 0, -1, 0, -1, -1, -1, -1, -1, 1], [0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1], [0, -1, 1, 0, 0, 1, 0, -1, 0, -1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][1][k] for k in range(2)] + [X[r][x][2][k] for k in range(2)] + [X[r][x][3][k] for k in range(2)] + [X[r][x][k][2] for k in range(5)] + [Y[r][x][y][2]], eq)
                if y==2:#b2 = a4a3 + a4 + a2 + a1 + 1
                    eq=[[0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, -1], [0, -1, 0, -1, -1, -1, -1, -1, 1], [0, 0, 0, 0, -1, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, -1], [-1, 0, -1, 0, -1, -1, -1, -1, 1], [1, 0, 0, 1, 0, 0, 0, 0, -1], [-1, -1, 0, 0, -1, -1, -1, -1, 1], [0, 1, 1, 0, -1, 0, -1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][3][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(1,5)] + [Y[r][x][y][2]], eq)
                if y==3: #b3 = a4a0 + a4 + a3a0 + a3 + a2 + a1 + a0
                    eq=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, 1], [-1, 1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 1], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1], [1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][0][k] for k in range(2)] + [X[r][x][3][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(5)] + [Y[r][x][y][2]], eq)
                if y==4:#b4 = a4a1 + a4 + a3 + a1a0 + a1
                    eq=[[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1], [0, 0, -1, -1, 0, 0, -1, -1, -1, -1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1], [1, 0, 0, 1, 0, 0, 0, 0, -1, 0, -1], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, -1], [0, -1, 0, -1, 0, -1, -1, -1, -1, -1, 1], [-1, -1, 0, 0, -1, -1, -1, -1, -1, -1, 1], [-1, 0, -1, 0, -1, 0, -1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][0][k] for k in range(2)] + [X[r][x][1][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(2)] +[X[r][x][k][2] for k in range(3,5)]+ [Y[r][x][y][2]], eq)


            for k in range(5):
                if k==0 or k==1 or k==3:
                    eq = [[1, 0, -1], [0, 1, -1], [-1, -1, 1]]
                    constr(m, [X[r][x][0][0] , Y[r][x][2][0] , Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][0][1] , Y[r][x][2][1] , Y[r][x][k][1]], eq)
                if k==2:
                    eq=[[0, 0, 1, 0, -1], [0, 1, -1, 0, -1], [1, 0, -1, 0, -1], [-1, 0, 0, 1, -1], [-1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][y][0] for y in range(1, 5)] + [Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][y][1] for y in range(1, 5)] + [Y[r][x][k][1]], eq)
                if k==4:
                    eq =[[0, 0, 1, 0, -1], [0, 1, -1, 0, -1], [1, 0, -1, 0, -1], [-1, 0, 0, 1, -1], [-1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][y][0] for y in range(2)] + [X[r][x][y][0] for y in range(3, 5)] + [Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][y][1] for y in range(2)] + [X[r][x][y][1] for y in range(3, 5)] + [Y[r][x][k][1]], eq)

def f3(m, Y, X,start,fr_y,rounds):

    for x in range(64):
        for y in range(5):
            start.append(Y[0][x][y][2])

    for r in range(rounds):
        for x in range(64):
            eq = [[0, 0, 0, 0, 1, -1], [0, 0, 0, 1, -1, 0], [1, 0, 0, 0, -1, 1], [0, 1, 0, 0, -1, 1], [0, 0, 1, 0, -1, 1], [-1, -1, -1, 0, 1, 0], [-1, -1, -1, 0, 0, -1]]
            for y in range(5):

                if y == 0:
                    constr(m, [Y[r][x][y][0], Y[r][(64 + x - 19) % 64][y][0], Y[r][(64 + x - 28) % 64][y][0], X[r + 1][x][0][2], X[r + 1][x][0][0], fr_y[r][x][0]], eq)
                if y == 1:
                    constr(m, [Y[r][x][y][0], Y[r][(64 + x - 61) % 64][y][0], Y[r][(64 + x - 39) % 64][y][0], X[r + 1][x][1][2], X[r + 1][x][1][0], fr_y[r][x][1]], eq)
                if y==2:
                    constr(m, [Y[r ][x][y][0],Y[r][(64 + x - 1)  % 64][y][0], Y[r][(64 + x - 6)  % 64][y][0], X[r + 1][x][2][2], X[r + 1][x][2][0], fr_y[r][x][2]], eq)
                if y == 3:
                    constr(m, [Y[r ][x][y][0],Y[r][(64 + x - 10) % 64][y][0], Y[r][(64 + x - 17) % 64][y][0], X[r + 1][x][3][2], X[r + 1][x][3][0], fr_y[r][x][3]], eq)
                if y==4:
                    constr(m, [Y[r ][x][y][0],Y[r][(64 + x - 7)  % 64][y][0], Y[r][(64 + x - 41) % 64][y][0], X[r + 1][x][4][2], X[r + 1][x][4][0], fr_y[r][x][4]], eq)

            eq = [[0, 1, 0, -1], [0, 0, 1, -1], [-1, -1, -1, 1], [1, 0, 0, -1]]
            for y in range(5):

                if y == 0:
                    constr(m, [Y[r][x][y][1], Y[r][(64 + x - 19) % 64][y][1], Y[r][(64 + x - 28) % 64][y][1], X[r + 1][x][0][1]], eq)
                if y == 1:
                    constr(m, [Y[r][x][y][1], Y[r][(64 + x - 61) % 64][y][1], Y[r][(64 + x - 39) % 64][y][1], X[r + 1][x][1][1]], eq)
                if y == 2:
                    constr(m, [Y[r ][x][y][1], Y[r ][(64 + x - 1) % 64][y][1], Y[r ][(64 + x - 6) % 64][y][1], X[r + 1][x][2][1]], eq)
                if y == 3:
                    constr(m, [Y[r ][x][y][1], Y[r ][(64 + x - 10) % 64][y][1], Y[r ][(64 + x - 17) % 64][y][1], X[r + 1][x][3][1]], eq)
                if y == 4:
                    constr(m, [Y[r ][x][y][1], Y[r ][(64 + x - 7) % 64][y][1], Y[r ][(64 + x - 41) % 64][y][1], X[r + 1][x][4][1]], eq)


            eq = [[0, 1, 0, -1], [0, 0, 1, -1], [-1, -1, -1, 1], [1, 0, 0, -1]]
            for y in range(5):

                if y == 0:
                    constr(m, [Y[r][x][y][2], Y[r][(64 + x - 19) % 64][y][2], Y[r][(64 + x - 28) % 64][y][2], X[r + 1][x][0][2]], eq)
                if y == 1:
                    constr(m, [Y[r][x][y][2], Y[r][(64 + x - 61) % 64][y][2], Y[r][(64 + x - 39) % 64][y][2], X[r + 1][x][1][2]], eq)
                if y == 2:
                    constr(m, [Y[r][x][y][2], Y[r][(64 + x - 1)  % 64][y][2], Y[r][(64 + x - 6)  % 64][y][2], X[r + 1][x][2][2]], eq)
                if y == 3:
                    constr(m, [Y[r][x][y][2], Y[r][(64 + x - 10) % 64][y][2], Y[r][(64 + x - 17) % 64][y][2], X[r + 1][x][3][2]], eq)
                if y == 4:
                    constr(m, [Y[r][x][y][2], Y[r][(64 + x - 7)  % 64][y][2], Y[r][(64 + x - 41) % 64][y][2], X[r + 1][x][4][2]], eq)

