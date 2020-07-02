import csv
import datetime


print('Hello World')
csvData =[]
				# old c-style way to open a file:
				# f = open('myfile','read')
				# do stuff
				# f.read()
				# f.close()
with open('Downloads/Quicken Transaction Data .txt', newline='') as csvFile:
	Transaction = csv.reader(csvFile)
	for row in Transaction: 
		#print(repr(row))
		csvData.append(row)

for i in reversed(range(len(csvData))) :
	row = csvData[i]   # row is now a list : [ '', 'blah blah', 'DEPOSIT', 'FIDELITY', 'YADDA YADDA', '-5334.0' ]
	emptyElements = [ len(column)== 0 for column in row ]
    # emptyElements = []
    # for column in row :
    #    emptyElements += [ len(column) == 0 ]
				# all( [ True, False, True          ] ) : returns False
				# all( [ True, True, True, True     ] ) : returns True
				# any( [ False, False, False, False ] ) : returns False
				# any( [ False, True, False         ] ) : returns True
	if all( emptyElements ) :
		del csvData[i]
		continue
				#	else :
				#		print('the world is round', repr(csvData[i]))
				#		continue
				# 
				# 
	if '-' in csvData[i][1] or 'BALANCE' in csvData[i][1] or 'TOTAL' in csvData[i][1]  :
				#		print(' Hello David   ',csvData)
		del csvData[i]
		continue

				# Moving 3 If statements to a single If with or 

				#	if '-'  in csvData[i][1] : 
				#		del csvData[i]
				#		continue 
				#	if 'BALANCE'  in csvData[i][1] : 
				#		del csvData[i] 
				#		continue
				#	if 'TOTAL'  in csvData[i][1] : 
				#		del csvData[i] 
				#		continue
				#	print(' Where is this printed?   ', csvData[i])

for i,r in enumerate(csvData) :
    # i will equal a number, the index of the current-loop's row
	# r will equal a list  , the row the loop is currently on
	print()
#	print(repr(r))
	# 	converts amount to a number
	csvData[i][9] = float( r[9].replace(',','') )
#	print(csvData[i][9])
#	print(repr(csvData[i]))
	
	# converts date string to date object
	# dt = datetime.strptime('21/11/2006 16:30', '%m/%d/%Y %H:%M' )
    	# dt = datetime.strptime('21/11/2006'      , '%m/%d/%Y %H:%M' )
#	print(csvData[i][1])
	dt = datetime.datetime.strptime(	csvData[i][1],'%m/%d/%Y' )
	csvData[i][1] = dt	
#	print(dt)
#	print(repr(csvData[i]))
#	print(repr(csvData[i][1]),'  ',repr(csvData[i][2]),'  ',repr(csvData[i][6]),'  ',repr(csvData[i][9])	)
				#	Exammple of strftime conversion 
				#   blah.strftime('my codes %m %d')
				#   blah.strftime
				#   a = csvData[i][1]
				#   b = a.strftime('%m %d %Y')
				#   s += repr(b) + '   '
	s = '  '
	s += repr(csvData[i][1].strftime("%m %d %Y")) + '  '
	s += repr(csvData[i][2]) + '  '
	s += repr(csvData[i][6]) + '  '
	s += repr(csvData[i][9]) + '  ' 
#			Prints the needed values of date, account, category, and transaction amount
#	print(s)
sumTotal = 0.0
for row in csvData :
	sumTotal += row[9]
# print( 'mystring with format code %b' % myinputvariable )
print(' This is a Total %.2f' % sumTotal )

ListSorted = sorted(csvData, key=lambda x: (x[2], x[1]) )
for row in ListSorted :
	s = '  '
	s += repr(row[1].strftime("%m %d %Y")) + '  '
	s += '%-45s' %repr(row[2]) + '  '   # negative is left justified
	s += '%-42s' %repr(row[6]) + '  '
	s += '%-20s' %repr(row[9]) + '  ' 
	print('Sorted $ value ' , s )
