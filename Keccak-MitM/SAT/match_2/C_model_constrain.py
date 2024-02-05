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

def less_count(m,x,count,num,start,mode):#模型 计数的列表((n-1)*count) 辅助变量 起点的值 计数的大小
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

        #要求等号一定成立
        for i in range(count):
            if i != count-1:
                start.append(s[len(x) - 2][i])
            else:
                c = [[1, 1], [-1, -1]]
                constr(m, [s[len(x) - 2][i], x[len(x) - 1]], c)
    return [num,start]
def less_count_0(m,x,count,num,start,mode):#模型 计数的列表((n-1)*count) 辅助变量 起点的值 计数的大小
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

        #要求等号一定成立
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

def set_start_weak(m,S,X,condition,L3,num,start):#



    #X0的值
    for x in range(5):
        for y in range(5):
            for z in range(64):
                #要求不能为白色
                start.append(X[0][x][y][z][2])

                # 有条件变灰  没条件不变
                if x==0:
                    eq = [[1, 0, 0, -1], [-1, 0, -1, 1], [-1, -1, 0, 1], [0, 1, 1, -1]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i],S[1][y][z][i], condition[2][y][z], X[0][x][y][z][i]], eq)

                if x==1:
                    for i in range(2):
                        eq = [[-1, 1], [1, -1]]
                        constr(m,[X[0][x][y][z][i],S[x][y][z][i]],eq)

                # 第二列一定为灰色
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


#设置蓝色中性集的起点
def set_start_blue(S,condition,start,loc_B,loc_R,loc_condition):
    # for i in loc_B:
    #     start.append(S[i[0]][i[1]][i[2]][0])
    #     start.append(-S[i[0]][i[1]][i[2]][1])
    #
    # for i in loc_R:
    #     start.append(-S[i[0]][i[1]][i[2]][0])
    #     start.append(S[i[0]][i[1]][i[2]][1])

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

