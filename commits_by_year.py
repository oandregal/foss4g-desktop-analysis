#!/usr/bin/python

import sys
from pygooglechart import GroupedVerticalBarChart, Axis

datafile = sys.argv[1]

commitsfile = open(datafile, 'r')
data_array = []
legend_array = []

chart = GroupedVerticalBarChart(500, 200,
                                y_range=(0, 7000))

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
chart.set_axis_labels('y', ['0', '1000','2000','3000','4000','5000', '6000', '7000'])

print chart.get_url()

chart.download('images/commits_by_year_'+str(datafile.split('.')[0])+'.png')

