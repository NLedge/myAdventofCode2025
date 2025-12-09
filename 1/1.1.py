# --- Day 1: Secret Entrance ---
value = 50
count = 0
max = 100

with open('input.txt',encoding='utf-8') as f:
    # lines hopefully match the regex /^[LR][0-9]+(\n|$(?!\n))/
    for line in f:
        if line[0] == 'L':
            sign = -1
        elif line[0] == 'R':
            sign = 1
        else:
            raise(Exception('Line does not begin with /[LR]/'))
        if line[-1] != '\n':
            line += '\n'
        rotate = sign * int(line[1:-1]) # expected to break on invalid input
        value = (value + rotate) % max # python mod is not c mod  
        if value == 0:
            count += 1
print(count) # 1071
