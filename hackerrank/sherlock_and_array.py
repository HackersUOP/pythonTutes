T = input()

for i in range(0,T):
    no_of_elements = input()
    arr = map(int, raw_input().strip().split(' '))
    print arr
    print sum(arr[0:3])