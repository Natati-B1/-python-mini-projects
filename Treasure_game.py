print('''Wellcome To Treasure island 
     your mission is to find the treasure''')
road = input("you're at cross road where do you want to go?"
             " type \"left\" or \"right\" ")
if road == "right" or road == "Right":
    print("Game over, you loss ")
elif road == "left" or road == "Left":
    lake = input("you've come to lake. type wait to wait for boat or swim").lower() # it covert user input to lowe cases
    if lake == "swim" :
        print("Game over, you loss ")
    elif lake== "wait" or lake== "Wait":
        door = input("There is a house with 3 doors red ,yellow and blue which one do you choose?")
        if door == "red" and door == "blue" or door == "Red" and door == "Blue":
            print("Game over, you loss ")
        elif door == "yellow" or door == "yellow":
            print("you win")


