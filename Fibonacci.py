#accep no, series , exit
def fib(n, first, end):
    if n>2:
        r = first+end
        print(r)
        fib(n-1, end, r)

while True:
    print('''
1. INPUT LENGTH OF THE SERIES
2. PRINT SERIES
3. EXIT
''')
    w = int(input('Enter choice :'))
    if w == 1:
        n = int(input('Enter the length of the series :'))
    elif w == 2:
        if n == 1:
            print(0)
        else:
            print(0)
            print(1)
            fib(n, 0, 1)
    else:
        break

