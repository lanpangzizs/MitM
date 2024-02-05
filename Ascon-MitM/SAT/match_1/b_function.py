from pysat.formula import CNF
from pysat.solvers import Cadical153

from c_model_constrain import *
from d_model_function import *
def F(M,start_red,start_blue,condition_num,consum_red,loc_B,loc_R,loc_cb1,loc_cb2,rounds,mode,match_all=None):

    m= CNF();start=[];num=1


    X=[];Y=[];fr_y=[];match=[];C_r=[];C_b=[]
    num=set_variable(num,rounds,X,Y,fr_y,match,C_r,C_b)


    num=set_start(m,num,Y[0],start,C_r,C_b,start_red,start_blue)


    num=set_value(Y[0],loc_R,loc_B,loc_cb1,loc_cb2,start,num,mode,C_b)


    num=set_condition(m,num,start,C_r,C_b,condition_num)


    num=set_DOF(m,num,start,consum_red,fr_y)


    f1(m, X, Y, rounds)
    f3(m, Y, X, start, fr_y, rounds)


    set_match(m,X[rounds],match)


    num=conunt_match(m,num,start,match,M,match_all)



    print("模型大小:",num)
    with Cadical153(bootstrap_with=m.clauses) as l:
        if l.solve(assumptions=start) == True:
            print("模型有解")

            result=l.get_model()
            result=[0]+result
            if len(result)<num:
                for i in range(len(result),num+1):
                    result.append(i)
            printresult(result,X,Y,fr_y,C_r,C_b,match,rounds,1)
            print_condition(result,C_r,C_b,Y[0])
            print_DOF(result, fr_y,rounds)
            print_match(result, match,X[rounds],match_all)
            print_start(result,Y[0],start_red,start_blue,rounds)
        else:
            print("模型无解")

