with open('files/March.txt') as march_workouts_file:
    
    lines = march_workouts_file.readlines()

    for index, line in enumerate(lines):
        if ":" in line:
            day =  lines[index - 1].rstrip()
            time_of_day = line.rstrip()
            miles_ran =  lines[index + 1].rstrip()
            calories_burned =  lines[index + 2].rstrip()
            total_strides =  lines[index + 3].rstrip()
            print(day,time_of_day, miles_ran,calories_burned,total_strides)


        