import re
with open('input',encoding='utf-8') as f:
    line = re.split('[-,]',f.readline().strip())
# trusting input to be /([0-9]+-[0-9]+,)*[0-9]+-[0-9]/
i = 0
s = 0
while i+1 < len(line):
    log = (len(line[i]) + 1) // 2
    if len(line[i]) % 2 == 1:
        left = 10**(log-1)
    else:
        left = int(line[i][:log])
        if left < int(line[i][log:]):
            left += 1
    n = left * 10**log + left
    if(n < int(line[i])):
        raise(exception("ya messed up son"))
    b = int(line[i+1])
    while(n <= b):
        s += n
        left += 1
        if(left == 10**(log)):
            log +=1
        elif(left > 10**(log)):
            raise(exception("ymus"))
        n = left * 10**log + left
    i += 2
print(s)
