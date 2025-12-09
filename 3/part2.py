import collections

dozen = 12
s = 0

with open("input",encoding ='utf-8') as f:
    for line in f:
        line = str(line[:-1]) # unsafely trim newlines
        deck = collections.deque([],maxlen=dozen)
        isSorted = False
        for n in reversed(line):
            n = int(n) #unsafe
            if len(deck) < dozen:
                deck.appendleft(n)
            elif n >= deck[0]:
                if not isSorted:
                    isSorted = True
                    for i in range(len(deck)-1): # if you're going to do this, is a deque really neccesary?
                        if deck[i] < deck[i+1]:
                            deck.remove(deck[i]) # maybe not, but indexed removal and append pushing is very convenient.
                            isSorted = False
                            break
                deck.appendleft(n)
        s += int(''.join(map(str,deck)))
print(s)
