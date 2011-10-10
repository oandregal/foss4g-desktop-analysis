#!/usr/bin/python

import sys
import os
from pygooglechart import GroupedVerticalBarChart, Axis

datafile = sys.argv[1]

commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = GroupedVerticalBarChart(500, 300,
                                y_range=(0, 4500))

#chart.set_bar_width(25)
#chart.set_bar_width(25)

for line in commitsfile:
    (legend, data) = line.split(' ')
    data_array.append(int(data.strip()))
    legend_array.append(legend)

print data_array
print legend_array

chart.add_data(data_array)
chart.set_axis_labels('x', range(1,13))
chart.set_axis_labels('y', range(0, 5000, 500))

print chart.get_url()

name = os.path.basename(datafile)
chart.download('images/commits_by_month_'+str(name.split('.')[0])+'.png')

