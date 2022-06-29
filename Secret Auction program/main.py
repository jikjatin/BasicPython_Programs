from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret aution program")
bidders={}
highest=0
def aution():
  bidders[int(input("What is your bid?:"))]=input("What is your name?:")
  cont=input("Are there any other bidders? Type 'yes' or 'no':").lower()
  clear()
  if cont=="yes":
    aution()
  
aution()  
for bid in bidders:
  if bid>highest: 
    highest=bid
print(f"The winner of the bid is {bidders[highest]} with a bid of {highest}.")    
    



