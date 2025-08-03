logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
Auction_data = {}
loop = True
while loop :
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    Auction_data[name] = bid
    other_bidder = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if other_bidder == "no":
        loop = False
        result_bid = 0
        result_name=""
        for Data in Auction_data:
            if Auction_data[Data] > result_bid:
                result_bid = Auction_data[Data]
                result_name = Data
        print(f"The winner is {result_name} with {result_bid}$ " )
    else:
        print("\n" * 100)










