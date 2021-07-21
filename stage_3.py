print("Write how many ml of water the coffee machine has:")
machine_water = int(input())
print("Write how many ml of milk the coffee machine has:")
machine_milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
machine_coffee = int(input())
print("Write how many cups of coffee you will need:")
cup = int(input())

has_water = int(machine_water / 200)
has_milk = int(machine_milk / 50)
has_coffee = int(machine_coffee / 15)

list1 = [has_water, has_milk, has_coffee]

cup_make = min(list1)

if cup_make == cup:
    print("Yes, I can make that amount of coffee")
    
if cup_make < cup:
    print("No, I can make only " + str(cup_make) + " cups of coffee")

if cup_make > cup:
    cup_can_make = cup_make - cup
    print("Yes, I can make that amount of coffee (and even " + str(cup_can_make) + " more than that)")