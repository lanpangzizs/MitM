

from C_model_constrain import *
from D_model_function import *

def F(rounds,start_red,start_blue,condition_num,DOF,mode):
    m = gp.Model("mip1")


    X,Y,fr,C_r,C_b,match=set_variable(m,rounds)


    set_start(m,Y[0],C_r,C_b,start_red,start_blue)


    set_condition(m,C_r,C_b,condition_num)


    set_DOF(m,fr,DOF)


    f1(m,X,Y,rounds)

    f3(m, Y, X, fr, rounds)

    if mode==1:
        t=[]
        for x in range(64):
            for y in range(5):
                t.append(X[2][x][y][2])
                t.append(Y[1][x][y][2])
        O = gp.quicksum(t)
        m.setObjective(O, GRB.MAXIMIZE)

        m.optimize()


    if m.solcount != 0:
        printresult(m, X, Y, fr, match, rounds, 1)

        print_condition(C_r,C_b)

        print_loc(Y[0])








