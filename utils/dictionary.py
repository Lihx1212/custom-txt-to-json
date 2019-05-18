from utils.format import formatTxtToList

def createDictionary(workouts_file):

	lines = workouts_file.readlines()
	newLines = formatTxtToList(lines)
	nested_dictionary = {}
	key = "workouts"
	for line in newLines.splitlines():
		newLine = line.rstrip().split(' ')
		listOfKeys = ['year', 'month', 'day', 'timeOfDay' , 'distance' , 'calories' , 'strides']
		zipbObj = zip(listOfKeys, newLine)
		nested_dictionary.setdefault(key, []).append(dict(zipbObj))
	return nested_dictionary