import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []
dealer_card = []

def compare (p_score , d_score):
    if p_score > 21:
        return "You went over. You lose 😭"
    elif d_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score == d_score:
        return "Draw 🙃"
    elif p_score < d_score:
        return "You lose 😤"
    elif p_score > d_score:
        return "You win 😃"
    else:
        return "you lose 😤"


def play_game ():
    print(logo)

    for i in range(2):
        player_card.append(random.choice(cards))
        i += 1
    dealer_card.append((random.choice(cards)))

    print(f"    You're cards: {player_card}, current score: {sum(player_card)}")
    print(f"    computer's first card: {dealer_card}")

    loop = True
    while loop:
        additional_card = input("Type 'y' to get another card, type 'n' to pass:\n")

        if additional_card == 'y':
            player_card.append(random.choice(cards))

            if 11 in player_card and sum(player_card) > 21:
                player_card.remove(11)
                player_card.append(1)

            print(f"    You're cards: {player_card}, current score: {sum(player_card)}")
            print(f"    computer's first card: {dealer_card}")

            if sum(player_card) > 21:
                loop = False
                print ("You went over. You lose 😭")
        else:
            loop = False
            while sum(dealer_card) <= 17:
                dealer_card.append(random.choice(cards))

            print(f"    You're final hand: {player_card}, final score: {sum(player_card)}")
            print(f"    computer final card: {dealer_card}, final score: {sum(dealer_card)}")
            print(compare(sum(player_card), sum(dealer_card)))

    return None


user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if user == 'y':
    play_game()















