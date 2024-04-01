class StaticVariable:
    count = 0

    def __init__ (self):
       StaticVariable.count +=1

obj1 = StaticVariable()
print(obj1.count)
obj2 = StaticVariable()
print(obj2.count)
obj3= StaticVariable()
print(obj3.count)
print(StaticVariable.count)

