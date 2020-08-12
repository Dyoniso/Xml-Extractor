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
 - Convert xml to string and string to xml

@DyonisoHacks
-> Select only options:
""" 

def extract():
	print("")
	print(tag2+"Geting data..")

	for filename in glob.glob('extract/*.txt'):
		data = open(filename, encoding="utf8").read()
		convert(data)

def restore():
	wr = codecs.open("result/xml.txt", "a", "utf-8");
	wr.truncate(0)

	print("")
	print(tag2+"Geting data..")

	dataVar = open("result/output-var.txt", encoding="utf8").read()
	data = open("result/output.txt", encoding="utf8").read()

	lineVar = dataVar.split("\n");
	line = data.split("\n")


	for x in range(0, len(line)):
		try:
			convert = "<string name=\"%s\">%s</string>" % (lineVar[x], line[x])
			wr = codecs.open("result/xml.txt", "a", "utf-8");
			print(tag+convert)

		except Exception as e:
			print(tag3+"Error to restore xml file")
			break

	print(tag2+"Finished salved in result/xml.txt")
			

def clear():
	try:		
		wr = codecs.open("result/output.txt", "a");
		wr.truncate(0)
		wr = codecs.open("result/output-var.txt", "a", "utf-8");
		wr.truncate(0)

		print(tag+"Reuslts has empty!")

	except Exception as e:
		print(tag3+"Error in clear resouces")
		

def convert(data):
	clear()

	print("")
	print(tag+" Writing and Converting data..")
	
	cht = False
	for x in data.rsplit("\""):
		cv = x.replace("<string name=", "").replace("</string", "").replace(">", "").replace("<", "").replace("resources", "")
		cv = cv.split("\n")[0]

		if not cht:
			if cv:
				wr = codecs.open("result/output.txt", "a", "utf-8");
				wr.write(cv + os.linesep)
				print(tag+cv)

		else:
			if cv:
				wr = codecs.open("result/output-var.txt", "a", "utf-8");
				wr.write(cv + os.linesep)

		cht = not cht;
			
	print(tag2+" Finished salved in result/output.txt and result/output-val.txt")

os.system("cls")
  
def banner():
	print(mBanner) 