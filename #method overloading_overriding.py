#method overloading
class Overloading:
    def add(self,a,b=0):
     return a+b
    
ob1 = Overloading()
#print(ob1.add(5))
#print(ob1.add(9,2))

#method overriding
class Parent:

   def add(self,a,b):
      return a+b
   
class Child(Parent):
   def add(self,a,b):
      return a-b
   
obj1 = Child()
print(obj1.add(3,4))

obj2 = Parent()
print(obj2.add(2,3))
   