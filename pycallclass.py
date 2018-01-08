import ctypes
so=ctypes.cdll.LoadLibrary
lib=so("./libpyclass.so")
print "display()"
lib.display()
print 'display(100)'
lib.display_int(100)
