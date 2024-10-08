#open write (w) mode
myfile=open("myfile.txt","w")
myfile.write("""After returning from South Africa, Gandhiji moved all over India.
 He personally experienced the political, social, 
educational and economic deteriorated conditions 
after observing life of Indian people.""")

#open read (r) mode
myfile.writelines(" \n Bapu made untiring efforts to find solution to all there problems.")
myfile=open("myfile.txt","r")
print(myfile.readline())
print(myfile.read())
myfile.close()

#open  read and write (r+) mode 
myfile=open("myfile.txt","r+")
myfile.writelines("""He made some initial experiments of education in Kochrab and
Sabarmati Ashram during 1915-1920.""")
myfile.close()

#replace any word in string 
myfile=open("myfile.txt","r+")
line=myfile.read()
modify=line.replace("Bapu","Gandhiji")
myfile.close()
myfile=open("myfile.txt","w+")
myfile.write(modify)
myfile.seek(0)
print(myfile.read())
print(myfile.tell())
myfile.close()

