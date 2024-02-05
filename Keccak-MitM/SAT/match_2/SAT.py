

def less_count(m,num,start,x,count,mode):
    if count==0:
        for i in x:
            start.append(-i)
        return num
    s=[]
    num=variable_2(s,len(x)-1,count,num)

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
    return num

def less_count_0(m,num,start,x,count,mode):
    if count==0:
        for i in x:
            start.append(-i)
        return num
    s=[]
    num=variable_2(s,len(x)-1,count,num)

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
    return num

def constr(m,X,Y):
    for j in range(len(Y)):
        T = []
        for i in range(len(Y[j])):
            if Y[j][i]==1:
                T.append(X[i])
            if Y[j][i]==-1:
                T.append(-X[i])
        m.append(T)

def variable_1(X,x,n):
    for i in range(x):
        X.append(n+i)
    return n+x

def variable_2(X,x,y,n):
    for i in range(x):
        X.append([])
        for j in range(y):
            X[i].append(n+j+i*y)
    return n+x*y

def variable_3(X,x,y,z,n):
    for i in range(x):
        X.append([])
        for j in range(y):
            X[i].append([])
            for k in range(z):
                X[i][j].append(n+k+j*z+i*y*z)
    return n+x*y*z

def variable_4(X,x1,x2,x3,x4,n):
    for i1 in range(x1):
        X.append([])
        for i2 in range(x2):
            X[i1].append([])
            for i3 in range(x3):
                X[i1][i2].append([])
                for i4 in range(x4):
                    X[i1][i2][i3].append(n+i4+i3*x4+i2*x3*x4+i1*x2*x3*x4)
    return n+x1*x2*x3*x4

def variable_5(X,x1,x2,x3,x4,x5,n):
    for i1 in range(x1):
        X.append([])
        for i2 in range(x2):
            X[i1].append([])
            for i3 in range(x3):
                X[i1][i2].append([])
                for i4 in range(x4):
                    X[i1][i2][i3].append([])
                    for i5 in range(x5):
                        X[i1][i2][i3][i4].append(n+i5+i4*x5+i3*x4*x5+i2*x3*x4*x5+i1*x2*x3*x4*x5)
    return n+x1*x2*x3*x4*x5

def data(result,X):
    if result[X]>0:
        return 1
    else:
        return 0