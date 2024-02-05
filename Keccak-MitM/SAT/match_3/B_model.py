from pysat.formula import CNF
from pysat.solvers import Cadical153
from constrain import *
from function import *
from D_model_function import *

def F(rounds,fredom_consume,M,loc_B,loc_R,loc_condition,model,match1_find=None,match2_find=None):
    m= CNF()

    num=1
    L1=[];L3=[];start=[]
    [S,X,C,D,Y,fr_c,fr_d,fr_y,match1,match2,condition,num]=create_variable(m,rounds,num)

    f2(L1,L3)

    num=set_start_weak(m,S,X,condition,L3,num,start)

    set_start_blue(S,condition,start,loc_B,loc_R,loc_condition)

    f1(m,X,C,D,Y,fr_c,fr_d,fr_y,rounds)
    f3(m,Y,X,L1,rounds)

    [num,start]=count_freedom(m,fr_c,fr_d,fr_y,fredom_consume,rounds,num,start)


    [num,start]=set_obj(m,X,match1,match2,rounds,M,num,start,model)

    print("模型大小：",num)

    with Cadical153(bootstrap_with=m.clauses) as l:
        if l.solve(assumptions=start) == True:
            print("模型有解")
            result = l.get_model()
            result = [0] + result
            if len(result) < num:
                for i in range(len(result), num + 1):
                    result.append(i)

            print_DOF(result,fr_d,fr_y,fr_c,rounds)
        else:
            print("模型无解")
