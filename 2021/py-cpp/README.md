This is a project I was given, to use the Python module os to run a C++ program. The C++ program takes a wordlist of 10,000, 20,000, or 30,000 words and sorts it, printing the sorted list.

The Python section allowed me to give the user a selection of which size wordlist to sort. I originally did this by triping the C++ program, each one hard-coded to sort one of the lists. Depending on the input, one of the programs would compile, and run. It was suggested by CWC, a.k.a. Icebowl, that I add a command line input. After attempting to understand the C++ code, I got it to work. It works similarly to the original three C++ codes. The same variable I used to select the correct program is used as a cli (command line input). The C++ program reads the variable as the file csort.o runs.

>magickalwiz@magickalwiz:~/py-cpp$ ./csort.o 10000

Python has another handy module, called datetime. Kinda self-explanatory. I took the time at the beginning of the sort, and compared it to the time at the end of the sort. This gave me the duration of the program, and is printed for reference.
