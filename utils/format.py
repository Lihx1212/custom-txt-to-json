#return new formatted lines
def formatTxtToList(lines):
    month = lines.pop(0).rstrip()
    newLines = ''
    for index, line in enumerate(lines):
        if ":" in line:
            day =  lines[index - 1].rstrip()
            time_of_day = line.rstrip()
            miles_unformat =  lines[index + 1].rstrip()
            miles_ran = miles_unformat[0] + '.' + miles_unformat[1:]
            calories_burned =  lines[index + 2].rstrip().replace("c","")
            total_strides =  lines[index + 3].rstrip().replace("s","")
            strides_per_min = str(round(int(total_strides)/30))
            newLines+=f'2019 {month} {day} {time_of_day} {miles_ran} {calories_burned} {total_strides} {strides_per_min} 30 \n'
    return newLines