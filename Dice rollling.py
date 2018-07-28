import random
import time

def start():
    result=random.randint(1,6)#slects a random number between 1 to 6
    print("program is rolling a dice")
    time.sleep(3) #sleeps for 3 seconds 
    print("program just finished rolling the dice and the result was")
    time.sleep(1) #sleeps for 1 second
    print(result)
    roll_again=input("Do you wanna roll again?(y/n)")#ask user if he/she wants to roll the dice again
    if roll_again == "y":
        print('You decided to roll again')
        start()
    else:
        print('You either seleted no or typed something else so the program is going to close')


start()