#秦岭月在22年欧密上的起点
def set_qin(m,S,X,fr_c,fr_d,fr_y,rounds,start_red,start_blue,condition,condition_num,L3,num,start):
    # 部分一定为灰色
    for x in range(5):
        for y in range(5):
            for z in range(64):
                if x == 4 or y >= 2:
                    for i in range(2):
                        start.append(S[L3[x * 320 + y * 64 + z][0]][L3[x * 320 + y * 64 + z][1]][L3[x * 320 + y * 64 + z][2]][i])

                # 规定上下两列颜色一定要相同
                if [x, y] in [[0, 0], [1, 0], [2, 0], [3, 0]]:
                    eq = [[1, 1]]
                    constr(m, [S[L3[x * 320 + y * 64 + z][0]][L3[x * 320 + y * 64 + z][1]][L3[x * 320 + y * 64 + z][2]][0], S[L3[x * 320 + y * 64 + z][0]][L3[x * 320 + y * 64 + z][1]][L3[x * 320 + y * 64 + z][2]][1]], eq)
                    for i in range(2):
                        eq = [[-1, 1], [1, -1]]
                        constr(m, [S[L3[x * 320 + y * 64 + z][0]][L3[x * 320 + y * 64 + z][1]][L3[x * 320 + y * 64 + z][2]][i], S[L3[x * 320 + 1 * 64 + z][0]][L3[x * 320 + 1 * 64 + z][1]][L3[x * 320 + 1 * 64 + z][2]][i]], eq)

                # 不允许有蓝色和红色在同一行
                if x == 0:
                    if y in [0, 2, 4]:
                        eq = [[1, -1, -1, 1], [-1, 1, 1, -1]]
                        for i in range(2):
                            constr(m, [S[0][y][z][0], S[0][y][z][1], S[1][y][z][0], S[1][y][z][1]], eq)

    #只有在为灰色的时候才能引入条件
    for x in range(2):
        for y in range(5):
            for z in range(64):
                # 非白色
                eq = [[0, 1, -1], [1, 0, -1]]
                constr(m, [S[x][y][z][0], S[x][y][z][1], condition[x][y][z]], eq)

    for x in range(5):
        for y in range(5):
            for z in range(64):
                # 要求不能为白色
                start.append(X[0][x][y][z][2])
                # 有条件变灰  没条件不变
                if x == 0:
                    for i in range(2):
                        eq = [[1, 0, 0, -1], [-1, 0, -1, 1], [-1, -1, 0, 1], [0, 1, 1, -1]]
                        constr(m, [S[0][y][z][i], S[1][y][z][i], condition[2][y][z], X[0][x][y][z][i]], eq)

                if x == 1:
                    for i in range(2):
                        eq = [[-1, 1], [1, -1]]
                        constr(m, [X[0][x][y][z][i], S[x][y][z][i]], eq)


                if x == 4:
                    eq = [[0, 0, -1, 0, 1], [0, 0, 0, -1, 1], [-1, -1, 0, 0, 1], [0, 1, 1, 1, -1], [1, 0, 1, 1, -1]]
                    for i in range(2):
                        constr(m, [S[0][y][z][i], S[1][y][z][i], condition[0][y][z], condition[1][y][z], X[0][x][y][z][i]], eq)

                # # 第二列一定为灰色
                if x == 2 or [x, y] in [[3, 3], [1, 1]]:
                    set_gray(m, X[0][x][y][z], start)

                if x == 3:
                    if y != 3:
                        eq = [[0, -1, 1], [-1, 0, 1], [1, 1, -1]]
                        for i in range(2):
                            constr(m, [S[0][y][z][i], condition[3][y][z], X[0][x][y][z][i]], eq)


    # # 统计起点中性集数量
    [num,start]= count_start(m, S, L3, start_red, start_blue, num, start)
    #
    # 统计起点条件数量
    [num,start] = count_condition(m, condition, condition_num, num, start)

    loc=[]
    loc_r_0=[4,9,26,32,40,45,47,56];loc_r_2=[61,56,53,47,39,34,33,28,26,19,11,6];loc_b_0=[4,26,40,47];loc_b_2=[6,28,34,56]
    for k in range(64):
        if k not in loc_r_0:
            for j in range(3):
                if j ==2 or j==1:
                    start.append(X[0][0][(2 * 0 + 3 * 0) % 5][(k + gama[0][0]) % 64][j])
                    start.append(X[0][1][(2 * 0 + 3 * 1) % 5][(k + gama[0][1]) % 64][j])
                else:
                    start.append(-X[0][0][(2 * 0 + 3 * 0) % 5][(k + gama[0][0]) % 64][j])
                    start.append(-X[0][1][(2 * 0 + 3 * 1) % 5][(k + gama[0][1]) % 64][j])
            loc.append([0, (2 * 0 + 3 * 0) % 5, (k + gama[0][0]) % 64])
            loc.append([1, (2 * 0 + 3 * 1) % 5, (k + gama[0][1]) % 64])
        if k not in loc_r_2:
            for j in range(3):
                if j == 2 or j == 1:
                    start.append(X[0][0][(2 * 2 + 3 * 0) % 5][(k + gama[2][0]) % 64][j])
                    start.append(X[0][1][(2 * 2 + 3 * 1) % 5][(k + gama[2][1]) % 64][j])
                else:
                    start.append(-X[0][0][(2 * 2 + 3 * 0) % 5][(k + gama[2][0]) % 64][j])
                    start.append(-X[0][1][(2 * 2 + 3 * 1) % 5][(k + gama[2][1]) % 64][j])
            loc.append([0,(2*2+3*0)%5,(k + gama[2][0]) % 64])
            loc.append([1,(2*2+3*1)%5,(k + gama[2][1]) % 64])
        if k in loc_b_0:
            for j in range(3):
                if j ==2 or j==0:
                    start.append(X[0][0][(2 * 0 + 3 * 0) % 5][(k + gama[0][0]) % 64][j])
                    start.append(X[0][1][(2 * 0 + 3 * 1) % 5][(k + gama[0][1]) % 64][j])
                else:
                    start.append(-X[0][0][(2 * 0 + 3 * 0) % 5][(k + gama[0][0]) % 64][j])
                    start.append(-X[0][1][(2 * 0 + 3 * 1) % 5][(k + gama[0][1]) % 64][j])
            loc.append([0, (2 * 0 + 3 * 0) % 5, (k + gama[0][0]) % 64])
            loc.append([1, (2 * 0 + 3 * 1) % 5, (k + gama[0][1]) % 64])
        if k in loc_b_2:
            for j in range(3):
                if j == 2 or j == 0:
                    start.append(X[0][0][(2 * 2 + 3 * 0) % 5][(k + gama[2][0]) % 64][j])
                    start.append(X[0][1][(2 * 2 + 3 * 1) % 5][(k + gama[2][1]) % 64][j])
                else:
                    start.append(-X[0][0][(2 * 2 + 3 * 0) % 5][(k + gama[2][0]) % 64][j])
                    start.append(-X[0][1][(2 * 2 + 3 * 1) % 5][(k + gama[2][1]) % 64][j])
            loc.append([0,(2*2+3*0)%5,(k + gama[2][0]) % 64])
            loc.append([1,(2*2+3*1)%5,(k + gama[2][1]) % 64])
    for i1 in range(64):
        for i2 in range(5):
            for i3 in range(5):
                start.append(X[0][i2][i3][i1][2])
                if [i2,i3,i1] not in loc:
                    set_gray(m,X[0][i2][i3][i1],start)

    #设置自由度消耗
    for r in range(rounds):
        if r==0:
            for x in range(5):
                for z in range(64):
                    if z in [0,3,8,18,21,28,29,30,38,43,50,52,53,61,62,63] and x==0:
                        start.append(fr_c[r][x][z])
                    elif z in [0,7,8,9,10,21,24,27,31,35,36,38,41,42,44,46,48,49,57,63] and x==1:
                        start.append(fr_c[r][x][z] )
                    else:
                        start.append(-fr_c[r][x][z] )
                    start.append(-fr_d[r][x][z] )
                    for y in range(5):
                        if z in [12,19,48,55,62] and x==0 and y==0:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [14,35,56] and x==1 and y==3:
                            start.append(fr_y[r][x][y][z] )
                        else:
                            start.append(-fr_y[r][x][y][z] )
        if r==1:
            for x in range(5):
                for z in range(64):
                    if z in [46] and x==4:
                        start.append(fr_c[r][x][z])
                    elif z in [47] and x==2:
                        start.append(fr_c[r][x][z] )
                    else:
                        start.append(-fr_c[r][x][z] )
                    start.append(-fr_d[r][x][z] )
                    for y in range(5):
                        if z in [29,37,46] and [x,y]==[0,0]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [15,17,38,47] and [x,y]==[0,2]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [10,18,27,61] and [x,y]== [1,1]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [10,40] and [x,y]==[1,2]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [5,37,39,60] and [x,y]==[1,3]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [4,13,47] and [x,y]==[2,0]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [35,48,56] and [x,y]==[2,1]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [11,19,28,62] and [x,y]==[2,2]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [3,5,26,35] and [x,y]==[2,3]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [15,17] and [x,y]==[3,0]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [11,20,52,54] and [x,y]==[3,1]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [16,29,37,46] and [x,y]==[3,2]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [24,45,54] and [x,y]==[3,4]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [2,10,19] and [x,y]==[4,0]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [25,46,55] and [x,y]==[4,1]:
                            start.append(fr_y[r][x][y][z] )
                        elif z in [2,15,23,32] and [x,y]==[4,4]:
                            start.append(fr_y[r][x][y][z] )
                        else:
                            start.append(-fr_y[r][x][y][z] )
    return [num,start]

