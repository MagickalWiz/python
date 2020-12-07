import random
for i in range(1,53):
	n = random.randint(0,51)
	print(n," ",end="")
	if(i % 10 == 0):
		print(" * ")
print("\n\t\t",i,"<- last i - - - \n\n")

#30 attempts until '0' is first
