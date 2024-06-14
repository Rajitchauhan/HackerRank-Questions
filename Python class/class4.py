#loops in python

# print("1")
# print("2")
# print("3")
# .........
# .........
# print("10")

# print(1 in range(5))
# print(2 in range(5))
# print(6 in range(5))


# print(r.next())
# print(r.next())

# for i in range(5): range(start , stop  , step) , range(0 , 10 , 1)
# for (starting ; condition; iteration) {  }
# print(range(10))
# for i in range(10):
#     print(i)
    
# for i  in range(2 , 21 , 2):
#     print(i)

# i = 1

# while(i <= 10):
#     print(i)
#     i += 1

# for i in range(10 , 0  , -1):
#     print(i)

# for i in range(5):
#     for j in range(5):
#         print(i , end=" ")
#     print()


# for i in range(5):
#     for j in range(4):
#         print(j , end=" ")
#     print()

# for i in  range(1 , 5):
#     for j in range(1 , 5):
#         print("@" , end  =" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1 , 5):
#     for j in range(1 , i):
#         print(i , end=" ")
#     print(i)
    
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# n=4
# for i in range(4 , 0 , -1):
#     for j in range(i):
#         print(i , end=" ")    
#     print()
    
# n -> input = 5
# 1 -> n (1 to 5) 1 + 2 + 3 + 4 + 5 = 15

# p = lambda : print("hello")
# print(p())
# def add(a , b):
#     return a+b

# add = lambda a , b : a+b
# print(add(12 , 24))

# local  and global  var
# global x 
# gb =20
# def test():
#     lb = 10
#     print(lb)
#     print(gb)

# test()
# print(gb)
# x = 10
# def mohit():
#     print(x)
# mohit()
# print(x)

# def fun1():
#     print("this is outer fun")
#     x = 10
#     def fun2():
#         print("this is inner fun")
#         nonlocal x
#         x = x+1
#         print(x)
#     fun2()
# fun1()

# def add(x , y):
#     x = x+1
#     y = y*2
#     print(x)
#     print(y)
# def getVal(x , y):
#     print(x , y)
#     add(x , y)
# getVal(10 , 20)

# x = 10
# def update():
#     global x
#     x = x + 10
#     # print(x)
# update()
# print(x)

a = 10
b = 10
def update(a , b):
    a += 2
    b += 2
    print(a , b)
def val(a , b):
    print(a , b)
    a += 1
    b += 1
    update(a , b)   
val(a , b)
print(a , b)
