def average(averages):
    averagesarray = averages.split(';')
    averages = 0
    mark = 0
    ret = dict()
    count = 0
    if averages == "":
        ret = {}
    for student in averagesarray:
        average = student.split(',')
        for j in average:
            for i in average:
                if len(j) > 2:
                    ret[i] = 0
                if len(i) < 2:
                    averages += int(i)
                    count += 1
                    ret[j] = averages / count
    return ret
