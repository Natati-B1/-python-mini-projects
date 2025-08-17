import random
logo = """

                                                                           ,----,                                                                                                     
                                                                         ,/   .`|                                      ,--.                                                           
  ,----..                                                              ,`   .'  :  ,---,                             ,--.'|                       ____                                
 /   /   \                                                           ;    ;     /,--.' |                         ,--,:  : |                     ,'  , `.  ,---,                       
|   :     :          ,--,                                          .'___,/    ,' |  |  :                      ,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-. 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.           |    :     |  :  :  :                      |   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /| 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '          ;    |.';  ;  :  |  |,--.   ,---.          :   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' | 
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./          `----'  |  |  |  :  '   |  /     \         |   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,' 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_                '   :  ;  |  |   /' : /    /  |        '   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /   
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `.             |   |  '  '  :  | | |.    ' / |        |   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '    
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \            '   :  |  |  |  ' | :'   ;   /|        '   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |    
'   | '/  .''  :  `--'   '   |  / | /  /`--'  //  /`--'  /            ;   |.'   |  :  :_:,''   |  / |        |   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;    
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /             '---'     |  | ,'    |   :    |        '   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'     
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'                        `--''       \   \  /         ;   |.'       `--`----'   '---'           /    \  /  \   \  /           
  `---`                     `----'                                                            `----'          '---'                                     `-'----'    `----'            
                                                                                                                                                                                      




"""

print(logo)
print("Wellcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

number = random.randint(1,101)
difficulty = input("Choose difficulty. Type 'easy' or 'hard': \n")


def checking (answer,guess,attempt):
    if answer > guess:
        print("Too low.\nGuess again.")
        return attempt - 1
    elif answer < guess:
        print("Too high.\nGuess again.")
        return  attempt - 1
    else:
        print(f"You got it! The actual answer is {attempt}")
        return "DONE"



def game ():

    if difficulty == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")

    guessed_number = 0
    while guessed_number != number:
        guessed_number = int(input("Make a guess:"))
        result = checking(number, guessed_number, attempts)
        attempts -= 1
        if attempts == 0:
            print("You've running out of attempts.")
            guessed_number = number
        elif result == "DONE":
            print("DONE")
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")


game()














