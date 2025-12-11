# input must have more than 3 lines
count = 0
top = ''
with open("input.txt",encoding ='utf-8') as f:
    mid = f.readline()
    low = f.readline()
    while(mid):
        for i in range(len(mid)):
            n = 0
            for a in [top,mid,low]:
                for j in range(-1,2):
                    if a and i+j >= 0 and i+j < len(a) and a[i+j] == '@':
                        n += 1
            if n < 5 and mid[i] == '@':
                count += 1
        top = mid
        mid = low
        low = f.readline()
print(count)