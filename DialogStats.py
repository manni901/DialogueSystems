from __future__ import division
import re
import csv

f = open('dialogue.txt', 'r')

dialogueTurns = {}
totalWords = {}
avgWordsPerTurn = {}
avgWordLength = {}

for speaker in ['A', 'B']:
	dialogueTurns[speaker] = 0
	totalWords[speaker] = 0
	avgWordsPerTurn[speaker] = 0
	avgWordLength[speaker] = 0

for line in f:

	if re.match("^\d", line): # Parse only dialogue lines which start with some number in the beginning

		# sub everything other than whitespace, alphabets, numbers. Remove whitespace at end.
		line = re.sub("[^\w\s]", '', line).rstrip()
		wordArray = re.split("\s+", line)
		
		# Array index 0 and 1 contain irrelevant data, index 2 contains the speaker identifier, rest are words
		speaker = wordArray[2]
		wordArray = wordArray[3:] 

		dialogueTurns[speaker] += 1
		totalWords[speaker] += len(wordArray)
		avgWordsPerTurn[speaker] = totalWords[speaker] / dialogueTurns[speaker]

		for word in wordArray:

			avgWordLength[speaker] += (len(word) - avgWordLength[speaker]) / totalWords[speaker]


writer = csv.writer(open("result.csv", 'w'))
headers = ["Interlocutor", "dialogueTurns", "totalWords", "avgWordsPerTurn", "avgWordLength"]
col_width = max(len(word) for word in headers) + 2
writer.writerow(headers)
print ''.join(header.ljust(col_width) for header in headers)

for speaker in ['A', 'B']:
	row = [speaker, str(dialogueTurns[speaker]), str(totalWords[speaker]), str(avgWordsPerTurn[speaker]), str(avgWordLength[speaker])]
	writer.writerow(row)
	print ''.join(val.ljust(col_width) for val in row)

print "\nSuccess! Output is in result.csv"	
