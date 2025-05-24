print("Feet to Inches")
print("")
def feet_to_inches(feet):
    return feet * 12

def inches():
    feet = float(input("Enter amount of feet to convert to inches: "))
    inches=feet_to_inches(feet)
    print(f"There are {inches:.2f} inches in {feet}ft")
inches()