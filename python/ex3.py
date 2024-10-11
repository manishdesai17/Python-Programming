import re
s1="""The university was founded on 18 October
1920 as a 'Rashtriya Vidyapith'Ty ('National University')
by Mahatma Gandhi"""

p1=r"\d{4}"
print(re.findall(p1,s1))

p1=r"\d"
print(re.findall(p1,s1))

p1=r"\d+"
print(re.findall(p1,s1))

p1=r"\w"
print(re.findall(p1,s1))

p1=r"\w+"
print(re.findall(p1,s1))

#any non digit
p1=r"\D"
print(re.findall(p1,s1))

s2="""Born and raised in a Hindu family in coastal Gujarat,
Gandhi trained in the law at the Inner Temple
in London and was called to the bar in June 1891, at the age of 22."""

#\A start to end line find begin
p2=r"\ABorn.*"
print(re.findall(p2,s2))

#any space
p2=r"\s"
print(re.findall(p2,s2))

#not any space
p2=r"\S"
print(re.findall(p2,s2))

