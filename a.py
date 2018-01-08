#!/user/bin/env python
#coding=utf-8

from ctypes import *
import time

if __name__=='__main__':
    time_begin=time.clock()

    dll=CDLL("./a.so")
    print(dll.add(2,6))
    dll.print_sum(10000)

    t=time.clock()-time_begin
    print("\nuse_time : %s"%t)
