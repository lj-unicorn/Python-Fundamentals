#TODO-1: Ask the user for input
#TODO-2: Save data into dictionary {name: price}
#TODO-3: Wheater if new bids need to be added
#TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    highest_amount = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with amount of {highest_amount}")

bids = {}

continue_bidding = True
while continue_bidding:
  name = input("What is your name? \n")
  price = int(input("What is your bid amount? $: "))
  bids[name] = price
  next = input("Is there any other bidders y/n? \n")
  if next == "n":
    continue_bidding = False
    find_highest_bidder(bids)
  elif next =="y":
     print("\n"* 20)




