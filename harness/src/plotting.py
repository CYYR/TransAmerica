import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def to_length_nine(aString):
    while len(aString) < 9:
        aString += "0"
    return aString

def quick_plot(path, str_path):
    sat_file = open(path, 'r')
    title = sat_file.readline().strip()
    name=[]
    time=[]
    while (True):
        subtitle = sat_file.readline().strip()
        if len(subtitle) == 0:
            break
        name.append(subtitle)
        start_time = to_length_nine(sat_file.readline().strip())
        end_time = to_length_nine(sat_file.readline().strip())
        time.append(time_different(start_time, end_time))

    n_groups = len(time)

    fig, ax = plt.subplots()
    index = np.arange(len(time))
    bar_width = 0.35

    opacity = 0.4
    rects1 = plt.bar(index, time, bar_width, alpha=opacity, color='r', label="es10fst")

    plt.xlabel('Solver')
    plt.ylabel('Time')
    plt.title(title)
    plt.xticks(index, name)
    plt.ylim(0, max(time) + 100)
    plt.legend()

    plt.tight_layout()
    plt.savefig(str_path + str(title) + "jpg")

def time_different(start, end):
    hou1 = int(start[0:2])
    min1 = int(start[2:4])
    sec1 = int(start[4:6])
    minisec1 = int(start[6:9])
    hou2 = int(end[0:2])
    min2 = int(end[2:4])
    sec2 = int(end[4:6])
    minisec2 = int(end[6:9])
    hourd = hou2 - hou1
    mind = min2 - min1
    secd = sec2 - sec1
    minisecd = minisec2 - minisec1
    return (hourd * 60 * 60 * 1000) + (mind * 60 * 1000) + (secd * 1000) + (minisecd)

if __name__=="__main__":
    if (len(sys.argx) != 3):
        print("plotting.py <Path_to_Statistics> <Path_for_store_the_tables>")
    else:
        quick_plot(sys.argv[1], sys.argv[2])
