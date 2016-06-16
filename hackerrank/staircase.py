x = input()

def staircase(n):
    for i in range(n-1,-1, -1):
        print i*' ' + '#'*(n-i)

staircase(x)