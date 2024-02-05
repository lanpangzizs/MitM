from function import *

def set_red(m,X,start):
    start.append(-X[0])
    start.append(X[1])
    start.append(X[2])

def set_blue(m,X,start):
    start.append(X[0])
    start.append(-X[1])
    start.append(X[2])

def set_gray(m,X,start):
    start.append(X[0])
    start.append(X[1])
    start.append(X[2])

def count_start(m,S,L3,start_red,start_blue,num,start):
    t1=[]
    for x in range(4):
        for z in range(64):
            t1.append(S[L3[x * 320 + z][0]][L3[x * 320 + z][1]][L3[x * 320 + z][2]][0])
    [num,start]=less_count(m,t1,256-start_red,num,start,0)
    return [num,start]

def less_count(m,x,count,num,start,mode):
    [s,num] = variable_2(m,len(x) - 1, count, num)
    if mode==0:
        c = [[-1, 1]]
        constr(m, [x[0], s[0][0]], c)
        for j in range(1, count):
            start.append(-s[0][j])
        for i in range(1, len(x)-1):
            c = [[-1, 1]]
            constr(m, [x[i], s[i][0]], c)
            constr(m, [s[i - 1][0], s[i][0]], c)
            for j in range(1, count):
                c = [[-1, -1, 1]]
                constr(m, [x[i], s[i - 1][j - 1], s[i][j]], c)
                c = [[-1, 1]]
                constr(m, [s[i - 1][j], s[i][j]], c)
            c = [[-1, -1]]
            constr(m, [x[i], s[i - 1][count - 1]], c)
        c = [[-1, -1]]
        constr(m, [x[len(x)-1], s[len(x)-2][count - 1]], c)
    else:
        c = [[-1, 1], [1, -1]]
        constr(m, [x[0], s[0][0]], c)
        for j in range(1, count):
            start.append(-s[0][j])
        for i in range(1, len(x)-1):
            c = [[-1, 1]]
            constr(m, [x[i], s[i][0]], c)
            c = [[-1, 1]]
            constr(m, [s[i - 1][0], s[i][0]], c)
            c = [[1, 1, -1]]
            constr(m, [x[i], s[i - 1][0], s[i][0]], c)
            for j in range(1, count):
                c = [[-1, -1, 1], [1, 1, -1], [-1, 1, -1]]
                constr(m, [x[i], s[i - 1][j - 1], s[i][j]], c)

                c = [[1, 1, -1]]
                constr(m, [x[i], s[i - 1][j], s[i][j]], c)
                c = [[-1, 1]]
                constr(m, [s[i - 1][j], s[i][j]], c)
            c = [[-1, -1]]
            constr(m, [x[i], s[i - 1][count - 1]], c)
        c = [[-1, -1]]
        constr(m, [x[len(x) - 1], s[len(x) - 2][count - 1]], c)

        for i in range(count):
            if i != count-1:
                start.append(s[len(x) - 2][i])
            else:
                c = [[1, 1], [-1, -1]]
                constr(m, [s[len(x) - 2][i], x[len(x) - 1]], c)
    return [num,start]
def less_count_0(m,x,count,num,start,mode):
    [s,num] = variable_2(m,len(x) - 1, count, num)
    if mode==0:
        c = [[1, 1]]
        constr(m, [x[0], s[0][0]], c)
        for j in range(1, count):
            start.append(-s[0][j])
        for i in range(1, len(x)-1):
            c = [[1, 1]]
            constr(m, [x[i], s[i][0]], c)
            c = [[-1, 1]]
            constr(m, [s[i - 1][0], s[i][0]], c)
            for j in range(1, count):
                c = [[1, -1, 1]]
                constr(m, [x[i], s[i - 1][j - 1], s[i][j]], c)
                c = [[-1, 1]]
                constr(m, [s[i - 1][j], s[i][j]], c)
            c = [[1, -1]]
            constr(m, [x[i], s[i - 1][count - 1]], c)
        c = [[1, -1]]
        constr(m, [x[len(x)-1], s[len(x)-2][count - 1]], c)
    else:
        c = [[-1, -1], [1, 1]]
        constr(m, [x[0], s[0][0]], c)
        for j in range(1, count):
            start.append(-s[0][j])
        for i in range(1, len(x)-1):
            c = [[1, 1]]
            constr(m, [x[i], s[i][0]], c)
            c = [[-1, 1]]
            constr(m, [s[i - 1][0], s[i][0]], c)
            c = [[-1, 1, -1]]
            constr(m, [x[i], s[i - 1][0], s[i][0]], c)
            for j in range(1, count):
                c = [[1, -1, 1], [-1, 1, -1], [1, 1, -1]]
                constr(m, [x[i], s[i - 1][j - 1], s[i][j]], c)
                c = [[-1, 1, -1]]
                constr(m, [x[i], s[i - 1][j], s[i][j]], c)
                c = [[-1, 1]]
                constr(m, [s[i - 1][j], s[i][j]], c)
            c = [[1, -1]]
            constr(m, [x[i], s[i - 1][count - 1]], c)
        c = [[1, -1]]
        constr(m, [x[len(x) - 1], s[len(x) - 2][count - 1]], c)


        for i in range(count):
            if i == count-1:
                c = [[1, -1], [-1, 1]]
                constr(m, [s[len(x) - 2][i], x[len(x) - 1]], c)
            else:
                start.append(s[len(x) - 2][i])
    return [num,start]





