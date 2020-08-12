import sys
import os
if sys.version_info.major < 3:
    print("Extractor supports only Python3. Run the application in Python3 environment.")
    exit(0)
from core.main import *

def main():
	try:
		banner()
		print("* Select [1] to extract. ")
		print("* Select [2] to exit.")
		print("")
		rInput = input(tag+"extractor > ")
		if rInput == "1" or rInput == "01":
			extract()

		if rInput == "2" or rInput == "02":
			exit(0)

	except(KeyboardInterrupt, SystemExit):
		print(tag3+"Tool Interrupted"+"\n")
		exit(0)
		
if __name__ == "__main__":
	main()
	

