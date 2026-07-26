items = []
prices =[]
total = 0

while True:
    food = input("What is the name of the food? (press q to quite): ")

    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food: "))
        items.append(food)
        prices.append(price)
print("Cart details: ")

for item in items:
    print(item)
for price in prices:
    total +=price

print(f"your total is ₦{total}")
