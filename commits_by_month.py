#!/usr/bin/python

import sys
import os
from pygooglechart import SparkLineChart

datafile = sys.argv[1]
commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = SparkLineChart(500, 200,
                       y_range=(0,750))

for line in commitsfile:
    (legend, data) = line.split(' ')
    legend_array.append(legend)
    data_array.append(int(data.strip()))

chart.add_data(data_array)

legend_array_stripped = [legend_array[0],
                         legend_array[len(legend_array)/2],
                         legend_array[-1]]

chart.set_axis_labels('x', legend_array_stripped)
chart.set_axis_labels('y', range(0,800, 100))

print chart.get_url()

name = os.path.basename(datafile)
chart.download('images/commits_by_month_'+str(name.split('.')[0])+'.png')
