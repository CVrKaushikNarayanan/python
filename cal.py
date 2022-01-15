import datetime as dt
spac="     "
da=["sun","mon","tue","wed","thu","fri","sat"]
mon=["jan","feb","mar","apr","may","jun"
    ,"jul","aug","sep","oct","nov","dec"]
n =[31,28,31,30,31,30,31,31,30,31,30,31]
def cal(y,m):
    def day(y,m):
        t=dt.datetime(y,m,1)
        return (t.weekday())    
    mo=mon[m-1]
    fd=day(y,m)
    if y%4==0 and m==2:
        ld=29
    else:
        ld=n[m-1]
    print(spac,y,spac,mo,"\n")
    for j in da:
        print(" ",j,end="")
    print("\n")
    print(spac*(fd+1), end="")
    for i in range(1,ld+1):
        if (fd+i)%7==0:
            print("\n")
        if i<10:
            print("  ",i,end=" ")
        else:
            print(" ",i,end=" ") 
m=6
y=2021
cal(y,m)

