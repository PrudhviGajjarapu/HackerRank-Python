# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    ab = list(s)
    c = []
    for i in ab:
        if i.islower():
            b = i.upper()
        elif i.isupper():
            b = i.lower()
        else:
            b = i
        c.append(b)
    d = ''.join(c)
    return d
