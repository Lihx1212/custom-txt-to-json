import json
from dictionary import createDictionary

#February workouts
with open('files/February.txt') as feb_workouts_file:
    
    d = createDictionary(feb_workouts_file)

    with open("files/february.json","w") as f:
        json.dump(d,f)

#March workouts
with open('files/March.txt') as mar_workouts_file:
    
    d = createDictionary(mar_workouts_file)

    with open("files/march.json","w") as f:
        json.dump(d,f)