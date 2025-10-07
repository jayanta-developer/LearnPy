from functools import reduce

def printName(name):
    # return("Hello"+ name)
    print("Hello" + name)

# printName("Sovon")

myArr = [2,3,5,6,8,9,1,5,3,6,7,3,5]
myObj = [
        {"name":"a","age":21},
        {"name":"r","age":41},
        {"name":"u","age":8}
    ]

# def multipal(num):
#     return num * 2

# res = map(multipal, myArr)
# print(list(res))

# filter
res = [x for x in myArr if x == 5]

# find
res1 = next((x for x in myArr if x == 5), None)

# totalVal = reduce(lambda a,b: a+b, myObj,0)

for man in myObj:
    print(man["name"], man["age"])