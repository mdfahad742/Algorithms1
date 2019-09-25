T = int(input())

for j in range(T):
    N = int(input())
    copy = N
    copy2 = N
    i = 1
    while copy > 0:
        lastDigit = copy % 10
        #print("lastdig", lastDigit)
        if lastDigit == 4:
            
            firstHalf = copy2 // (10 ** i)
            #print("firstHalf", firstHalf)
            secondHalf = copy2 % (10 ** (i - 1))
            #print("SecondHalf", secondHalf)
            copy2 = firstHalf * (10 ** i) + 3 * (10 ** (i-1)) + secondHalf
        copy = copy // 10
        i = i + 1
        
    print("Case #", end = '')
    print(j + 1, end = '')
    print(":", copy2, N - copy2)