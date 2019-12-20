import random
pscore = 0
cscore = 0
roll = 0
done = 0
keepscore = input("Keep ?")
while ((pscore <= 100) and (cscore <= 100)):
	scoreTemp = 0
	while (done == 0):
		#roll = 0
		roll = random.randint(1,6)
		print("It is your turn")
		print("The roll is: " + str(roll))
		#keepscore = input("Keep total score? type k to keep: ")
		keepscore = input("Keep ?")
		print ("keepscore",keepscore)
		keep =  keepscore[0].lower()
		print(keep)
		if (keep == 'k'):
			done = 1
		if (roll != 1):
			scoreTemp = scoreTemp + roll
			print(("Your total score is: ") + str(scoreTemp) + "\n\n")
		else:
			scoreTemp = 0
			done = 1
	#pscore = pscore + scoreTemp
	#done = 0
	'''
	while (done == 0):
		roll = 0
		keep = 1
		if (keep == 1):
			done = 1
		roll = random.randint(1,6)
		print("The computer's roll is: " + str(roll))
		if (roll != 1):
			cscore = cscore + roll
			roll = 0
			print(("The computer's score is: ") + str(cscore))
		else:
			scoreTemp = 0
			done = 1
'''
