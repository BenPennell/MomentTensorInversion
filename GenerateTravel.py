import numpy as np
import time
import datetime

VELOCITY = 2.800 # km/s
PATH = "./2023-02-06T011734_TURKEY/weights.dat"

infile = np.genfromtxt(PATH, dtype=None)

output = ""

for line in infile:
    distance = float(line[1]) # km
    travel_time = float(distance) / VELOCITY # seconds
    print_time = str(travel_time)
    
    print(print_time)
    output = output + ' '.join(str(x) for x in line)[:-8] + " " + print_time + " 0 0\n"
    
outfile = open("newweights.dat", "w")
outfile.write(output[:-1])
