print("Would you like to test this basic chatbot?")
print("Use 1 for yes and 0 for no")
test1 = input("Enter yes or no: ")
if (test1 == 0):
	print("Do it anyway.")
else: (test1 == 1)

print("\nHave you ever read The Hitchhiker's Guide to the Galaxy?")
book = input("Enter 1 or 0: ")
if (book == 1):
	print("\nGood. You don't suck.\n\n")
else:
	print("Go read it and come back.")

print("\nIf you haven't read the book by now, leave and never return.")
print("If you have read the book, please continue.")
print("\nWhat is the name of the main character?")
print("Adam       Pierce       Arthur       Craig")
print("1, 2, 3, or 4: ")
name = input("Enter the number of his name: ")
if (name == 3):
	print("\nSo you do know the book. Or else you repeated this with the process of elimination.")
	print("Where were the mice from? ")
	print("Maragrathea       Pluto       the Moon       Demos")
	planet = input("1, 2, 3, or 4: ")
	if (planet == 1):
		print("Correct. Next question.\n\n")
		print("What did the mice pay the Maragratheans to create? ")
		print("Cars       PacMan       Earth       Chickens")
		earth = input("1, 2, 3, or 4: ")
		if (earth == 3):
			print("Correct. Next question.\n\n")
			print("What hit Arthur in the small of the back as he flew throught the sky?")
			print("A city       A party       A rock       A bullet")
			city = input("1, 2, 3, or 4.")
			if (city == 2):
				print("\nCorrect. You have completed this test. Thank you for your input.  This program is now terminated.")
			elif (city == 4):
				print("He would be dead. The book continues, therefore...  This program is now terminated.")
			else:
				print("Wrong. This program is now terminated.")
		else:
			print("Wrong. This program is now terminated.")
	else:
		print("Wrong. This program is now terminated.")


elif (name == 4):
	print("That's the teacher. Not the character. This program is now terminated.")
else:
	print("Wrong. This program is now terminated.")
		
	
