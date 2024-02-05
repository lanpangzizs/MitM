
from constrain import *
from function import *


def F(rounds,start_red,start_blue,condition_num,fredom_consume):
    m = gp.Model()

    L1=[];L3=[]
    [S,X,C,D,Y,fb_0,fr_0,fr_c,fr_d,fr_y,match1,match2,condition]=create_variable(m,rounds)

    f2(L1,L3)

    set_start_weak(m,S,X,condition,L3,start_red,start_blue,condition_num)

    f1(m,X,C,D,Y,fr_c,fr_d,fr_y,rounds)
    f3(m,Y,X,L1,rounds)
    count_start(m, S, L3, start_red, start_blue)

    count_condition(m, condition, condition_num)

    count_freedom(m,fr_c,fr_d,fr_y,fredom_consume,rounds)

    t=[]
    for x in range(5):
        for y in range(5):
            for z in range(64):
                t.append(X[rounds][x][y][z][2])
    o = gp.quicksum(t)
    m.setObjective(o, GRB.MAXIMIZE)


    m.optimize()
    if m.solcount != 0:
        printresult(m,rounds,S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,L1,L3)
        print_weak(m,rounds,S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,L1,L3)
    else:
        print("模型无解")
