li=[]

class sentrev:
    
    def __init__(self,sen):
        self.sen=sen
        
        
    def sentrev(self):
        newsen=[]
        
        newsen=self.sen.split(" ")

        print(newsen)
        newsen.reverse()
        print(newsen)       
        newsent=""
        for i in newsen:
            newsent=newsent+i+" "

        print(newsent)

        li.append(newsent)
        print(li)

    def vowelcount(self):
        vowel=['A','E','I','O','U','a','e','i','o','u']
        vcount=0
        di={}
        for i in li:
            print(i)
            for x in i:
                if x in vowel:
                    vcount=vcount+1
            di[i]=vcount

        print(di)
        di=sorted(di.items(),key=lambda z:z[1],reverse=True)
        print(di)
for i in range(3):
    sen=input('Enter a sentence')
    o1=sentrev(sen)
    o1.sentrev()

o1.vowelcount()
