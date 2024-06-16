n = int(input("Number of Elements"))
k=[]
for i in range(n):
    k.append(int(input("-->")))
    
def mini(i,n):
    if(i+3<len(n)):
        a=abs(abs(n[i])-abs(n[i+1]))
        b=abs(abs(n[i])-abs(n[i+3]))
        if(a<b):
            return i+1,a
        elif(b<a):
            return i+3,b
        else:
            i1,c1 = mini(i+1,n)
            i2,c2 = mini(i+3,n)
            if c1<c2:
                return i1,c1+a
            else:
                return i2,c2+b
    else:
        return i+1,abs(abs(n[i])-abs(n[i+1]))

    
def sd(n):
    c = 0
    i = 0
    while(i<len(n)-1):
        i,b = mini(i,n)
        c+=b
        #print(i,c)
    print(c)
sd(k)
