import xlrd			# Read from excel
import xlwt			# Write to excel
import os
from random import randint

Q = []
A = {}

#############################
#	Excel grid explained	#
#############################
#	a1 = cell_value(0,0)	#
#	a2 = cell_value(1,0)	#
#	b3 = cell_value(2,1)	#
#############################


name = 'Questions'		# Excel sheet name

#############################
#	Read from Excel 		#
#############################


book_read = xlrd.open_workbook(os.path.join("Questions.xlsx"))		# Choose Excel file
sheet = book_read.sheet_by_name(name)								# Choose Excel sheet
i = 1																# Choose start column/row (to be used for looping)
while True:
	try:
		f = sheet.cell_value(i,0)									# Choose start column/row (row,column)
		Q.append(f)													# Add selected cell to list
		i += 1														# Increment i, change cell
	except IndexError:												# When cell is empty
		break														# End loop


# Read answers
for i in xrange(len(Q)):
	A[Q[i]]=sheet.cell_value(i+1,1)



# Initial values
tries = 0
streak = 0
streakrecord = 0
q = randint(0,len(Q)-1)

print '+-------->'
print '| Quiz time: %s' %(name)
print '+---------------------------------+'
print "| Commands: 'quit' 'exit'         |"
print '+---------------------------------+'
print '| 1st question;'


# Starting questions loop
while True:
	print '| %s' %(Q[q])
	answer = raw_input("| Answer: ")
	tries += 1
	
	if answer != A[Q[q]]:
		print '| Wrong answer!'

	if answer == A[Q[q]]:
		print '| Correct! try: %i' %(tries)
		if tries <= 1:
			streak += 1
		if streak >= 5:
			print "| Nice streak! %i in a row!" %(streak)
			if streak > streakrecord:
				print '+-------------------------->'
				print "| New streak record! %i" %(streak)
				print '+--------------------------------->'
		print '| Next Question;'
		q = randint(0,len(Q)-1)
		tries = 0
	
	
	if answer in ('quit', 'exit'):
		print '| Correct answer was: %s' %(A[Q[q]])
		print '| Bye bye!'
		print '+--------------------------------->'
		break

	

	elif tries > 5:
		print '| You failed 5 times, correct answer: %s' %(A[Q[q]])
		tries = 0
		if streak > streakrecord:
			streakrecord = streak
		#		print '+-------------------------->'
		#		print "| New streak record! %i" %(streak)
		#		print '+--------------------------------->'
		streak = 0
		q = randint(0,len(Q)-1)
		print '| Next Question;'
