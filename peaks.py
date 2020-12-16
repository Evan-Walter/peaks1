# peaks.py
# Evan Walter
# October 23, 2020
# This program finds the peaks in a given csv file.

import math
import numpy


# Set up a list of data points
f = open('PeakFindingData.csv', 'r')
dataPoints = f.readlines()
dataPoints = numpy.asarray(dataPoints, dtype=float)

# Set up an empty list to populate with peaks
# Specify the chunk size to step through the data
peaks = []
chunk = math.ceil((len(dataPoints)) / 10)

for i in range(len(dataPoints)):
    # Calculate the average for each chunk
    if i + 1 + chunk <= len(dataPoints):
        avg = math.fsum(dataPoints[i : i + chunk]) / (chunk)

    # Criteria for a peak:
    # 110% above the average of its containing chunk
    # Greater than each point on the left and right
    if (dataPoints[i] >= 1.1*avg and dataPoints[i] >= dataPoints[i - 1]
            and dataPoints[i] >= dataPoints[i + 1]):
        peaks.append(dataPoints[i])

# Display the peaks on the screen
print('Peaks:')
for i in peaks:
    print(i)
