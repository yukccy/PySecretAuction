import os
from art import logo

have_bidder = True
total_bid = []

print(logo)

while have_bidder:
    bidder_name = input("What is your name? ")
    bid_price = int(input("What is your bid price? "))
    current_bid = {"name": bidder_name, "price": bid_price}
    total_bid.append(current_bid)
    other_bidder = input("Is there other users who want to bid? yes or no. ")
    if other_bidder == "yes":
        os.system("clear")
    else:
        have_bidder = False

highest_bid_user = max(total_bid, key=lambda x: x['price'])
print(f'Congratulations! The winner is {highest_bid_user["name"]} with ${highest_bid_user["price"]} bid')