import functools

li=[]

for i in range(6):
    li.append(int(input('Enter the element')))
li1=[]
print(li)
li1=[i*3 for i in li]

print(li1)

print(functools.reduce(lambda x,y:x+y,li))
print(functools.reduce(lambda x,y:x+y,li1))

