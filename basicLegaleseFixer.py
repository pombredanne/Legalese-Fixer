''' Basic Legalese Fixer
	Here, just input a text file with the legalese,
	and edits will be made 
	eventually, I'll need to add a GUI
	and a way to read word files '''

import sys

exampleList = []
fixList = []
dictList = []

''' Trie used for spellchecking 
	based off notes from CIS 121'''

class Node:    
    def __init__(self):
        self.word = None
        self.nodes = {} # dictionary of various nodes
        
    def __getAll__(self):
    	''' Recursively get all the words in the trie '''
        x = []
        for key, node in self.nodes.iteritems() : 
            if(node.word is not None):
                x.append(node.word)
            x += node.__getAll__()      
        return x
    
    def __str__(self):
        return self.word
    
    def __insert__(self, word, stringPos = 0):
        currentLetter = word[stringPos]
        
        # Create the Node if it does not already exist
        if current_letter not in self.nodes:
            self.nodes[currentLetter] = Node();
        if(string_pos + 1 == len(word)):
            self.nodes[currentLetter].word = word
        else:
        	self.nodes[currentLetter].__insert__(word, stringPos + 1)   
    	return True
    
    def __getAllPrefix__(self, prefix, stringPos):
        ''' Much like getAll, but with a prefix '''
        x = []
        for key, node in self.nodes.iteritems() : 
            # If the current character of the prefix is one of the nodes or we have
            # already satisfied the prefix match, then get the matches
            if(stringPos >= len(prefix) or key == prefix[stringPos]):
            	if(node.word is not None):
                	x.append(node.word)
                    
                if(node.nodes != {}):
                    if(string_pos + 1 <= len(prefix)):
                        x += node.__getAllPrefix__(prefix, stringPos + 1)
                    else:
            			x += node.__getAllPrefix__(prefix, stringPos)
    
        return x       


class Trie:
   def __init__(self):
        self.root = Node()
        
   def insert(self, word):
        self.root.__insert__(word)
        
   def getAll(self):
        return self.root.__getAll__()

   def getAllPrefix(self, prefix, stringPos = 0):
        return self.root.__getAllPrefix__(prefix, stringPos)



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
	global fileText

	''' Now close the files '''
	dictFile.close()
	legaleseFile.close()
	legaleseFixes.close()
	fileToExamine.close()

	''' Spellcheck '''

	''' Check For Legalese and Edit '''



if __name__ == "__main__":
    main(sys.argv)