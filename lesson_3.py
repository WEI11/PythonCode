#bicycles=['trek','cannondale','readline','specialized']

#print(bicycles[0])
#print(bicycles[1])
#print(bicycles[2])
#print(bicycles[3])

#message="hello"

#mes=bicycles[0]+","+message
#print(mes)

names=["Wei",'jonh','LiLin']
print(names)

name=names.pop()
print(name+" can not come.")
print(names)
name='Wang'
names.append(name)
print(names)
#print(names.pop()+"Weclome.")
#print(names.pop()+"Weclome.")
#print(names.pop()+"Weclome.")
print("find a biger table.");

names.insert(0,"Zhang")
names.insert(2,"Keke")
names.append("MiMi")
print(names)
print("sorry,two people can come.")
names.pop()
names.pop()
names.pop()
names.pop()
print(names)
del names[0]
del names[0]
print(names)

print("---------------------------------\n")
city=['Beijing','xiamen','quanzhou','dunhuang','hangzhou']
print("origin:\t")
print(city)
print(sorted(city))
print(city)
print(sorted(city,reverse=True))
print(city)

city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)

print(len(city))




