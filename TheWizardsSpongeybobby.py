import turtle
import TNZlifeless
import Wizardsquigglesquare
import MagickalWiz_Spngbb
import Spongeboi

def main():
	done = 0
	while (done == 0):
		Wizardsquigglesquare.main()
		MagickalWiz_Spngbb.main()
		TNZlifeless.main()
		Spongeboi.main()
		q = input(" * ")
		if (q == "1"):
			done = 1

if __name__ == '__main__':
	main()
