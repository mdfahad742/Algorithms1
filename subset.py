T = int(input())

nameHandle = open('test.txt', 'r')
L = []
for line in nameHandle:
    L.append(line)
#print(L)
x = 0
for j in range(T):
    N = int(L[x])
    s = L[x + 1]
    x = x + 2
    ans = ''
    for i in s:
        if i == 'S':
            ans = ans + 'E'
        elif i == 'E':
            ans = ans + 'S'
            
    print("Case #", end = '')
    print(j + 1, end = '')
    print(":", ans)