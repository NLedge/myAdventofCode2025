s = 0
with open("input",encoding ='utf-8') as f:
    for line in f:
        a = b = 0
        for n in reversed(str(line)):
            if(n == '\n'):
                continue
            n = int(n)
            if(b == 0):
                b = n
                continue
            if(a == 0):
                a = n
                continue
            if n >= a:
                if a > b:
                    b = a
                a = n
            print('\r',end='',)
            print(a,end='')
            print(b,end='',flush = True)
        s += a * 10 + b
print('')
print(s)
