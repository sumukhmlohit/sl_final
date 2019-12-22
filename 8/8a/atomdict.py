di={}
n=int(input('Enter no of elements'))

for i in range(n):
    symbol=input('Enter atomic symbol')
    name=input('Enter element name')
    di[symbol]=name

print(di)

count=0

for i in di:
    count=count+1

print(count)

x=input('Enter element to search')

if x in di:
    print('Element present')
else:
    print('Element not present')
