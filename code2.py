T = int(input())

for i in range(T):
    N = int(input())
    
    str1, ch = input().split(" ")
    ch = ch[0]
    c = 0
    len1 = len(str1)
    x = str1.find(ch)
    y = str1.rfind(ch)
    
    for i in range(len1):
        #s = str1[i : ]
        #print("s1", s)
        len2 = len1 - i
        
        if y >= i:
          c = c + 1
          #print("c", c)
        #print("c y i", c, y, i)
        x = x - i;
        if len2 >= 2:
            noofsubs = len2 - 1
            ans = noofsubs
            if x >= 0:
                ans = noofsubs - x
                
                #print("ans, i, noofsubs", ans, i, noofsubs)
            c = c + ans
        x = x + i
            
            
#    for i in range(len1 - 1, 0, - 1):
#        s2 = s[0 : i]
#        print("s2", s2)
#        if ch in s2:
#            c = c + 1
#    
    print(c)