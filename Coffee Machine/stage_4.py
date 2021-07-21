water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550

def has():
    print("The coffee machine has :")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans")
    print(str(cups) +  " of disposable cups")
    print(str(money) + " of money")

has()
print()

print("Write action (buy, fill, take):")
action = str(input())

if action == 'buy':
    
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_name = int(input())
    
    if coffee_name == 1:
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
    
    elif coffee_name == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7

    elif coffee_name == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6

if action == 'fill':
    
    print("Write how many ml of water do you want to add: ")
    water_to_add = int(input())
    print("\nWrite how many ml of milk do you want to add: ")
    milk_to_add = int(input())
    print("\nWrite how many grams of coffee beans do you want to add:")
    coffee_to_add = int(input())
    print("\nWrite how many disposable cups of coffee do you want to add:")
    cups_to_add = int(input())
    print()
    water += water_to_add
    milk += milk_to_add
    coffee_beans += coffee_to_add
    cups += cups_to_add
    
if action == 'take':
    print("I gave you $ " + str(money))
    money = 0

print()
has()