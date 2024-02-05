

from MILP import *
def set_variable(m,rounds):
    X = variable_4(m, rounds + 1, 64,5, 3)
    Y = variable_4(m, rounds, 64,5, 3)
    C_r = variable_2(m, 64, 2)
    C_b = variable_2(m, 64, 2)
    fr = variable_3(m, rounds, 64,5)
    match=variable_2(m,rounds,64)
    return X,Y,fr,C_r,C_b,match

def set_start(m,X,C_r,C_b,start_red,start_blue):
    for x in range(64):
        if x==62 or x==63:
            for y in range(5):
                for i in range(3):
                    m.addConstr(X[x][y][i]==1)
        else:

            eq = [[-1, 3, -1, -1, 1, 1, 0], [-2, 3, 1, -2, 3, -2, 0], [1, -3, 1, 1, -1, -1, 0]]
            constr(m,[X[x][0][0],X[x][1][0],X[x][3][0],X[x][4][0],C_r[x][0],C_r[x][1]],eq)
            constr(m,[X[x][0][1],X[x][1][1],X[x][3][1],X[x][4][1],C_b[x][0],C_b[x][1]],eq)

            for i in range(2):
                m.addConstr(X[x][2][i]==1)
        for y in range(5):
            m.addConstr(X[x][y][0]+X[x][y][1]>=1)


    m.addConstr(64 - gp.quicksum([X[x][1][0] for x in range(64)]) == start_red)
    m.addConstr(64 - gp.quicksum([X[x][1][1] for x in range(64)]) == start_blue)

def set_condition(m,C_r,C_b,condition_num):
    m.addConstr(gp.quicksum([j for i in C_r for j in i]+[j for i in C_b for j in i])<=condition_num)
    return 0

def set_DOF(m,fr,DOF):
    m.addConstr(gp.quicksum([k for i in fr for j in i for k in j])<=DOF)
    return

def set_match_2(m, Y, rounds, match):
    for r in range(1,rounds):
        for x in range(64):
            eq = [[-1, -1, -1, -1, -1, 1, 4], [1, 1, 1, 1, 1, -5, 0]]
            constr(m,[Y[r][x][y][1] for y in range(5)]+[match[r][x]],eq)

def f1(m,X,Y,rounds):
    for r in range(1,rounds):
        for x in range(64):
            for y in range(5):
                if y ==0:#b0 = a4a1 + a3 + a2a1 + a2 + a1a0 + a1 + a0
                    eq= [[-2, -1, -1, 0, -3, -3, 3, 8], [0, -2, -1, -3, -3, -3, 3, 9], [1, 0, 0, 1, 2, 0, -3, 0], [0, 1, 1, 0, 0, 2, -3, 0]]
                    constr(m,[X[r][x][1][k] for k in range(2)]+[X[r][x][2][k] for k in range(2)]+[Y[r][x][4][2]]+[X[r][x][0][2]] + [Y[r][x][y][2]],eq)
                if y ==1:#b1 = a4 + a3a2 + a3a1 + a3 + a2a1 + a2 + a1 + a0
                    eq= [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, -3, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, -3, 0], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, -3, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, -3, 0], [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, -3, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, -3, 0], [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, -3, 0], [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, -3, 0], [0, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, 1, 7], [-3, -1, -3, -1, -2, 0, -3, -3, -3, -3, -3, 3, 22], [-3, -1, -2, 0, -3, -1, -3, -3, -3, -3, -3, 3, 22], [-2, 0, -3, -1, -3, -1, -3, -3, -3, -3, -3, 3, 22]]
                    constr(m, [X[r][x][1][k] for k in range(2)] + [X[r][x][2][k] for k in range(2)] + [X[r][x][3][k] for k in range(2)] + [X[r][x][k][2] for k in range(5)] + [Y[r][x][y][2]], eq)
                if y==2:#b2 = a4a3 + a4 + a2 + a1 + 1
                    eq= [[0, 0, 0, 0, 1, 1, 0, 1, -3, 0], [0, 0, 0, 0, 1, 0, 1, 1, -3, 0], [1, 0, 0, 1, 0, 1, 1, 0, -3, 0], [0, 1, 1, 0, 0, 1, 1, 0, -3, 0], [-2, -1, -1, 0, -3, -2, -3, -2, 3, 12], [-1, -1, -2, -2, -3, -3, -3, -3, 3, 15], [-1, -2, -1, -2, -3, -3, -3, -3, 3, 15]]
                    constr(m, [X[r][x][3][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(1,5)] + [Y[r][x][y][2]], eq)
                if y==3: #b3 = a4a0 + a4 + a3a0 + a3 + a2 + a1 + a0
                    eq= [[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, -3, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, -3, 0], [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, -3, 0], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, -3, 0], [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, -3, 0], [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, -3, 0], [-1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, 1, 6], [0, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, 1, 7], [-2, 0, -3, -1, -3, -1, -3, -3, -3, -3, -3, 3, 22]]
                    constr(m, [X[r][x][0][k] for k in range(2)] + [X[r][x][3][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(5)] + [Y[r][x][y][2]], eq)
                if y==4:#b4 = a4a1 + a4 + a3 + a1a0 + a1
                    eq= [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, -3, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, -3, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, -3, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, -3, 0], [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, -3, 0], [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, -3, 0], [0, -1, -2, -3, 0, -1, -3, -3, -3, -3, 3, 16], [-3, -1, -2, 0, -3, -1, -3, -3, -3, -3, 3, 19]]
                    constr(m, [X[r][x][0][k] for k in range(2)] + [X[r][x][1][k] for k in range(2)] + [X[r][x][4][k] for k in range(2)] + [X[r][x][k][2] for k in range(2)] +[X[r][x][k][2] for k in range(3,5)]+ [Y[r][x][y][2]], eq)

            for k in range(5):
                if k==0 or k==1 or k==3:
                    eq= [[-1, -1, 1, 1], [1, 1, -2, 0]]
                    constr(m, [X[r][x][0][0] , Y[r][x][2][0] , Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][0][1] , Y[r][x][2][1] , Y[r][x][k][1]], eq)
                if k==2:
                    eq= [[-1, -1, -1, -1, 1, 3], [1, 0, 1, 0, -2, 0], [0, 1, 0, 1, -2, 0]]
                    constr(m, [X[r][x][y][0] for y in range(1, 5)] + [Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][y][1] for y in range(1, 5)] + [Y[r][x][k][1]], eq)
                if k==4:
                    eq = [[-1, -1, -1, -1, 1, 3], [1, 0, 1, 0, -2, 0], [0, 1, 0, 1, -2, 0]]
                    constr(m, [X[r][x][y][0] for y in range(2)] + [X[r][x][y][0] for y in range(3, 5)] + [Y[r][x][k][0]], eq)
                    constr(m, [X[r][x][y][1] for y in range(2)] + [X[r][x][y][1] for y in range(3, 5)] + [Y[r][x][k][1]], eq)

def f3(m, Y, X,fr_y,rounds):

    for r in range(rounds):
        for x in range(64):
            eq= [[0, 1, 0, 2, -3, 1, 0], [1, 1, 1, 0, -3, 3, 0], [-1, -1, -1, 0, 3, -3, 2]]
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

            eq= [[-1, -1, -1, 1, 2], [1, 1, 1, -3, 0]]
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

