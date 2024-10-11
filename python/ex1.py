#use reg functions

import re
from re import split
s1="""The university was founded on 18 October
1920 as a 'Rashtriya Vidyapith'Ty ('National University')
by Mahatma Gandhi"""

#compile
# using d+ 1999 89 99 9
p=re.compile('\d+')
print(p.findall(s1))

#using w+ any word like [i,manish,desai]
p=re.compile('\w+')
print(p.findall(s1))
#find b-c character
p=re.compile('[b-c]')
print(p.findall(s1))

#split w+ saparate word
s2="my name is manish desai"
s2="my birth date 17 november 2003"
p1="\W+"
print(split(p1,s2))
#no skip and split
p1="\d+"
print(split(p1,s2))

#escape saparate word using  \
print(re.escape(s2))

#search
p1="\d+"
print(re.search(p1,s2))


