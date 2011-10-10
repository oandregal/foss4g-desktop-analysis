#!/usr/bin/python

import sys
import os
from pygooglechart import GroupedVerticalBarChart, Axis

datafile = sys.argv[1]
name = os.path.basename(datafile)

commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = GroupedVerticalBarChart(250, 300,
                                y_range=(0, 6000))

#chart.set_bar_width(25)
#chart.set_bar_width(25)

for line in commitsfile:
    (legend, data) = line.split(' ')
    data_array.append(int(data.strip()))
    legend_array.append(legend)

print data_array
print legend_array

chart.add_data(data_array)
chart.set_axis_labels('x', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
chart.set_axis_labels('y', range(0, 6000, 500))

chart.set_title(name.split('.')[0].upper() + " - # commits grouped by day")
print chart.get_url()

chart.download('images/commits_by_day_'+str(name.split('.')[0])+'.png')

