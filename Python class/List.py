# print("list")

# 5 ->
# [1 , 4 , 9 , 16 , 25]
# new_list = [expression for item in iterable if condition]

# square = [i*i for i in range(1 , 6)]
# print(square)
# even = [e for e in range(1 , 11) if e % 2  ==0]
# print(even)

# even_odd = ['even' if num % 2 == 0 else 'odd' for num in range(1 , 11)]








# sequence[start:stop:step]
# lt = [1 ,2  ,3 ,4 ,  5 ,6  ,7 ]
# print(lt)
# # [2  ,3 ,4 ,  5]
# # lt[start:stop:step]
# print(lt[1:])
# print(lt[2:])
# print(lt[1:5])
# print(lt[::-1])

# tp  = ()

# tp1 = (1  , 2, 3)
# print(tp1)
# tp1[1] = 10
# print(tp1)

# s = "ABCDCDC"
# s.find("D")
# sub = "CDC"
# o/p = 2

# count = 0
# s in sub -> s.find("CDC" , 6) :: 2 
#      0 1 2 3 4 5
# s = "B A N A N A" len = 6
#                y            
     
# yashi (vowels) : 0 + (6-1) + (6-3) + (6-5) = 9 
# Mehak (consonents): 0 + (6-0) + (6-2) + (6-4) =  12


# def fun(*args):
#     for i in args:
#         print(i)
#     print(type(args))
        
# fun(1 , 2 , 4 , 8 , 9 , 7  , "o" , 90.98 , True)

def fun(**kwargs):
    for k , v in kwargs.items():
        print(f"key {k} :: val {v}")
        
        
fun(name="Ram" ,)
    