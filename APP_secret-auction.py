from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

print("Welcome to the Secret Auction!")

bid_log = []

keep_going = True
while keep_going:
  name = input("What's your name: ")
  bid = int(input("Enter your bid: $"))

  def add_new_bid (new_name, new_bid):
    new_bid_dictionary = {}
    new_bid_dictionary["name"] = new_name
    new_bid_dictionary["bid"] = new_bid
    bid_log.append(new_bid_dictionary)
  add_new_bid (name, bid)

  again = input("Would you like to add another bidder? yes/no: ")
  if again == "yes":
    clear()
  else:
    keep_going = False

    # finding the max bid value in a list of dictionaries
    max_bid = max(bid_log, key=lambda x:x['bid'])
    
    #print(bid_log)
    print(f"{max_bid['name']} won the Silent Auction with a bid of ${max_bid['bid']}!")



