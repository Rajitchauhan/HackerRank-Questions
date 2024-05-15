#  collections key values pairs.

# dt = dict()
dt = {}
dt= {'name' : 'Rajit' , 'city' : 'Agra'}
# print(dt['name']) # print the value
dt['city'] = 'Delhi' # update the values
# del dt['city']
# print(dt)
# print(type(dt))

myDict = {'name' : 'Ram' , 'age' : 10 , 'place' : 'Ayodhya'}

# for d in myDict:
#     print(f'key : {d} and val : {myDict[d]}')

# for key , val in myDict.items():
#     print(key , val)

# for key in myDict.keys():
#     print(key)

# for val in myDict.values():
#     print(val)

# dt = {1 : 4 , 2 : 1 , 3 :1}
# lt = [1 ,2 , 3 ,4 , 5 ,1  , 2 , 2 , 1  ,2  , 3]

# 1 : 3
# 2 : 4
# 3 : 2
# 4 : 1
# 5 : 1
lt = ['a' , 'b' , 'a' , 'c' , 'd' , 'd' , 'a' , 'b' , 'c']
occur = {}

for i in lt:
    if i not in occur:
        occur[i] = 1
    else:
        occur[i] += 1
    # print(occur)
print(occur)