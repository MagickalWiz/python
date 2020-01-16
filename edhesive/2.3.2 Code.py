feet1 = str(input("Enter the first number of feet: "))
feet2 = str(input("Enter the second number of feet: "))
in1 = str(input("Enter the first number of inches: "))
in2 = str(input("Enter the second number of inches: "))

totalinches = in1 + in2 + feet1 *12 + feet2 *12
ffeet = int(totalinches / 12)
fin = int(totalinches % 12)
print("Feet: "+str(ffeet)+" Inches: "+str(fin))

#Thanks to Craig Coleman for part of this code.
