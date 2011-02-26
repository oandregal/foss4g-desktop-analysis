#!/usr/bin/python

import sys
from pygooglechart import PieChart2D

chart = PieChart2D(500, 200)

datafile = sys.argv[1]

linesofcodefile = open(datafile, 'r')
data_array = []
legend_array = []

for line in linesofcodefile:

    (legend, data) = line.split(',')

    legend_array.append(legend)
    data_array.append(int(data.strip()))

print legend_array
print data_array

# Add some data
chart.add_data(data_array)

# Assign the labels to the pie data
chart.set_pie_labels(legend_array)

# Print the chart URL
print chart.get_url()

# Download the chart
chart.download('./images/lines_of_code_'+str(datafile.split('.')[0]) + '.png')
