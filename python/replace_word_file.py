#replace any word in string using comand line
import sys
myfile=open(sys.argv[1],"r+")
line=myfile.read()
print("before modify....")
print(line)
modify=line.replace("gujarat",sys.argv[2])
myfile.close()
myfile=open(sys.argv[1],"w+")
myfile.write(modify)
myfile.seek(0)
print("after modify......")
print(myfile.read())
myfile.close()
