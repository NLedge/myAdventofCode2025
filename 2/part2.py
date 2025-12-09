import re
with open('input',encoding='utf-8') as f:
    line = re.split('[-,]',f.readline().strip())
# trusting input to be /([0-9]+-[0-9]+,)*[0-9]+-[0-9]/
i = 0
s = 0
primes = [2,3,5,7,11,13,17,19]
dubcomp = [6,10,12,14,15,20]
check = primes + dubcomp
while(i+1 < len(line)): # loop over ranges
    a = int(line[i])
    b = int(line[i+1])
    log = len(line[i])
    while(log <= len(line[i+1])):
        if(log > 20):
            raise(exception("Big numbers"))
        for p in check: # loop over primes
            if(log % p != 0):
                continue
            sz = log // p
            left = a * 10**sz // 10 ** log
            n = 0
            for digit in range(p):
                n *= 10**sz
                n += left 
            if(n < a):
                n = 0
            while(n <= b and left < 10**sz):
                if(p in primes):
                    s += n
                if(p in dubcomp):
                    s -= n
                left += 1
                n = 0
                for digit in range(p):
                    n *= 10**sz
                    n += left
        a = 10**log
        log +=1
    i +=2
print(s) # 22617871034