#描述线性部分  X->C  C->D D->Y
def f1(m,X,C,D,Y,fr_c,fr_d,fr_y,rounds):
    # X->C色块传播
    for r in range(rounds):
        for x in range(5):
            for z in range(64):
                eq= [[0, 0, 1, 0, 0, -1], [0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 1, -1], [1, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, -1], [-1, -1, -1, -1, -1, 1]]
                constr(m,[X[r][x][i][z][2] for i in range(5)]+[C[r][x][z][1]],eq)
                eq = [[0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 1, 0, -1, 1], [0, 0, 0, 1, 0, 0, -1, 1], [1, 0, 0, 0, 0, 0, -1, 1], [0, 0, 1, 0, 0, 0, -1, 1], [0, 1, 0, 0, 0, 0, -1, 1], [-1, -1, -1, -1, -1, 0, 1, 0], [-1, -1, -1, -1, -1, 0, 0, -1]]
                constr(m, [X[r][x][i][z][0] for i in range(5)] + [C[r][x][z][1]]+[C[r][x][z][0]]+[fr_c[r][x][z]], eq)
    # C->D色块传播
    for r in range(rounds):  # 遍历轮数
        for x in range(5):  # 遍历x
            for z in range(64):  # 遍历z
                eq= [[1, 0, -1], [0, 1, -1], [-1, -1, 1]]
                constr(m, [C[r][(x - 1) % 5][z][1], C[r][(x + 1) % 5][(z - 1) % 64][1],D[r][x][z][1]], eq)
                eq= [[0, 0, 0, 1, -1], [0, 0, 1, -1, 0], [0, 1, 0, -1, 1], [-1, -1, 0, 1, 0], [-1, -1, 0, 0, -1], [1, 0, 0, -1, 1]]
                constr(m, [C[r][(x - 1) % 5][z][0], C[r][(x + 1) % 5][(z - 1) % 64][0],D[r][x][z][1],D[r][x][z][0],fr_d[r][x][z]], eq)
    # D->Y
    for r in range(rounds):  # 遍历轮数
        for z in range(64):  # 遍历z
            for x in range(5):  # 遍历x
                for y in range(5):  # 遍历y
                    eq = [[1, 0, -1], [0, 1, -1], [-1, -1, 1]]
                    constr(m, [X[r][x][y][z][2], D[r][x][z][1], Y[r][x][y][z][2]], eq)
                    eq= [[0, 0, 0, 1, -1], [0, 0, 1, -1, 0], [0, 1, 0, -1, 1], [-1, -1, 0, 1, 0], [-1, -1, 0, 0, -1], [1, 0, 0, -1, 1]]
                    constr(m, [X[r][x][y][z][0], D[r][x][z][0], Y[r][x][y][z][2], Y[r][x][y][z][0], fr_y[r][x][y][z]], eq)
                    eq= [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]]
                    constr(m, [X[r][x][y][z][1]]+[X[r][(x-1)%5][i][z][1] for i in range(5)]+[X[r][(x+1)%5][i][(z-1)%64][1] for i in range(5)]+[Y[r][x][y][z][1]],eq)

