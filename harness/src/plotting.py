import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def quick_plot():
    name = []
    time = []
    sub = {}

    # Read the statistics
    sat_file = open(os.getcwd() + "/../../output/FatherNode-output.txt", 'r')

    # grep the big title
    headline = sat_file.readline().strip()
    while (True):
        # Read from file
        title = sat_file.readline().strip()
        if (len(title) == 0):
            break
        name.append(title)
        sub[title]=list()
        start_time = sat_file.readline().strip()

        subtitle = sat_file.readline().strip()

        while not (ord(subtitle[0]) >= 48 and ord(subtitle[0]) <= 57):
            substart = sat_file.readline().strip()
            subend = sat_file.readline().strip()

            sub[title].append(time_different(substart, subend))
            subtitle = sat_file.readline().strip()

        time.append(time_different(start_time, subtitle))

    plt.figure("TAbench Total Execution Time")

    index = np.arange(len(time))
    bar_width = 0.35
    opacity = 0.4

    plt.bar(index, time, bar_width, alpha=opacity, color='b', label="es10fst")

    plt.xlabel("Solver")
    plt.ylabel("Time (millisecond)")
    plt.title(title)
    plt.xticks(index, name)
    plt.ylim(0, max(time) + 100)
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.getcwd() + "/../../output/" + headline +"_total.png")

    plt.figure("TAbench Single Execution Time")

    for i in sub.keys():
        plt.plot(range(0, len(sub[i])), sub[i], label=i)
    plt.title("Single Execution Time")
    plt.ylabel("millisecond")
    plt.legend()
    plt.savefig(os.getcwd() + "/../../output/" + headline + "_single.png")

    maximum = []
    plt.figure("TAbench Maximum Execution Time")
    for i in sub.keys():
        maximum.append(max(sub[i]))
    plt.bar(index, maximum, bar_width, alpha=opacity, color='b', label="es10fst")

    plt.xlabel("Solver")
    plt.ylabel("Time (millisecond)")
    plt.title(title)
    plt.xticks(index, name)
    plt.ylim(0, max(maximum) + 100)
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.getcwd() + "/../../output/" + headline +"_maximum.png")

    minimum = []
    plt.figure("TAbench Minimum Execution Time")
    for i in sub.keys():
        minimum.append(min(sub[i]))
    plt.bar(index, minimum, bar_width, alpha=opacity, color='b', label="es10fst")

    plt.xlabel("Solver")
    plt.ylabel("Time (millisecond)")
    plt.title(title)
    plt.xticks(index, name)
    plt.ylim(0, max(minimum) + 100)
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.getcwd() + "/../../output/" + headline +"_minimum.png")


def time_different(start, end):
    startE = start.split('-')
    endE = end.split('-')

    hourd = int(endE[0]) - int(startE[0])
    mind = int(endE[1]) - int(startE[1])
    secd = int(endE[2]) - int(startE[2])
    minisecd = int(endE[3]) - int(startE[3])

    return (hourd * 60 * 60 * 1000) + (mind * 60 * 1000) + (secd * 1000) + (minisecd)

if __name__=="__main__":
    quick_plot()
