# class Student:
#     # name = "Rajit"
#     def info(self):
#         print("this is for student info")
#     def getRoll(self , roll):
#         print(f"thi s is roll {roll} ")
    
# obj = Student()
# obj.info()
# obj.getRoll(21)



# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#         print(f"name ::  {self.name} {self.age}")
# obj = Student("Rajit" , 24)
        

# class Person:
#     def basicInfo(self , name , age):
#         self.name = name
#         self.age = age
        
# class Student(Person):
#     def info(self , roll , course):
#         Person.basicInfo("Rajit , 24")
#         self.roll = roll 
#         self.course = course 
#         print(f'{self.name} : {self.age} : {self.roll} , {self.course}')
        

# class Car:
#     def info(self , name , model):
#         self.name = name 
#         self.model = model
#         print(f"this is car {self.name} :: {self.model}")

# class SportCar(Car):
#     def getInfo(self , booster , power):
#         self.booster = booster
#         self.power = power
#         print(f"this is sport car {self.booster} :: {self.power}")

# obj =SportCar()
# obj.getInfo("Booster" , "20hrs")
# obj.info("porsche" , 911)

class Person:
    def info(self , name , age):
        self.name = name
        self.age = age 
        print("name and  age is" , self.name , self.age )
        
class Student(Person):
    def __init__(self , roll, course):
        self.roll = roll 
        self.course = course 
        print("course and roll" , self.roll , self.course)
        
s = Student(21 , "Btech")
s.info("Rajit" , 24)       

# obj  = Person("Rajit" , 24)
        









