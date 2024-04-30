def say_hello():
    print('hello')
say_hello()

def sum(int1, int2):
    return int1 + int2
print(sum(4, 5))

def avg(int1, int2):
    return (int1 + int2)/2
print(avg(3, 9))

def name(firstname, lastname):
    fullname = f"{lastname}, {firstname}"
    return fullname
print(name("Josh", "Rivera"))

def personList(firstname, lastname, gradYear, studentNum):
    listPerson = [firstname, lastname, gradYear, studentNum]
    return listPerson
print(personList("Josh", "Rivera", 2017, 891313))

# def checkEighteen(num):
#     if(num > 18):
#         print(f"{num} is greater than 18")
#     elif(num == 18):
#         print(f"{num} is 18.")
#     else:
#         print(f"{num} is less than 18.")
# checkEighteen(4)
# checkEighteen(18)
# checkEighteen(999)

def checkEighteen(num):
    return num > 18
print(checkEighteen(4))
print(checkEighteen(18))
print(checkEighteen(999))

def reverse(string):
    #Had to google this one
    # return string[::-1]
    print(string[::-1])
# print(reverse("Oh no don't reverse me!"))