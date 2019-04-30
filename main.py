import json
from utils.dictionary import createDictionary

#January workouts
with open('files/text/January.txt') as jan_workouts_file:
    
    d = createDictionary(jan_workouts_file)

    with open("files/json/january.json","w") as f:
        json.dump(d,f)

#February workouts
with open('files/text/February.txt') as feb_workouts_file:
    
    d = createDictionary(feb_workouts_file)

    with open("files/json/february.json","w") as f:
        json.dump(d,f)

#March workouts
with open('files/text/March.txt') as mar_workouts_file:
    
    d = createDictionary(mar_workouts_file)

    with open("files/json/march.json","w") as f:
        json.dump(d,f)