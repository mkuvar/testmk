import random

#random game function
def playagain():
    pg = input("Wanna play again")
    if pg == "y" or pg == "n":
        return pg
    else:
        return playagain()


playagain = playagain()
def randomgame():
    while playagain == "y":
        range = random.randint(0, 60)
        winns = 0
        data = int(input("put your numbers here ==>"))
        diff = range - data
        if range == data:
             print("you have guessed the correct number")
             winns = winns + 20
        elif diff >= -5 and diff <= 5:
             print("you are a little close to your number")
             print("The randomly generated number was ",range)
             print("your numbers were ",data)
             winns = winns + 5
        elif diff >= -10 and diff <= 10:
            print("you are a little close to your number")
            print("The randomly generated number was ", range)
            print("your numbers were ", data)
            winns = winns +20
        else:
             print("sorry you didn't make it")
             print("The randomly generated number was ",range)
             print("your numbers were ",data)
        print("You have scored ", winns)
        # userdata = input("Wanna play again")



randomgame()