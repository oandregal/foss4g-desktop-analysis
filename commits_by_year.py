#!/usr/bin/python

import sys
import os
from pygooglechart import GroupedVerticalBarChart, Axis

datafile = sys.argv[1]
commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = GroupedVerticalBarChart(500, 200,
                                y_range=(0, 5500))

#chart.set_bar_width(25)
#chart.set_bar_width(25)

for line in commitsfile:
    (legend, data) = line.split(' ')
    data_array.append(int(data.strip()))
    legend_array.append(legend)

print data_array
print legend_array

chart.add_data(data_array)
chart.set_axis_labels('x', legend_array)
chart.set_axis_labels('y', range(0,6000,500))

print chart.get_url()

name = os.path.basename(datafile)
chart.download('images/commits_by_year_'+str(name.split('.')[0])+'.png')

