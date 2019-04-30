from convert import txtToJson

#start with March workouts
with open('files/March.txt') as march_workouts_file:
    
    lines = march_workouts_file.readlines()
    newLines = txtToJson(lines)
    print(newLines)


        