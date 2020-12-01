select = input("Enter 'while' or 'for': ")
count = 0
if(select == "while"):
	while(count < 256):
		print(str(count)+" ",end="")
		count = count + 1
		if(count % 20 == 0):
			print(" * ")

elif(select == "for"):
	for i in range(0,256):
		#print(i)
		print(i," ",end="")
		if(i % 10 == 0 and i > 0):
			print()

else:
	print("Failure")
