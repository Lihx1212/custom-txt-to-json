from format import formatTxtToList

def createDictionary(workouts_file):

	lines = workouts_file.readlines()
	newLines = formatTxtToList(lines)
	#print(newLines)
	nested_dictionary = {}
	for line in newLines.splitlines():
		newLine = line.rstrip().split(' ')
		day = newLine.pop(0)
		listOfKeys = ['timeOfDay' , 'distance' , 'calories' , 'strides']
		zipbObj = zip(listOfKeys, newLine)
		nested_dictionary[day] =  dict(zipbObj)
		# print(d[day])
	return nested_dictionary