print()
print('This is the dir function for a datetime object', dir( row[1] ))
print()
print('This is the dir for the datetime module ', dir(datetime))
print()
a = datetime.datetime.strptime('05/12/1986', '%m/%d/%Y')
#from datetime.datetime import strftime
#b = strftime('12/15/1949', '%m/%d/%Y')
print('My BirthDay  ', a.weekday() )
print('End of Dir example')
print()
				#     lambda examples
				#	mylamb = lambda x :     4*x + 3
				#	def mylamb2(x) : return 4*x + 3
				#	mylamb( 7) # 31
				#	mylamb2(7) # 31

				# 1. get list of 2nd position in all rows
				# 2. remove duplicate elements from 1. with # a = set()
				# 3. use set items to create dictonary for storing sums
				# 4. loop over rows, 
				#    4a. determine the row's category, 
				#    4b. add number to dictionary using category as a key

categoryList = []  
for row in ListSorted  :
	categoryList.append(row[2])
	# categoryList += [ row[2] ]
				# a = [blah, blah]
				# b = set(a)
				# c = list(b)
uniqueCategory = set(categoryList)
uniqueCategoryList = list(uniqueCategory)  

				# list1 = [4,2,'blah','ex']
				# dict1 = {'gamma':4, 'beta':12, '7':'organic'}
				# list1[2]       # returns 'blah'
				# dict1['gamma'] # returns 4
				# dict1['7']     # returns 'organic'
				# dict1['mambo'] = 14
				# dict1['mambo'] += 3.7
				# dict1[18] = 124124
				# actually works like: dict1['18'] = 124124
				# mykey = 'mambo'
				# dict1[mykey] += 4.2
				# for k,v in dict1.items() :
				#   print( 'key:',k,'   value:',v)
				# for k in sorted(dict1.keys()) :
				#   print('dict1[%25s] = %s' %      ( k, dict1[k] ) ) # inspired by C  
				#   print('dict1[{1}]  = {0}'.format( dict1[k], k ) ) # alternate way
				# dict1.keys()
				# dict1.values()

sumDictionary = {}

for category in uniqueCategoryList :
	sumDictionary[category] = 0
#	print(' this is a sumDictionary value  ',sumDictionary)
for sumDictionaryKey, sumDictionaryValue in sumDictionary.items() :
	print('sumDictionaryKey  is  ', sumDictionaryKey, ' sumDictionaryValue  is  ', sumDictionaryValue)

for k in sorted(sumDictionary.keys())   :
	print('This is sumDictionary[%75s] is %s' % ( k, sumDictionary[k] ) )

				#a = [2,4,6,3,5,9,11]
				#for b in a :
				#	print('a: %d' % a )
				#	if a == 9 :
				#		break
				#	if a > 5 :
				#		continue
				#	print('a is small!')


for row in ListSorted  :
	keyName = row[2]
	sumDictionary[keyName] += row[9]
print()
for k in sorted(sumDictionary.keys())   :
	print('This is the Total for sumDictionary[%75s] is %9.2f' %   (k, sumDictionary[k] ))




#   The next few statements are examples of string manipulation for training
#     Also examples of isinstance for identification


a = 47
b = 22.8
c = 'granola'
a1 = 'alsejfsbi  %d aseflief' % a
a2 = 'shnrgurg%swoifjse' % c  # this wont work, cant put string into %d chg'd to %s
b1 = 'aseinfse  %.2f  seifsfj' % b
b2 = 'aes%dsibjgsief   %.1f   girjgw' % ( a, b )
c1 = 'bigefs  %f    sefijg   %d  iesjfsf  %s seigjs' % ( b, a, c )
d1 = 'big string %s %s %s %s' % ( a1, b1, b2, c1 )

if isinstance( sumDictionary     , int  ) : print('sumDictionary is an integer!'       )
if isinstance( sumDictionary     , dict ) : print('sumDictionary is a dictionary!'     )
if isinstance( uniqueCategoryList, list ) : print('uniqueCategoryList is a list!'      )
if isinstance( sumDictionary     , float) : print('sumDictionary is a float!'          )
if isinstance( sumDictionary     , str  ) : print('sumDictionary is a string!'         )

