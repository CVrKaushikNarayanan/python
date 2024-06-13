def perfect(n, ref, f=[]):
    if ref != 0:
        if n % ref == 0:
            f.append(ref)
        perfect(n, ref-1)
    elif sum(f) == n:
            print(n, ' is a perfect number')
            print()

    else:
        print(n, ' is not a perfect number')
        print()

while True:
    print('''1.Enter Number \n2.CHECK \n3.EXIT''')
    w = int(input('Enter choise :'))
    print()
    if w == 1:
        n = int(input('Enter number :'))
        print()
    elif w == 2:
        perfect(n, n-1)
    else:
        break
