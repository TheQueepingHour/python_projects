def hello():
    print("Greetings user!")

def pack(gear1, gear2, gear3):
    return [gear1, gear2, gear3]
print(pack("Flashlight", "Matches", "Flask"))

def eat_lunch(lunch_list):
    #Had to google this one
    if not lunch_list:
        print("My lunch box is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")
        for foods in lunch_list[1::]:
            print(f"Next I eat {foods}")

eat_lunch([])
eat_lunch(["Salad", "Steak", "Fruits"])