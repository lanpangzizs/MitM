from function import *

def set_red(m,X):
    m.addConstr(X[0] == 0)
    m.addConstr(X[1] == 1)
    m.addConstr(X[2] == 1)

def set_blue(m,X):
    m.addConstr(X[0] == 1)
    m.addConstr(X[1] == 0)
    m.addConstr(X[2] == 1)

def set_gray(m,X):
    m.addConstr(X[0] == 1)
    m.addConstr(X[1] == 1)
    m.addConstr(X[2] == 1)

def count_start(m,S,L3,start_red,start_blue):
    t1=gp.quicksum([S[L3[0*320+z][0]][L3[0*320+z][1]][L3[0*320+z][2]][1] for z in range(64)]+[S[L3[1*320+z][0]][L3[1*320+z][1]][L3[1*320+z][2]][1] for z in range(64)]+[S[L3[2*320+z][0]][L3[2*320+z][1]][L3[2*320+z][2]][1] for z in range(64)]+[S[L3[3*320+z][0]][L3[3*320+z][1]][L3[3*320+z][2]][1] for z in range(64)])
    t2=gp.quicksum([S[L3[0*320+z][0]][L3[0*320+z][1]][L3[0*320+z][2]][0] for z in range(64)]+[S[L3[1*320+z][0]][L3[1*320+z][1]][L3[1*320+z][2]][0] for z in range(64)]+[S[L3[2*320+z][0]][L3[2*320+z][1]][L3[2*320+z][2]][0] for z in range(64)]+[S[L3[3*320+z][0]][L3[3*320+z][1]][L3[3*320+z][2]][0] for z in range(64)])
    m.addConstr(4*64-t1==start_blue)
    m.addConstr(4*64-t2==start_red)

def count_condition(m,condition,condition_num):
    t=[]
    for x in range(4):
        for y in range(5):
            for z in range(64):
                t.append(condition[x][y][z])
    m.addConstr(gp.quicksum(t)<=condition_num)


def set_start_weak(m,S,X,condition,L3,start_red,start_blue,condition_num):

    for x in range(5):
        for y in range(5):
            for z in range(64):
                if x == 4 or y >= 2:
                    for i in range(2):
                        m.addConstr(S[L3[x*320+y*64+z][0]][L3[x*320+y*64+z][1]][L3[x*320+y*64+z][2]][i] == 1)


                if [x,y] in [[0,0],[1,0],[2,0],[3,0]]:
                    m.addConstr(S[L3[x*320+y*64+z][0]][L3[x*320+y*64+z][1]][L3[x*320+y*64+z][2]][0] + S[L3[x*320+y*64+z][0]][L3[x*320+y*64+z][1]][L3[x*320+y*64+z][2]][1] >= 1)
                    for i in range(2):
                        m.addConstr(S[L3[x*320+y*64+z][0]][L3[x*320+y*64+z][1]][L3[x*320+y*64+z][2]][i]==S[L3[x*320+1*64+z][0]][L3[x*320+1*64+z][1]][L3[x*320+1*64+z][2]][i])


                if x==0:
                    if y in [0,2,4]:
                        eq = [[1, -1, -1, 1, 1], [-1, 1, 1, -1, 1]]
                        for i in range(2):
                            constr(m,[S[0][y][z][0],S[0][y][z][1],S[1][y][z][0],S[1][y][z][1]],eq)


    for x in range(2):
        for y in range(5):
            for z in range(64):
                eq=[[1, 1, -2, 0]]
                constr(m, [S[x][y][z][0], S[x][y][z][1], condition[x][y][z]], eq)




    for x in range(5):
        for y in range(5):
            for z in range(64):

                m.addConstr(X[0][x][y][z][2]==1)


                if x==0:
                    eq=[[-3, -2, -1, 3, 3], [2, 1, 1, -3, 0]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i],S[1][y][z][i], condition[2][y][z], X[0][x][y][z][i]], eq)

                if x==1:
                    for i in range(2):
                        m.addConstr(X[0][x][y][z][i]==S[x][y][z][i])


                if x == 2 or [x, y] in [[3, 3], [1, 1]]:
                    set_gray(m, X[0][x][y][z])


                if x == 3:
                    if y != 3:
                        eq = [[-1, -1, 2, 0], [2, 2, -2, 0]]
                        for i in range(2):
                            constr(m, [S[0][y][z][i], condition[3][y][z], X[0][x][y][z][i]], eq)

                if x==4:
                    eq= [[-1, -1, -2, -2, 5, 1], [4, 1, 5, 5, -5, 0]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i],S[1][y][z][i],condition[0][y][z],condition[1][y][z],X[0][x][y][z][i]],eq)






