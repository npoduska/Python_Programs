logo = '''
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

bids={}
bidding_done = False

# Function to find the highest bidder
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # {"Name": 123, "Name2": 124, etc}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}. Congratulations!")
    
    
while not bidding_done:
    name = input("Enter Name: ")
    price = int(input("Enter Bid: $"))
    bids[name] = price
    ask= (input("Are there any more bidders? Type 'yes' or 'no'.")).lower()
    if ask == "no":
        bidding_done = True
        print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
        highest_bidder(bids)
    elif ask == "yes":
        print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")

