li=[]
n=int(input('Enter no of elements'))
for i in range(n):
    x=int(input('Enter the element'))
    li.append(x)
print(li)
print(max(li))
print(min(li))
x=int(input('Enter element to insert'))
li.append(x)
x=int(input('Enter element to delete'))
li.remove(x)
print(li)
x=int(input('Enter element to search'))
if x in li:
    print('Element present')
else:
    print('Element not present')
