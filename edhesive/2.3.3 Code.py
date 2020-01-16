hr = int(input("Enter the hours: "))
min = int(input("Enter the minutes: "))

min = min + 15

if (min >= 60):
	hr = hr + 1
	min = min - 60
	if (hr > 12):
		hr = hr - 12

print ("Hours: " + str(hr))
print ("Minutes: " + str(min))
