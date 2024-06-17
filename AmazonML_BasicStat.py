n = int(input("list Size"))
k1 = list(map(int,input().split()))
def basicStat(n,arr):
    arr.sort()
    d = {}
    s = 0
    print(arr)
    if n%2==0:
        med = (arr[n/2]+arr[n/2 - 1])/2
    else:
        med = arr[n//2]
    for i in arr:
        s += i
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    v = list(d.values())
    k = list(d.keys())
    maxi = max(v)
    m =  []
    for i in range(len(k)):
        if v[i]==maxi:
            m.append(k[i])

    mode = min(m)
    mean = s/n
    print(f'{mean:.6f},{med:.6f},{mode:.6f}')
basicStat(n,k1)

    
        
         
     
        
