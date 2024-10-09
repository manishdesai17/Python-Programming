import re
s="manishdesai@gmail.com"
x=re.search("\.",s)
print(x)

x=re.search("[@]",s)
print(x)

x=re.findall("[a]",s)
print(x)

x=re.findall("^m.*",s)
print(x)

x=re.findall("c.+",s)
print(x)

x=re.findall("^.*[@].*[.].*",s)
print(x)

#file any mobile no in string

s1="""Gujarat Vidyapith 72858 84703 was established as a national university without a government
charter. Gandhiji was its (576) 580-1984 life-long chancellor. Professor 9328304561 A T Gidwani was its founder
vice-chancellor. After Gandhiji, Sardar Vallabhbhai Patel, 9105555091 Dr. Rajendra Prasad and 
Morarji Desai (+1)207 558 0918 adorned the post of chancellor of the Vidyapith.Later, 
many more institutions, colleges and schools were affiliated to the Vidyapith."""

#9048389075
#99755 90877
#(555) 555-1234
#(+1)202 555 0118
p1=r"\d{10}"
p2=r"\d{5}\s\d{5}"
p3=r"\(\d{3}\)\s\d{3}\D\d{3}"
p4=r"\(\D\d{1}\)\d{3}\s\d{3}\s\d{4}"

all=p1+"|"+p2+"|"+p3+"|"+p4
x=re.findall(all,s1)
print(x)

s2=""" Gujarat Vidyapith was established as a national university without a
 government charter. Gandhiji manish@gmail.com was its life-long chancellor. Professor
A T Gidwani was its founder vice-chancellor.a.manish@gamil.com After Gandhiji, Sardar 
Vallabhbhai Patel, Dr. m@g.c Rajendra Prasad and Morarji Desai manish123@gmail.c adorned the
post of chancellor of the Vidyapith.Later, many more institutions, 
colleges and schools were affiliated to the Vidyapith."""

#abc@gmail.com
#a@g.c
p1=r"\w+\@\w+\.\w+"
p2=r"\w\.\w+\@\w+\.\w+"
all=p1+"|"+p2
x=re.findall(all,s2)
print(x)
