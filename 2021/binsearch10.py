import random

def main():
	file = open("wordlist10.txt")
	array = file.read().split(',')
	
	success = False
	count = 1
	word = ''
	begin = input("This program searches a list of 10-letter words to locate a randomized selection of letters. Press \'Enter\' to begin:")
	randomizeWord(array, success)
	print("Place in array: " + str(success))



def binsearchrand(array, w, success, count):
	n = len(array)
	s = 0
	e = n
	m = int((e + s) / 2)
	
	while(s <= e):
		if(array[m] == w):
			return m
		else:
			if(array[m] < w):
				s = m + 1
				m = int((e + s) / 2)
			else:
				e = m - 1
				m = int((e + s) / 2)
	print("not found - count: " + str(count) + "\n")
	return False


def randomizeWord(array, success):
	count = 0
	while(success == False):
		word = ''
		for i in range(10):
			rn = random.randint(97,122)
			word = word + chr(rn)
		print(word)
		success = binsearchrand(array, word, success, count)
		count = count + 1
	print("Place in array: " + str(success) + " after " + str(count) + " loops")
	

if __name__ == '__main__':
    main()