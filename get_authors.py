#!/usr/bin/python

import sys

datafile = sys.argv[1]
authorsfile = open(datafile, 'r')
outputfile = open('/tmp/authors.2010', 'w')

selected_authors = []

for line in authorsfile:
    (author, date) = line.split(',')
    if author not in selected_authors:
        selected_authors.append(author)

for author in selected_authors:
    outputfile.write(author+'\n')

outputfile.close()
authorsfile.close()
authorsfile.close()
