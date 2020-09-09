import numpy
def dot(x, y):
    return sum(x_i*y_i for x_i, y_i in zip(x, y))
def mp(x,w,b):
    y=dot(x,w)+b
    return 1 if y>=0 else 0
"---------------For 2 inputs-------------------"
x=([0,0],[0,1],[1,0],[1,1])
w=[1,1]
for i in range (0,4):
    a=mp(x[i],w,-2)
    b=mp(x[i],w,-1)
    print("Case {3}:{0};And:{1};Or:{2}".format(x[i],a,b,i+1))
"---------------For 5 inputs-------------------"
from itertools import product
inputs = list(product([1,0],repeat = 5))
w2=[1,1,1,1,1]
for i in range (0,32):
   a=mp(inputs[i],w2,-2)
   b=mp(inputs[i],w2,-1)
   print("Case {3}:{0};And:{1};Or:{2}".format(inputs[i],a,b,i+1))
"----------------For n inputs:------------------"
n=input("Enter the number of inputs:")
w=numpy.ones(int(n))
from itertools import product
inputs = list(product([0,1],repeat = int(n)))
turn=2**int(n)
for i in range (0,turn):
   a=mp(inputs[i],w,-2)
   b=mp(inputs[i],w,-1)
   print("Case {3}:{0};And:{1};Or:{2}".format(inputs[i],a,b,i+1))