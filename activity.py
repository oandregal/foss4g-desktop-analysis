#!/usr/bin/python

import sys
import os

datafile = sys.argv[1]
gitlogfile = open(datafile, 'r')

datafile_selected_authors = sys.argv[2]
selectedauthorsfile = open(datafile_selected_authors, 'r')

#ex: data/qgis_top3.commitsbymonth
name = os.path.basename(datafile)
selected_defined = os.path.basename(datafile_selected_authors)
commits_selected_authors_file = open(
    'data/'+str(name.split('.')[0])+'_'+selected_defined.split('.')[1]+'.commitsbymonth', 'w')

selected_authors = []
for author in selectedauthorsfile:
    selected_authors.append(author.strip())

months = ("Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec")

years = ("1999", "2000", "2001", "2002", "2003", "2004", "2005",
         "2006", "2007", "2008", "2009", "2010", "2011")

months_dict = {"Jan":0,
               "Feb":0,
               "Mar":0,
               "Apr":0,
               "May":0,
               "Jun":0,
               "Jul":0,
               "Aug":0,
               "Sep":0,
               "Oct":0,
               "Nov":0,
               "Dec":0
               }

commits = {"2011": months_dict.copy(),
           "2010": months_dict.copy(),
           "2009": months_dict.copy(),
           "2008": months_dict.copy(),
           "2007": months_dict.copy(),
           "2006": months_dict.copy(),
           "2005": months_dict.copy(),
           "2004": months_dict.copy(),
           "2003": months_dict.copy(),
           "2002": months_dict.copy(),
           "2001": months_dict.copy(),
           "2000": months_dict.copy(),
           "1999": months_dict.copy(),
           }


for line in gitlogfile:
    (author, date) = line.split(',')
    (day, month, daynumber, hour, year, timezone) = date.strip().split(' ')

    if author in selected_authors:
        commits[year][month] = commits[year][month]+1

for y in years:
    for m in months:
        commits_selected_authors_file.write(y+"-"+m+" "+str(commits[y][m])+"\n")

commits_selected_authors_file.close()
