print("Write how many cups of coffee you will need:")
n = input()
water = int(n) * 200
milk = int(n)  * 50
beans = int(n)  * 15
print("For " + n + " cups of coffee you will need:")
print(str(water) + " ml of water")
print(str(milk) + " ml of milk")
print(str(beans) + " g of coffee beans")