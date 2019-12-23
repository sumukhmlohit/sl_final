di={}
import functools
str=""
i=0
li=[]
with open('fil.txt',"r") as f:
    li=[word for line in f for word in line.split(" ")]    

print(li)

for x in li:
    if x not in di:
        di[x]=1
    else:
        di[x]=di[x]+1

print(di)

print('Dictionary sort')
newdi=sorted(di.items(),key=lambda x:x[1],reverse=True)
print(newdi)

print('Dictionary to list')
li=list(di.values())
print(li)

print('Average length')
newli=functools.reduce(lambda x,y:(x+y)/2,li)
print(newli)

print('Squares of odd nos')
li2=[i*i for i in li if i%2!=0]
print(li2)
