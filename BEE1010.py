#Reading the code, unit and price of product 1
item_1 = input().split(" ") # split function soman bave vag kore space create kore
#print(item_1)

#Reading the code, unit and price of product 2
item_2 = input().split(" ")

code_1, unit_1, price_1 = item_1

code_2, unit_2, price_2 = item_2


total_price = ( ( int(unit_1) * float(price_1) )
              + ( int(unit_2) * float(price_2) ) )

print('VALOR A PAGAR: R$ %0.2f' %total_price)