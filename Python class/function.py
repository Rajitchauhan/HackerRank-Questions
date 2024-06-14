# def functionName():
#     print("Rajit")
    
# functionName()

# def functionName(name):
#     print(name)
    
# functionName("Rajit")


# def add(a , b):
#     return a+b 

# res = add(10 , 20)
# print(res)



# class Student:
#     def info(self):
#         print("student")

# obj = Student()
# obj.info()

# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#         print(f"student :: {self.age} :  {self.name}")
        
# obj = Student("Rajit" , 24)


# class Calc:
#     def add(self , a , b):
#         self.a = a 
#         self.b = b 
#         return self.a + self.b 
#     def subtrack(self , a , b):
#         self.a = a 
#         self.b = b 
#         return self.a - self.b
#     def multi(self , a , b):
#         self.a = a 
#         self.b = b 
#         return self.a * self.b
    
# cal  = Calc()
# res = cal.add(20 , 10)
# print(res)
# res = cal.subtrack(20  , 10)
# print(res)
# res =  cal.multi(5 , 2)
# print(res)
        
# class GrandFather:
#     def base(self):
#         print("i am superior")
        
# class Father(GrandFather):
#     def get(self):
#         print("father")
        
# class Child(Father):
#     def myInfo(self):
#         print(" hey i am child  , wanna inheritance")
        
# obj = Child()
# obj.myInfo()
# obj.get()
# obj.base()

# class GautamSir:
#     def math(self):
#         print("i have a knowledge of math")
# class RajitSir:
#     def python(self):
#         print("i have a knowledge of coding")
# class  YouTube:
#     def channel(self):
#         print(" i have a lots of knowledge")
# class You(GautamSir , RajitSir , YouTube):
#     def study(self):
#         print("i am good learner") 
               
# obj = You()
# obj.math()
# obj.python()
# obj.channel()
# obj.study()

# class Intermedite:
#     def physics(self):
#         print("physics")
#     def math(self):
#         print("math")
#     def chemistry(self):
#         print("chemistry")
        
# class Btech(Intermedite):
#     def semester(self):
#         print(" 6 subject sem each ")
        
        
# class Person:
#     def __init__(self):
#         print("this is constructor")
#     def __init__(self , a):
#         self.a = a 
#         print(f"val of a  ::  {self.a}")
        
        
# p = Person(10)

# print(5/0)

# a  , b = int(input()) , int(input())
# a = 10
# b = 20
# # print(a/b)
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("zero se divide mat karo")
# except TypeError:
#     print("type alag alag h")
# else:
#     print("i am else")
# finally:
#     print("finally to chlega hi hai")



class Calc:
    def division(self , a , b):
        self.a =a
        self.b = b 
        
        try:
            return self.a / self.b 
        except ZeroDivisionError:
            return "cant division by zero"
        finally:
            print("task complete")
c = Calc()
res = c.division(20 , 5)
print(res)