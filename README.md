    # pythonandcplus
    pythonandcplus_pythoncallc
    c文件和c++文件需要编译成so文件后才能在python文件中被调用，如下：
    C:\Users\test\Desktop\pythonandcplus>g++ -o a.so -shared -fPIC a.cpp
    
    注意c文件和cpp文件的区别
    
    C:\Users\test\Desktop\pythonandcplus>gcc -o fo.so -shared -fPIC fo.c
