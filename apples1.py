amt = int (input('how muck kg. of apples u want'))

if amt >=5:
    price= 80
else:
    price = 90 
total = amt * price 
print(f"you have to pay rs.{total} for {amt} kg.of apples")  