print()
print('This is varible di%10s'  % d1)
print('Above line is a Formated string for Variable d1')
 

#    The next section is to perform sub Totals of a particlar Quicken Bank Account or a Quicken Category) by Month
#    The principle utility is by forming dictionarys of the information in the list "ListSorted".
#    The two dictionarys are "sumAccoountMonthDictionary", "sumCategoryMonthDictionary", and "sumMonthDictionary"  
#

newvariable = 0
sumMonthDictionary = {}
sumAccountMonthDictionary = {}
monthName = {'01':'January','02':'February','03': 'March','04': 'April', '05':'May'}

#    In the statements are the Variable designation for the Account Name 
#      not the raw file infomation where Category is the designation for the designation
#      for Auto:Fuel, Food:Groceries, Utilities and such.
#
for row in ListSorted :
	keyDate = row[1]
	keyMonth = keyDate.strftime("%m")
	if keyMonth not in sumMonthDictionary.keys() :
		sumMonthDictionary[keyMonth] = 0
	sumMonthDictionary[keyMonth] += row[9]
	keyAccountMonth = row[2] + '  ' + keyMonth + ' ' + '%10s' % monthName[keyMonth]
	if keyAccountMonth not in sumAccountMonthDictionary.keys() :
		sumAccountMonthDictionary[keyAccountMonth] = 0
	sumAccountMonthDictionary[keyAccountMonth] += row[9]
print()
for k in sorted(sumMonthDictionary.keys())   :
	keyMonth = monthName[k]
	print('A Monthly Total for %11s  is %9.2f' % (keyMonth,   sumMonthDictionary[k] ))

for k in sorted(sumAccountMonthDictionary.keys())   :
	print('A Monthly Total by Account for %95s is %9.2f' % (k, sumAccountMonthDictionary[k] ))



full_name = lambda first, last: 'full_name: %s %s first.title() last.title()'
print(full_name('guido','van rossum'))

ListSorted = sorted(csvData, key=lambda x: (x[6], x[1]) )
for row in ListSorted :
	s = '  '
	s += repr(row[1].strftime("%m %d %Y")) + '  '
	s += '%-45s' %repr(row[6]) + '  '   # negative is left justified
	s += '%-42s' %repr(row[2]) + '  '
	s += '%-35s' %repr(row[3]) + '  '  
	s += '%-20s' %repr(row[9]) + '  ' 
	print('Sorted $ value ' , s )

sumCategoryMonthDictionary = {}
for row in ListSorted :
	keyDate = row[1]
	keyMonth = keyDate.strftime("%m")

	keyCategoryMonth = row[6] + '  ' + keyMonth + ' ' + '%10s' % monthName[keyMonth]
	if keyCategoryMonth not in sumCategoryMonthDictionary.keys() :
		sumCategoryMonthDictionary[keyCategoryMonth] = 0
	sumCategoryMonthDictionary[keyCategoryMonth] += row[9]

print()

for k in sorted(sumCategoryMonthDictionary.keys())   :
	print('Monthly Total by a category for %55s is %9.2f' % (k, sumCategoryMonthDictionary[k] ))


import json
a = {'blah':'orange','keeper':'apple','laptop':[1,4,5,2],'storage':{'monkey':7}}
with open( 'json_example.json', 'w' ) as f :
   json.dump( a, f )
   # json.dump can be rewritten like:
   # b = json.dumps( a )
   # f.write(b)

# somestr = json.dumps( a ) # returns the variable 'a' encoded as a string

del a
try :
   print('a should be gone now:  %s' % repr(a) )
except NameError :
   print('no variable \'a\' in memory!')

with open('json_example.json','r') as f :
	a = json.load(f)
	print('a is now:',a)

    # json.load can be rewritten like
    # b = f.readlines()[0]
    # a = json.loads( b )
    # recovers the variable from a string

# 10 digit string : 10 bytes
# 10 digit number :  4 bytes (4*8 = 32, 2*32 possible binary combinations)
# json encodes & decodes via strings,
# bson encodes & decodes via binary bits

print('now a is back: |%s|' % repr(a) )
#   |stuff|
#   ||



