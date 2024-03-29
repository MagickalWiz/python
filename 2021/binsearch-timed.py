from datetime import datetime
import random

def main():
	file = open("wordlist.txt")
	array = file.read().split(',')
	#print(array) #debugs
	#print(len(array))
	
	success = False
	count = 1
	word = ''
	start = datetime.now()
	start_time = start.strftime("%D:%H:%M:%S:")
	print("This program searches a list of 1000 words to locate the input. The program will create a random string of letters, and continue to randomize until it locates a match.\nPress \'Enter\' to begin")
	inputword = str(input("Enter word: "))
	randomizeWord(array, success, start_time)


def binsearch(array, w, success):
	n = len(array)
	s = 0					#start		p
	e = n					#end		r
	m = int((e + s) / 2) 	#middle		q
	
	while(s <= e):
		#print(m) #debug
		if(array[m] == w):
			return m
		else:
			if(array[m] < w):
				s = m + 1
				m = int((e + s) / 2)
			else:
				e = m - 1
				m = int((e + s) / 2)
	return 'Word not found'


def binsearchrand(array, w, success):	#for randomizing, it loops and repeats randomizing until it locates a word
	n = len(array)
	s = 0					#start		p
	e = n					#end		r
	m = int((e + s) / 2) 	#middle		q
	
	while(s <= e):
		#print(m) #debug
		if(array[m] == w):
			return m
		else:
			if(array[m] < w):
				s = m + 1
				m = int((e + s) / 2)
				#print(str(m) + ' < ') #debug
			else:
				e = m - 1
				m = int((e + s) / 2)
				#print(str(m) + ' > ') #debug
	print("not found\n")
	return False


def randomizeWord(array, success,start_time):	#repeats the creation of randomized words and relaunches the search function
	count = 0
	while(success == False):
		word = ''
		for i in range(random.randint(5,8)):
			rn = random.randint(97,122)
			word = word + chr(rn)
			#print(rn) #debug
		print(word) #debug
		success = binsearchrand(array, word, success)
		count = count + 1
	#print(str(count) + " COUNT") #debug
	print("Place in array: " + str(success) + " after " + str(count) + " loops")
	end = datetime.now()
	end_time = end.strftime("%D:%H:%M:%S:")
	print("Start date/time: " + str(start_time))
	print("End date/time: " + str(end_time))
	
	



if __name__ == '__main__':
    main()