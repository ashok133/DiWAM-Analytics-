import geocoder,math,csv
from pandas import DataFrame
#from itertools import zip_longest

#&markers=color:blue%7Clabel:S%7C40.702147,-74.015794

ph_states = []
EC_states = []
BOD_states = []
DO_states = []

df = DataFrame.from_csv('analysed.csv',sep=',',parse_dates=False)
df2 = DataFrame.from_csv('analysed_with_zips.csv',sep=',',parse_dates=False)
df2.insert(12,'DO?','NA')
df2.insert(13,'pH?','NA')
df2.insert(14,'EC?','NA')
df2.insert(15,'BOD?','NA')


for index,row in df.iterrows():
	unsafe_params = row[10]

	if 'pH' in unsafe_params:
		ph_states.append(row[1])

	if 'BOD' in unsafe_params:
		BOD_states.append(row[1])

	if 'DO' in unsafe_params:
		DO_states.append(row[1])

	if 'EC' in unsafe_params:
		EC_states.append(row[1])

for index,row in df2.iterrows():
	unsafe_params = row[10]

	if 'pH' in unsafe_params:
		df2.set_value(index,'ph?','True')

	if 'BOD' in unsafe_params:
		df2.set_value(index,'BOD?','True')

	if 'DO' in unsafe_params:
		df2.set_value(index,'DO?','True')

	if 'EC' in unsafe_params:
		df2.set_value(index,'EC?','True')

df2.to_csv('analysed_with_individual_params.csv')

ph_set = set(ph_states)
ec_set = set(EC_states)
do_set = set(DO_states)
bod_set = set(BOD_states)

print "pH Unsafe states: {} {}".format(len(ph_set),ph_set)
print "EC Unsafe states: {} {}".format(len(ec_set),ec_set)
print "BOD Unsafe states: {} {}".format(len(bod_set),bod_set)
print "DO Unsafe states: {} {}".format(len(do_set),do_set)

#rows = zip(list(ph_set),list(ec_set),list(do_set),list(bod_set))
