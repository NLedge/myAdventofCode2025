# --- Day 1: Secret Entrance ---
# --- Part Two ---
value = 50
count = 0
max = 100

with open('input.txt',encoding='utf-8') as f:
    # lines hopefully match the regex /^[LR][0-9]+(\n|$(?!\n))/
    for line in f:
        if len(line) == 0 or len(line) > 20:
            raise(Exception('Line empty or line too long'))
        if line[0] == 'L':
            sign = -1
        elif line[0] == 'R':
            sign = 1
        else:
            raise(Exception('Line does not begin with /[LR]/'))
        if line[-1] != '\n':
            line += '\n'
        rotate = int(line[1:-1]) # expected to break on invalid input
        count += rotate // max
        rotate %= max
        if rotate == 0:
            continue
        value += sign * rotate # 0 to 99 + -99 to 99 = -99 to 198
        if value == 0:
            count += 1
        if value < 0:
            if value != -rotate:
                count += 1
            value += max
        if value >= max:
            value -= max
            count += 1
print(count)
