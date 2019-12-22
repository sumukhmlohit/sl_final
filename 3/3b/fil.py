from collections import Counter
import functools

file=open("fil.txt","r")
di={}
di=Counter(file.read().split())
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
