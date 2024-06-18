def m1():
    global r,b
    b = b+r[0]
    r = r[1:]
def m2():
    global b,k
    k = k+b[-1]
    b = b[:-1]


r = input().strip()
b = ''
k = ''
r = r.lower()
m = min(r)
#print(k)
for i in r:
    #print(r,b,k)
    if i!=m:
        m1()
    elif i==m:
        m1()
        #print(r,b,k)
        m2()
        if len(r)!=0:
            m = min(r)
    else:
        break
while(len(b)>0):
    m2()


    
print(k)
