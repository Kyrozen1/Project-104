import csv
import time
from collections import Counter

with open("SOCR-HeightWeight.csv", newline="") as file:
    reader = csv.reader(file)
    fileData = list(reader)
    fileData.pop(0)
    newData = []
    for i in range(len(fileData)):
        n_number = fileData[i][2]
        newData.append(float(n_number))

    #mean
    n = len(newData)
    total = 0
    for x in newData:
        total += x
    mean = total/n
    print("mean (Average) ->"+str(mean))

    #median
    if n%2 == 0:
        median1 = float(newData[n//2])
        median2 = float(newData[n//2-1])
        median = (median1+median2)/2
    else:
        median = newData[n//2]
    print("median ->"+str(median))

    #mode
    data = Counter(newData)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is: " + ', '.join(map(str, mode))
    print(get_mode)

    time.sleep(1000)
