# -*- coding: utf-8 -*-
import random

def randomList():
    N=random.randint(0,101)
    list=range(N)
    for i in range(N):
        list[i]=random.randint(-1,2**31)
    print "N=%d"%N
    print "排序前数组为："
    print list
    list.sort()
    print "排序后数组为："
    print list
    
if __name__=="__main__":
    randomList()