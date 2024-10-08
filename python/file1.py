import sys
myfile=open(sys.argv[1],"r")
r=myfile.read()
print(r)
myfile.close()

myfile=open(sys.argv[2],"w+")
myfile.write(r)
myfile.seek(0)
print(myfile.read())
myfile.close()