def count_condition(m,condition,condition_num,num,start):
    t=[]
    for x in range(4):
        for y in range(5):
            for z in range(64):
                t.append(condition[x][y][z])
    [num,start]=less_count(m,t,condition_num,num,start,0)
    return [num,start]



def set_start_weak(m,S,X,condition,L3,num,start):

    for x in range(5):
        for y in range(5):
            for z in range(64):

                start.append(X[0][x][y][z][2])

                if x==0:
                    eq = [[1, 0, 0, -1], [-1, 0, -1, 1], [-1, -1, 0, 1], [0, 1, 1, -1]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i],S[1][y][z][i], condition[2][y][z], X[0][x][y][z][i]], eq)

                if x==1:
                    for i in range(2):
                        eq = [[-1, 1], [1, -1]]
                        constr(m,[X[0][x][y][z][i],S[x][y][z][i]],eq)


                if x == 2 or [x, y] in [[3, 3], [1, 1]]:
                    set_gray(m, X[0][x][y][z],start)


                if x == 3:
                    if y != 3:
                        eq= [[0, -1, 1], [-1, 0, 1], [1, 1, -1]]
                        for i in range(2):
                            constr(m, [S[0][y][z][i], condition[3][y][z], X[0][x][y][z][i]], eq)

                if x==4:
                    eq= [[0, 0, -1, 0, 1], [0, 0, 0, -1, 1], [-1, -1, 0, 0, 1], [0, 1, 1, 1, -1], [1, 0, 1, 1, -1]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i],S[1][y][z][i],condition[0][y][z],condition[1][y][z],X[0][x][y][z][i]],eq)

    return num


def set_start_blue(S,condition,start,loc_B,loc_R,loc_condition):
    for x in range(5):
        for y in range(5):
            for z in range(64):
                if [x,y,z] in loc_R:
                    start.append(-S[x][y][z][0])
                    start.append(S[x][y][z][1])
                elif [x,y,z] in loc_B:
                    start.append(S[x][y][z][0])
                    start.append(-S[x][y][z][1])
                else:
                    start.append(S[x][y][z][0])
                    start.append(S[x][y][z][1])

    for x in range(4):
        for y in range(5):
            for z in range(64):
                if [x,y,z] in loc_condition:
                    start.append(condition[x][y][z])
                else:
                    start.append(-condition[x][y][z])



