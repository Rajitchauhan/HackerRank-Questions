
def text_wrap(s , w):
    res  = ""
    n = len(s)
    for i in range(0 , n , w):
        res += s[i:i+w]
        res += "\n"
    return res 


s = input()
w = int(input())

print(text_wrap(s , w))