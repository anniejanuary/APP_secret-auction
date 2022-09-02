from replit import clear

from art import logo
print(logo)

bid_log = {}

print("Welcome to the Secret Auction!")

keep_going = True

def winner (bidding_record): ##  made up "bidding_record" dictionary placeholder just now that will later take bid_log dictionary as input to sift through it
    highest_bid = 0
    winner_name = ""

    for person in bidding_record:
      bidding_amount = bidding_record[person]
      if bidding_amount > highest_bid:
        highest_bid = bidding_amount 
        winner_name = person
    
    print(f"{winner_name} won the Silent Auction with a bid of ${highest_bid}!")

# finding the max bid value in a dictionary of several key-value pairs:
def add_new_bid (new_name, new_bid):    
  ## this creates: {"Kara" : 200}
  bid_log[name] = bid
    
  ## this would create : {"name" : Kara, "bid" : 200}
  # bid_log["name"] = new_name
  # bid_log["bid"] = new_bid

while keep_going:
  name = input("What's your name: ")
  bid = int(input("Enter your bid: $"))

  # finding the max bid value in a dictionary of several key-value pairs:  
  add_new_bid (name, bid)

  again = input("Would you like to add another bidder? yes/no: ")
  if again == "yes":
    clear()
  else:
    keep_going = False
    winner (bid_log)
    
    
### way 2: adding new bids as separate dictionaries inside a list
# bid_log = []

# keep_going = True
# while keep_going:
#   name = input("What's your name: ")
#   bid = int(input("Enter your bid: $"))

#   def add_new_bid (new_name, new_bid):
#     new_bid_dictionary = {}
#     new_bid_dictionary["name"] = new_name
#     new_bid_dictionary["bid"] = new_bid
#     bid_log.append(new_bid_dictionary)
#   add_new_bid (name, bid)

#   again = input("Would you like to add another bidder? yes/no: ")
#   if again == "yes":
#     clear()
#   else:
#     keep_going = False

#     # LAMBDA: finding the max bid value in a list of dictionaries
#     max_bid = max(bid_log, key=lambda x:x['bid'])
#     #print(bid_log)
#     print(f"{max_bid['name']} won the Silent Auction with a bid of ${max_bid['bid']}!")


