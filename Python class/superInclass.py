class Parent:
    def __init__(self):
        print("this is parent method")
    def parentMethod(self , msg):
        self.msg = msg 
        print(f'message :: {msg}')
     
class Child(Parent):
    def __init__(self):
        print("this is child method  after that parent will call using super")
        super().__init__()
         
    def callParent(self):
        super().parentMethod("Karma always return")
 
c = Child()
c.callParent()        
# p = parent()
# p.parentMethod("Be good for everyone")