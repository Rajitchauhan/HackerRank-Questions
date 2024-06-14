# i = 1
# while(i<=10):
#     print(i)
#     i += 1

# def printNatural(i):
#     if i <= 10:
#         print(i)
#         printNatural(i+1)
# printNatural(1)

# fact = 1
# i = 1
# while(i <= 5):
#     fact = fact * i
#     i += 1
# print(fact)


# def printList(i):
#     if i > 10:
#         return
#     print(i)
#     printList(i + 1)
#     # print(i)

# printList(1)
# 5!  = 5 * 4 * 3 * 2 * 1 = 120
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 0! or 1! = 1

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

# i = fact(5)
# print(i)

# if i > 10:
#     return 


# printList(1) -> T 
# printList(2) -> T 
# printList(3) -> T 
# printList(4) -> T
# .................
# printList(11) -> F 
# 10
# 9
# 8
# 7
# ...
# ...
# 1
 




# def printList(i):
#     if i < 1:
#         return
#     # print(i)
#     printList(i - 1)
#     print(i)
# printList(10)
def myf(lt , target , idx):
    if (idx == -1):
        return -1
    if(lt[idx] == target):
        return idx
    return myf(lt , target , idx-1)
    
lt = [1 , 2, 3 , 4 ,5 ,6, 7,8 ,9,10]
target= 3
print(myf(lt , target , len(lt)-1))