def f1(m,X,C,D,Y,fr_c,fr_d,fr_y,rounds):
    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                eq= [[0, 0, 1, 0, 0, -1], [0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 1, -1], [1, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, -1], [-1, -1, -1, -1, -1, 1]]
                constr(m,[X[r][x][i][z][2] for i in range(5)]+[C[r][x][z][1]],eq)
                eq = [[0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 1, 0, -1, 1], [0, 0, 0, 1, 0, 0, -1, 1], [1, 0, 0, 0, 0, 0, -1, 1], [0, 0, 1, 0, 0, 0, -1, 1], [0, 1, 0, 0, 0, 0, -1, 1], [-1, -1, -1, -1, -1, 0, 1, 0], [-1, -1, -1, -1, -1, 0, 0, -1]]
                constr(m, [X[r][x][i][z][0] for i in range(5)] + [C[r][x][z][1]]+[C[r][x][z][0]]+[fr_c[r][x][z]], eq)

    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                eq= [[1, 0, -1], [0, 1, -1], [-1, -1, 1]]
                constr(m, [C[r][(x - 1) % 5][z][1], C[r][(x + 1) % 5][(z - 1) % 64][1],D[r][x][z][1]], eq)
                eq= [[0, 0, 0, 1, -1], [0, 0, 1, -1, 0], [0, 1, 0, -1, 1], [-1, -1, 0, 1, 0], [-1, -1, 0, 0, -1], [1, 0, 0, -1, 1]]
                constr(m, [C[r][(x - 1) % 5][z][0], C[r][(x + 1) % 5][(z - 1) % 64][0],D[r][x][z][1],D[r][x][z][0],fr_d[r][x][z]], eq)

    for r in range(rounds):
        for z in range(64):
            for x in range(5):
                for y in range(5):
                    eq = [[1, 0, -1], [0, 1, -1], [-1, -1, 1]]
                    constr(m, [X[r][x][y][z][2], D[r][x][z][1], Y[r][x][y][z][2]], eq)
                    eq= [[0, 0, 0, 1, -1], [0, 0, 1, -1, 0], [0, 1, 0, -1, 1], [-1, -1, 0, 1, 0], [-1, -1, 0, 0, -1], [1, 0, 0, -1, 1]]
                    constr(m, [X[r][x][y][z][0], D[r][x][z][0], Y[r][x][y][z][2], Y[r][x][y][z][0], fr_y[r][x][y][z]], eq)
                    eq= [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]]
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
                    eq= [[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1], [-1, -1, -1, 1]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][0] for i in range(3)] + [X[r + 1][x][y][z][0]],eq)
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][1] for i in range(3)] + [X[r + 1][x][y][z][1]],eq)
                    eq= [[1, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 1, 0, -1], [0, 0, 0, 1, 0, 0, 1, -1], [-1, -1, -1, -1, 0, -1, 0, 1], [-1, -1, -1, 0, -1, 0, -1, 1], [-1, -1, -1, -1, -1, 0, 0, 1], [-1, -1, -1, 0, 0, -1, -1, 1]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][2] for i in range(3)] +[Y[r][L1[((x+1)%5) * 320 + y * 64 + z][0]][L1[((x+1)%5) * 320 + y * 64 + z][1]][L1[((x+1)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[Y[r][L1[((x+2)%5) * 320 + y * 64 + z][0]][L1[((x+2)%5) * 320 + y * 64 + z][1]][L1[((x+2)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[X[r + 1][x][y][z][2]], eq)



def count_freedom(m,fr_c,fr_d,fr_y,fredom_consume,rounds,num,start):
    t=[]
    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                t.append(fr_c[r][x][z])
                t.append(fr_d[r][x][z])
                for y in range(5):
                    t.append(fr_y[r][x][y][z])
    [num,start]=less_count(m,t,fredom_consume,num,start,0)
    return [num,start]


def set_obj(m,X,match1,match2,rounds,M,num,start,model,match1_find=None,match2_find=None):
    for z in range(64):
        eq= [[1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, -1, 0, -1, -1], [0, 0, 0, 0, -1, 0, -1, 0, -1], [-1, -1, -1, -1, 1, 0, 0, 1, 1], [-1, -1, -1, -1, 1, 1, 0, 0, 1], [-1, -1, -1, -1, 0, 1, 1, 0, 1], [-1, -1, -1, -1, 0, 0, 1, 1, 1]]
        constr(m, [X[rounds][3][0][z - gama[3][0]][2], X[rounds][3][3][z - gama[3][0]][2], X[rounds][0][2][z - gama[0][2]][2], X[rounds][0][0][z - gama[0][2]][2]] + [X[rounds][3][0][z - gama[3][0]][i] for i in range(2)] + [X[rounds][3][3][z - gama[3][0]][i] for i in range(2)] + [match1[z]], eq)
        constr(m, [X[rounds][4][1][z - gama[4][1]][2], X[rounds][4][4][z - gama[4][1]][2], X[rounds][1][3][z - gama[1][3]][2], X[rounds][1][1][z - gama[1][3]][2]] + [X[rounds][4][1][z - gama[4][1]][i] for i in range(2)] + [X[rounds][4][4][z - gama[4][1]][i] for i in range(2)] + [match2[z]], eq)

    if model==1:
        t=[]
        for z in range(64):
            t.append(match1[z])
            t.append(match2[z])
        [num,start]=less_count(m,t,M,num,start,1)
    else:
        t = []
        for z in range(64):
            if z not in match1_find:
                t.append(match1[z])
            if z not in match2_find:
                t.append(match2[z])
        [num, start] = less_count(m, t, M, num, start, 1)

    return [num,start]



