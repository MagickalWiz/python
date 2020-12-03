import os
print("This python code will ask for a name for an image")
print("then add a file name type of .png.")
print("the *.png will be saved in the directory where this")
print("file is executed.")
imagename = input("Imput a name for an image : ")
oscommand = "scrot "+imagename+".png"
print(oscommand)
os.system(oscommand)

'''
Now the challenge is to 
os.system(sleep 5)
'''
