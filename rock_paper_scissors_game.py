import random



user_input=int((input("What do you choose? Type 0 for rock , 1 for paper or 2 for scissors")))


rock= '''                 _    
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''

paper = '''  _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
|_|         |_|              '''

scissors = '''           _                        
 ___  ___(_)___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ /
|___/\___|_|___/___/\___/|_|  |___/   '''



list_of_item =list( [rock,paper,scissors])
computer=random.randint(0,2)

if user_input == 0:
    if computer == 0:
        print(f"computer: {rock}\n")
        print(f"you choose: {rock}\n")
        print("you're tied start again")
    elif computer == 1:
        print(f"computer: {paper}\n")
        print(f"you choose: {rock}\n")
        print("you lose")
    elif computer == 2:
        print(f"computer: {scissors}\n")
        print(f"you choose: {rock}\n")
        print(" you win")
if user_input == 1:
    if computer == 0:
        print(f"computer: {rock}\n")
        print(f"you choose: {paper}\n")
        print("you win")
    elif computer == 1:
        print(f"computer: {paper}\n")
        print(f"you choose: {paper}\n")
        print("you're tied start again")
    elif computer == 2:
        print(f"computer: {scissors}\n")
        print(f"you choose: {paper}\n")
        print(" you lose")
if user_input == 2:
    if computer == 0:
        print(f"computer: {rock}\n")
        print(f"you choose: {scissors}\n")
        print("you lose")
    elif computer == 1:
        print(f"computer: {paper}\n")
        print(f"you choose: {scissors}\n")
        print("you win")
    elif computer == 2:
        print(f"computer: {scissors}\n")
        print(f"you choose: {scissors}\n")
        print(" you're tied start again")




