import time
from b_function import *

oldtime=time.time()


M =8


loc_cb1= [0, 3, 6, 8, 17, 20, 22, 25, 28, 31, 34, 42, 45, 47, 50, 53, 56, 59]
loc_cb2= [0, 3, 6, 8, 17, 20, 22, 25, 28, 31, 34, 42, 45, 47, 50, 53, 56, 59]
condition_num= 44
loc_R= []
loc_B= [[0, 0], [0, 1], [3, 0], [3, 1], [6, 0], [6, 1], [8, 0], [8, 1], [17, 0], [17, 1], [20, 1], [20, 4], [22, 0], [22, 1], [25, 0], [25, 1], [28, 0], [28, 1], [31, 0], [31, 1], [34, 1], [34, 4], [42, 0], [42, 1], [45, 0], [45, 1], [47, 0], [47, 1], [50, 0], [50, 1], [53, 0], [53, 1], [56, 0], [56, 1], [59, 1], [59, 4]]
rounds= 2
start_red= 44
start_blue= 18


consum_red = start_red-start_blue
F(M,start_red,start_blue,condition_num,consum_red,loc_B,loc_R,loc_cb1,loc_cb2,rounds,2)

newtime=time.time()
print("condition_num=",condition_num,"\n")
print(newtime-oldtime)