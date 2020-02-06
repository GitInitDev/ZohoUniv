def calcPower(base, power):
    base = float(input("Enter The Base : "))
    power = float(input("Enter The Power : "))
    ans = print("The power of", base, "to the power", power, "is: ", pow(base, power))
    return ans
calcPower(2, 5)