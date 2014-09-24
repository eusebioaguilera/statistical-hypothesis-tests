# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:10:56 2013

@author: eusebio
"""

"""
	This code calculates the wilcoxon test from a csv text file
"""

import sys
from numpy import genfromtxt
import numpy
from scipy import stats
import prettytable


# Help func
def show_help( ):
	
	print "Wilcoxon test"
	print ""
	print "Usage:"
	print "\tpython wilcoxon.py csv-file"

if len( sys.argv ) != 2:
	show_help()
	sys.exit( -1 )

# Read the csv file
try:
	my_data = genfromtxt( sys.argv[ 1 ] , delimiter=',')
except Exception, ex:
	print "Some error happens: ", ex.message
	sys.exit( -1 )

first, second = numpy.hsplit( my_data, 2 )

first = first.flatten()
second = second.flatten()


t, p = stats.wilcoxon( first, second )

table = prettytable.PrettyTable([ "Data1", "Data2", "D1-D2", "Sign" ])
table2 = prettytable.PrettyTable([ "Possitive Rank sum", "Negative Rank Sum", "Total" ])

positives = 0
negatives = 0

for i in range( len( first ) ):
    f1 = float( first[i] )
    f2 = float( second[i] )
    
    ret = f1 - f2
    
    s = 0
    
    if ret >= 0:
        positives += 1
        s = 1
    else:
        negatives += 1
        s = -1
    
    table.add_row( [ f1, f2, ret, s  ] )

table2.add_row( [positives, negatives, positives + negatives] )

print table
print table2

if positives > negatives:
    print "The sum of the negatives ranks of the differences", t
else:
    print "The sum of the positives ranks of the differences", t
print "p-value", p

if p < 0.05:
	print "Null hypothesis could be rejected!"
else:
	print "Null hypothesis could not be rejected!"
