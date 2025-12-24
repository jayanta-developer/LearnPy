from functools import reduce

def printName(name):
    # return("Hello"+ name)
    print("Hello" + name)

# printName("Sovon")

myArr = [2,3,5,6,8,9,1,5,3,6,7,3,5]
myObj = [
        {"name":"arup","age":21},
        {"name":"rahul","age":41},
        {"name":"upandar","age":8}
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



def age(num):
    if num > 18:
        print("You are good to go!")
    else:
        print("You cun't go")    
# age(22)   


total = 0
for item in myArr:
    total = total + item
# print(total)

for val in myObj:
    print(val["name"], "is", val["age"], "years old")

