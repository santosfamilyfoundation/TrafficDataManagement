#import pandas
import numpy
import sqlite3
import storage
from matplotlib.pyplot import *


# objects = storage.loadTrajectoriesFromSqlite('stmarc.sqlite', 'object')
# speed = objects[5].getVelocityAtInstant(10).norm2()
# timeInterval = objects[3].getTimeInterval()
# speeds = [objects[3].getVelocityAtInstant(t).norm2() for t in range(timeInterval.first, timeInterval.last)]
# speeds = [v.norm2() for v in objects[3].getVelocities()]

if storage.tableExists('stmarc.sqlite','indicators'):
	interactions = storage.loadInteractions('stmarc.sqlite')
	print len(interactions)
	for i in interactions:
		TTC = i.getIndicator("Time to Collision")
		if (TTC != None):
			plot(range(TTC.getTimeInterval().first,TTC.getTimeInterval().last+1), TTC.getValues(), linewidth=2.0)
			TTC.getValues()
	xlabel('Frame of Calculation')
	ylabel('Time to Collision (in frames)')
	axis([180, 2000, 0, 2500])
	show()
	
	# show()

# print speeds
# figure()
# plot(range(timeInterval.first, timeInterval.last+1), speeds)
# show()
print "done"