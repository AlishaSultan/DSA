# Dict = {1:'Alisha',2:'Alia'}
# print(Dict)
# print(type(Dict))

Dict = {}
print(Dict)

Dict = {'Hello' : 1, "World":2}
print(Dict)

Dict = {1: [1,2,3,4,5],2:"World"}
print(Dict)

#Adding Elements to the Dictionary:
Dict = {}
Dict[0] = "Hello"
Dict[1] = "World"
print(Dict)

Dict[3] = {'Geeks':{'0':'absent','1':'present'}}
print(Dict)

#Update
#Dict[3] = {1:'bye'}
#print(Dict)

#Access the Elements
print(Dict[1])
print(Dict[3]['Geeks'])

#Delete:
del(Dict[3])
print(Dict)

