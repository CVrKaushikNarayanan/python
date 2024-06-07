def bs(arr, x, start, end):
    mid = (start+end)//2
    if end >= start:
        if x == arr[mid]:
            print('Found')
        else:
            if x > arr[mid]:
                bs(arr, x, mid+1, end)
            else:
                bs(arr, x, start, mid-1)
    else:
        print('Not Found')


while True:
    print('''
1. ACCEPT
2. SORT
3. SEARCH
4. EXIT
''')
    w = int(input('Enter choice :'))
    if w == 1:
        l = eval(input('Enter list :'))
        print()
        #bs(l, x, 0, len(l)-1)
    elif w == 2:
        l.sort()
        print('List sorted')
        print(l)
        print()
    elif w == 3:
        x = int(input('Enter number to be searched :'))
        bs(l, x, 0, len(l)-1)
    else:
        break
