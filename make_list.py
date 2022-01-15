from vpython import *
import math
import copy 
from rate import *

p=[]
def make_list(planet1):
    # q=sun.pos
    w=planet1.pos
    # dis=math.sqrt( (q.x-w.x)**2 +(q.y-w.y)**2 +(q.z-w.z)**2 )
    dis=mag(planet1.pos)
    print('%0.5f'%dis)
    x=copy.deepcopy('%0.5f'%dis)
    # print(x)
    if len(p)==0:
        p.append(x)
    elif p[0]!=x:
        p.append(x)
    c=0
    if pause is False and c==0:
        print(p)
        c=1
