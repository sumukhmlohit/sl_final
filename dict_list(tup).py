dict={37:97,39:100,25:50}
li=[]
li=[(k,v) for k,v in dict.items()]

print(li)

li.sort(key=lambda x:x[1])
print(li)
