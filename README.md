


    pythonandcplus
    pythonandcplus_pythoncallc
    c文件和c++文件需要编译成so文件后才能在python文件中被调用，如下：
    C:\Users\test\Desktop\pythonandcplus>g++ -o a.so -shared -fPIC a.cpp
    
    注意c文件和cpp文件的区别
    
    C:\Users\test\Desktop\pythonandcplus>gcc -o fo.so -shared -fPIC fo.c
    
    python对C/C++可执行程序的调用，生成
    可执行文件使用如下命令：
    g++ -o testmain C:\Users\Asus\Desktop\test_exe.cpp

    # cpp文件需要extern "C"来辅助，也就是说还是只能调用C函数，不能直接调用方法，但是能解析C++方法。
    # 不是用extern "C"，构建后的动态链接库没有这些函数的符号表