#生成拉线变换表格
def f2(L1,L3):
    L2 = [[[0, 0] for i in range(5)] for i in range(5)]
    for x in range(5):
        for y in range(5):
            L2[y][(2 * x + 3 * y) % 5] = [x, y]

    # Y->Z拉线操
    for x in range(5):
        for y in range(5):
            for z in range(64):
                L1.append(L2[x][y] + [(z - gama[L2[x][y][0]][L2[x][y][1]]) % 64])

    #Z->Y的拉线表格
    for x in range(5):
        for y in range(5):
            for z in range(64):
                for i in range(len(L1)):
                    if L1[i] == [x, y, z]:
                        L3.append([int(i / 320), int((i % 320) / 64), i % 64])

#描述非线性部分
def f3(m,Y,X,L1,rounds):
    # #Z->X
    for r in range(rounds):
        for x in range(5):
            for y in range(5):
                for z in range(64):
                    # 限制第三比特
                    eq= [[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1], [-1, -1, -1, 1]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][0] for i in range(3)] + [X[r + 1][x][y][z][0]],eq)
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][1] for i in range(3)] + [X[r + 1][x][y][z][1]],eq)
                    eq= [[1, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 1, 0, -1], [0, 0, 0, 1, 0, 0, 1, -1], [-1, -1, -1, -1, 0, -1, 0, 1], [-1, -1, -1, 0, -1, 0, -1, 1], [-1, -1, -1, -1, -1, 0, 0, 1], [-1, -1, -1, 0, 0, -1, -1, 1]]
                    constr(m, [Y[r][L1[((x+i)%5) * 320 + y * 64 + z][0]][L1[((x+i)%5) * 320 + y * 64 + z][1]][L1[((x+i)%5) * 320 + y * 64 + z][2]][2] for i in range(3)] +[Y[r][L1[((x+1)%5) * 320 + y * 64 + z][0]][L1[((x+1)%5) * 320 + y * 64 + z][1]][L1[((x+1)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[Y[r][L1[((x+2)%5) * 320 + y * 64 + z][0]][L1[((x+2)%5) * 320 + y * 64 + z][1]][L1[((x+2)%5) * 320 + y * 64 + z][2]][i] for i in range(2)]+[X[r + 1][x][y][z][2]], eq)


#统计自由度消耗
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

#设置目标函数
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



