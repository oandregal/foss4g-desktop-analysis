#!/usr/bin/python

import sys
import os
from pygooglechart import GroupedVerticalBarChart, Axis

datafile = sys.argv[1]
name = os.path.basename(datafile)

commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = GroupedVerticalBarChart(800, 350,
                                y_range=(0, 3000))

#chart.set_bar_width(25)
#chart.set_bar_width(25)

for line in commitsfile:
    (legend, data) = line.split(' ')
    data_array.append(int(data.strip()))
    legend_array.append(legend)

print data_array
print legend_array

chart.add_data(data_array)
chart.set_axis_labels('x', range(1,25))
chart.set_axis_labels('y', range(0, 3250, 250))

chart.set_title(name.split('.')[0].upper() + " - # of commits grouped by hour of day")
print chart.get_url()

chart.download('images/commits_by_hour_'+str(name.split('.')[0])+'.png')
