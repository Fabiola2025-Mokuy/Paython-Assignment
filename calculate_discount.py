# Calculates the final price after applying a discount. 
price = float(input("Enter the price: "))

if price >= 20:
 discount_percent = price

discount_amount = price * (discount_percent/ 100)
final_price = price - discount_amount
print ("The  final price with discount is:")
print(final_price )

    #If price < 20% , don't apply the discount; return the original price. 
else:

final_price= price
print ("final_price is" )
print(price)

#2.Print the final price after applying the discount, or if no discount was applied, print the original price.

price = float(input("Enter the price: "))
discount_percent = float(input("Enter discount_percent: "))

if discount_percent >=20:

discount_amount = price * (discount_percent/ 100)
final_price = price - discount_amount
print("The price is":)
print (price)

print("The discount_percent is:")
print (discount_percent)
print ("The  final price with discount is:")
print(final_price )
        
else:
final_price= price
print ("you have not discount becouse the price is < 20" )
print ("your price is:")
print(price)



