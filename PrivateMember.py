class PrivateMember:

    def __init__ (self,value):
        self.__value = value  #Private attribute

    def getValue(self):
        print("Print",self.__value)

obj1 = PrivateMember(10)
#print(obj1.__value)
obj1.getValue()