myfile=open("myfile.txt","w")
myfile.write("""my name is manish desai
my village name is varnoda
my city name is deesa,banaskantha""")

myfile.writelines("  again my name is manish")
myfile=open("myfile.txt","r")
print(myfile.readline())
print(myfile.read())
myfile.close()

myfile=open()