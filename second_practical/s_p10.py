#replace any word in string 
myfile=open("myfile.txt","r+")
line=myfile.read()
print("before modify....")
print(line)
modify=line.replace("Gujarat","gujrat")
myfile.close()
myfile=open("myfile.txt","w+")
myfile.write(modify)
myfile.seek(0)
print("after modify......")
print(myfile.read())
print(myfile.tell())
myfile.close()