def f1(m,X,C,D,Y,fr_c,fr_d,fr_y,rounds):

    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                eq = [[-1, -1, -1, -1, -1, 1, 4], [1, 1, 1, 1, 1, -5, 0]]
                constr(m,[X[r][x][i][z][2] for i in range(5)]+[C[r][x][z][1]],eq)
                eq=[[1, 1, 1, 1, 1, 0, -5, 5, 0], [0, 0, 0, 1, 1, 3, -5, 2, 0], [-1, -1, -1, -1, -1, 0, 5, -5, 4]]
                constr(m, [X[r][x][i][z][0] for i in range(5)] + [C[r][x][z][1]]+[C[r][x][z][0]]+[fr_c[r][x][z]], eq)

    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                eq = [[-1, -1, 1, 1], [1, 1, -2, 0]]
                constr(m, [C[r][(x - 1) % 5][z][1], C[r][(x + 1) % 5][(z - 1) % 64][1],D[r][x][z][1]], eq)
                eq =[[1, 1, 2, -4, 2, 0], [-2, -2, 1, 3, -4, 2]]
                constr(m, [C[r][(x - 1) % 5][z][0], C[r][(x + 1) % 5][(z - 1) % 64][0],D[r][x][z][1],D[r][x][z][0],fr_d[r][x][z]], eq)

    for r in range(rounds):
        for z in range(64):
            for x in range(5):
                for y in range(5):
                    eq = [[-1, -1, 1, 1], [1, 1, -2, 0]]
                    constr(m, [X[r][x][y][z][2], D[r][x][z][1], Y[r][x][y][z][2]], eq)
                    eq = [[1, 1, 2, -4, 2, 0], [-2, -2, 1, 3, -4, 2]]
                    constr(m, [X[r][x][y][z][0], D[r][x][z][0], Y[r][x][y][z][2], Y[r][x][y][z][0], fr_y[r][x][y][z]], eq)
                    eq = [[-1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,10], [1, 1, 1, 1,1,1,1,1,1,1,1,-11,0]]
                    constr(m, [X[r][x][y][z][1]]+[X[r][(x-1)%5][i][z][1] for i in range(5)]+[X[r][(x+1)%5][i][(z-1)%64][1] for i in range(5)]+[Y[r][x][y][z][1]],eq)


def f2(L1,L3):
    L2 = [[[0, 0] for i in range(5)] for i in range(5)]
    for x in range(5):
        for y in range(5):
            L2[y][(2 * x + 3 * y) % 5] = [x, y]

    for x in range(5):
        for y in range(5):
            for z in range(64):
                L1.append(L2[x][y] + [(z - gama[L2[x][y][0]][L2[x][y][1]]) % 64])

    for x in range(5):
        for y in range(5):
            for z in range(64):
                for i in range(len(L1)):
                    if L1[i] == [x, y, z]:
                        L3.append([int(i / 320), int((i % 320) / 64), i % 64])

def f3(m,Y,X,L1,rounds):

    for r in range(rounds):
        for x in range(5):
            for y in range(5):
                for z in range(64):

                    eq=[[-1, -1, -1, 1, 2], [1, 1, 1, -3, 0]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][0] for i in range(3)] + [X[r + 1][x][y][z][0]],eq)
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][1] for i in range(3)] + [X[r + 1][x][y][z][1]],eq)
                    eq=[[-5, -5, -5, -3, -2, -2, -1, 5, 19], [-5, -5, -5, -1, -2, -2, -3, 5, 19], [2, 0, 2, 1, 0, 0, 1, -5, 0], [2, 2, 0, 0, 1, 1, 0, -5, 0]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][2] for i in range(3)] +[Y[r][L1[((x+1)%5) * 320 + y * 64 + z][0]][L1[((x+1)%5) * 320 + y * 64 + z][1]][L1[((x+1)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[Y[r][L1[((x+2)%5) * 320 + y * 64 + z][0]][L1[((x+2)%5) * 320 + y * 64 + z][1]][L1[((x+2)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[X[r + 1][x][y][z][2]], eq)


def count_freedom(m,fr_c,fr_d,fr_y,condition_num,rounds):
    t0=[];t1=[];t2=[]
    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                t0.append(fr_c[r][x][z])
                t1.append(fr_d[r][x][z])
                for y in range(5):
                    t2.append(fr_y[r][x][y][z])
    t=gp.quicksum(t0+t1+t2)
    m.addConstr(gp.quicksum(t1)==0)
    m.addConstr(t<=condition_num)

def set_obj(m,X,match1,match2,rounds):
    for z in range(64):
        eq=[[-2, -2, -2, -2, 1, 2, 1, 0, 2, 6], [-2, -2, -2, -2, 1, 0, 1, 2, 2, 6], [1, 1, 0, 0, 0, 0, 0, 0, -2, 0], [0, 0, 1, 0, -1, 0, -1, 0, -2, 2], [0, 0, 1, 1, 0, 0, 0, 0, -2, 0], [0, 1, 0, 0, 0, -1, 0, -1, -2, 2]]
        constr(m, [X[rounds][3][0][z - gama[3][0]][2], X[rounds][3][3][z - gama[3][0]][2], X[rounds][0][2][z - gama[0][2]][2], X[rounds][0][0][z - gama[0][2]][2]] + [X[rounds][3][0][z - gama[3][0]][i] for i in range(2)] + [X[rounds][3][3][z - gama[3][0]][i] for i in range(2)] + [match1[z]], eq)
        constr(m, [X[rounds][4][1][z - gama[4][1]][2], X[rounds][4][4][z - gama[4][1]][2], X[rounds][1][3][z - gama[1][3]][2], X[rounds][1][1][z - gama[1][3]][2]] + [X[rounds][4][1][z - gama[4][1]][i] for i in range(2)] + [X[rounds][4][4][z - gama[4][1]][i] for i in range(2)] + [match2[z]], eq)




