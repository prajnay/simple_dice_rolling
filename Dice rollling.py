import random

def start():
    result=random.randint(1,6)
    print("program is rolling a dice")
    print("program just finished rolling the dice and the result was")
    print(result)
    roll_again=input("Do you wanna roll again?(y/n)")
    if roll_again == "y":
        print('You decided to roll again')
        start()
    else:
        print('You either seleted no or typed something else so the program is going to close')


start()
