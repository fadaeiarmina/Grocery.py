inventory = {
    "apple" : 3.22,
     "cheese": 12.12, 
     "pasta" : 1.78, 
     "coffee" : 3.56, 
     "peanuts" : 4.20,
     "butter" : 5.85
    }
print("the inventory has apple, cheese, pasta, coffee,peanuts,butter") 
chosen_product = input ("please choose an item from the inventory: ")
chosen_quantity = input ("and how many do you want?...")

price = inventory [chosen_product]
total_price = price * int (chosen_quantity)
print ("that is going to cost you $" , total_price)
