import commands
import os

main="testmain.exe"
print "*"*10
f=os.popen(main)
data=f.readlines()
f.close()
print data
print "*"*10
os.system(main)
