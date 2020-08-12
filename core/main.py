import os
import sys
import glob
import codecs

red = "\033[0;31m"
white = "\033[0m"
blue = "\033[94m"
green = "\033[92m"
magenta = "\033[1;35;40m"

tag3 = red+"[X] "+white
tag2 = green+"[+] "+white
tag1 = red+"[+] "+white
tag = blue+"[*] "+white

mBanner = """  
*The xml Extractor*  

@DyonisoHacks
-> Select only options:
""" 

def extract():
	print("")
	print(tag2+"Geting data..")

	for filename in glob.glob('extract/*.txt'):
		data = open(filename, encoding="utf8").read()
		convert(data)
			

def convert(data):
	print("")
	print(tag+" Writing and Converting data..")
	
	cht = False
	for x in data.rsplit("\""):
		cv = x.replace("<string name=", "").replace("</string", "").replace(">", "").replace("<", "")
		cv = cv.split("\n")[0]

		if not cht:
			wr = codecs.open("result/output.txt", "a", "utf-8");
			wr.write(cv + os.linesep)
			print(tag2+cv)

		cht = not cht;
			
	print(tag2+" Finished!")

os.system("cls")
  
def banner():
	print(mBanner) 