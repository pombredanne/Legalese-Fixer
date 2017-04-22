''' Basic Legalese Fixer
	Here, just input a text file with the legalese,
	and edits will be made 
	eventually, I'll need to add a GUI
	and a way to read word files '''

import sys

exampleList = []
fixList = []
dictList = []

def checkAndEditLegalese(fileString):
	fileStringList = fileString.split()
	for i in range (0, len(fileStringList)):
		stringCheckVal = fileStringList[i].lower()
		if stringCheckVal in exampleList:
			editString = fixList[exampleList.index(stringCheckVal)]
			potentialEditList = []
			if "," not in editString:
				potentialEditList = [editString]
			else:
				editListVal = ""
			for j in editString:
				if j == ",":
					potentialEditList.append(editListVal)
					editListVal = ""
				else:
					editListVal += "j"
					potentialEditList.append(editListVal)
			for solution in potentialEditList:
				if solution.isUpper():
					if solution == "OMIT" or solution == "REMOVE":
						fileString.replace(stringCheckVal, "", 1)
						break
					pass
				else:
					fileString.replace(stringCheckVal, solution, 1)
					break
	return fileString
			

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
	global exampleList
	for exampleLine in legaleseFile:
		exampleList.append(exampleLine)

	global fixList
	for fixLine in legaleseFixes:
		fixList.append(fixLine)

	finalList = zip(exampleList, fixList)

	global dictList
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