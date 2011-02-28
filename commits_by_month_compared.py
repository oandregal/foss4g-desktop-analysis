#!/usr/bin/python

import sys
import os
from pygooglechart import SparkLineChart

datacompletefile = sys.argv[1]
commitsfile = open(datacompletefile, 'r')

datacomparefile = sys.argv[2]
comparefile = open(datacomparefile, 'r')

legend_array = []
data_array = []
data_compared_array = []

chart = SparkLineChart(500, 200, y_range=[0,750])

for line in commitsfile:
    (legend, data) = line.split(' ')
    legend_array.append(legend)
    data_array.append(int(data.strip()))

for line in comparefile:
    (legend, data) = line.split(' ')
    data_compared_array.append(int(data.strip()))

chart.add_data(data_array)
chart.add_data(data_compared_array)
chart.add_data([0]*2)

chart.set_colours(['000000'])

chart.add_fill_range('224499', 0, 1)
chart.add_fill_range('339966', 1, 2)

legend_array_stripped = [legend_array[0],
                         legend_array[len(legend_array)/2],
                         legend_array[-1]]

chart.set_axis_labels('x', legend_array_stripped)
chart.set_axis_labels('y', ['0', '150', '300', '450', '600', '750'])

print chart.get_url()

name = os.path.basename(datacompletefile)
chart.download('images/commits_by_month_compared_2010_'+str(name.split('.')[0])+'.png')
