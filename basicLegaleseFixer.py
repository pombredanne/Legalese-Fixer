''' Basic Legalese Fixer
	Here, just input a text file with the legalese,
	and edits will be made 
	eventually, I'll need to add a GUI
	and a way to read word files '''

import sys

def checkAndEditLegalese():
	

def spellCheck():


def main(argv):
	''' Check to make sure there are at least 2 args '''
	if len(argv) < 1:
		raise ValueError("Not enough arguments (1 arg instead of 2)")
	''' Open the files '''
	fileName = argv[1]
	dictFile = fopen("en-US.dic", "r")
	legaleseFile = fopen("legaleseExamples.txt", "r")
	legaleseFixes = fopen("legaleseFixes.txt", "r")
	fileToExamine = fopen(fileName, "r")
	editedOutputFile = fopen("editedFile.txt", "w")

	''' Develop the lists for the dictionary,
		the fixes, the legalese examples '''
	exampleList = []
	for exampleLine in legaleseFile:
		exampleList.append(exampleLine)

	fixList = []
	for fixLine in legaleseFixes:
		fixList.append(fixLine)

	finalList = zip(exampleList, fixList)

	dictList = []
	for dictLine in dictFile:
		dictList.append(dictFile)
	return 0

	fileText = fileToExamine.read()

	''' Now close the files '''
	dictFile.close()
	legaleseFile.close()
	legaleseFixes.close()
	fileToExamine.close()

	''' Spellcheck '''

	''' Check For Legalese and Edit '''



if __name__ == "__main__":
    main(sys.argv)