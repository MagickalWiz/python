import os
from os import path
from datetime import datetime


def main():
	print("This program compiles a C++ program, then times how long it takes to run.\nThe C++ program sorts a wordlist of 10,000, 20,000, or 30,000 randomly generated strings.")
	print("10,000     20,000     30,000")
	print("   1         2           3")
	wlSize = int(input("Enter 1, 2, or 3 for the size of wordlist to sort: "))
	
	if(wlSize == 1):
		x = '10000.txt'
		y = 10000
		#print(x)
	elif(wlSize == 2):
		x = '20000.txt'
		y = 20000
		#print(x)
	elif(wlSize == 3):
		x = '30000.txt'
		y = 30000
		#print(x)
	else:
		print("ERROR PLEASE REATTEMPT")
	
	
	oscpp(x,y)


def oscpp(x,y):
	start = datetime.now()
	startM = start.strftime("%M")
	startS = start.strftime("%S")
	startMS = start.strftime("%f")
	if(path.exists(x) == True):
		#print("File exists, continuing with program")
		if(path.exists("csort" + str(y) + ".cpp") == True):
			os.system("g++ csort" + str(y) + ".cpp -o csort.o")
			os.system("./csort.o")
			end = datetime.now()
			endM = end.strftime("%M")
			endS = end.strftime("%S")
			endMS = end.strftime("%f")
			
			durationM = int(endM) - int(startM)
			durationS = int(endS) - int(startS)
			durationMS = abs(int(endMS) - int(startMS))
			print("\nM:S:MS")
			print(str(durationM) + ":" + str(durationS) + ":" + str(durationMS))
			
		else:
			filename = "csort" + str(y) + ".cpp"
			errorFunction(filename)
		
	else:
		errorFunction(x)


def errorFunction(filename):
	print("ERROR FILE DOES NOT EXIST")
	print("\nPLEASE CONFIRM THAT " + filename + " EXISTS AND IF NOT REDOWNLOAD")
	print("\nhttps://github.com/MagickalWiz/python/tree/master/2021/py-cpp")


if __name__ == "__main__":
	main()
