def palindrom(st):
    #write  you code here
    n = len(st)
    i , j = 0  , n-1
    while(i <= j):
        if st[i] != st[j]:
            return False
        i = i + 1
        j = j - 1       
    return True

res = palindrom(input())
print(f"given input is palindrom " , res)

# 0 1 2 3 4
# n a m a n len -> 5 
#   j   i
  
    
  
# y a s h 
# i     j
  

