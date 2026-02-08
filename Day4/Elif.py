a=[11,22,33]
b=[10,20,30]
c=[111,222]

if(len(a)>len(b))and(len(a)>len(c)):
print("a is max:")

elif(len(b)>len(a))and(len(b)>len(c)):
print("b  is max:")

elif(len(c)>len(a))and(len(c)>len(b)):
print("c is max:")

else:
print("all list are equal:")
