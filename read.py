import json
from dictionary import createDictionary

#start with March workouts
with open('files/March.txt') as workouts_file:

    
    d = createDictionary(workouts_file)

    print('--------------new nested dictionary-------------------')
    print(d)

    with open("files/march.json","w") as f:
        json.dump(d,f)