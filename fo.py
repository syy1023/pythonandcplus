import ctypes
ll=ctypes.cdll.LoadLibrary
lib=ll("./fo.so")
lib.foo(1,3)
print "***finish***"
