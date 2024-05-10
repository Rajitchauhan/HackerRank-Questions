

# num = 10 (1010)
# 1010 >> 2 = 10 (2)
# print(num << 2)
# print(num >> 2)


# is not is
# a = [1 ,2 , 3]
# b = [1 ,2 , 3]
# a = [1 ,2 ,3 , 4]
# c = a

# print(a is b)
# print(a is not b)


# membership operator (in  , not in)
# a = [1 ,2 ,3 , 4]
# # print(1 in a)
# print(10 in a)
# print(10 not in a)

# num = 10

# if num > 20:
#     print("bada hai")
#     # agr mai kuch bhi , koi bhi statement vo if block mai hi ayega

# print("kuch bhi kro")

# num = 10
# if num > 0:
#     print("bada hai")
# else:
#     print("chhota hai")

# num = 10
# if num > 11:
#     print("bada hai")
# else:
#     print("chhota hai")

# calculator

a = int(input("enter first num :: "))
b = int(input("enter first second :: "))
c = input("please press '+' or '-' or '/' or '//' or '*' or '**'")
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '/':
    print(a/b)
elif c == '//':
    print(a//b)
elif c == '*':
    print(a*b)
elif c == '**':
    print(a**b)
else:
    print("invalid choice")
    
