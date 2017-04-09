import DataType as D
import sys


def Read(fileName):
	f = open(fileName, 'r')
	
	line = []
	while True:
		tmp = f.readline()
		
		if not tmp : break
		
		line.append(tmp)
	f.close()
	
	#split data & store

	print len(line)
	data = D.Data(2, len(line))
	for i in range(0, len(line)):
		lineSplited  = line[i].split(' ')
		data.label[i] = lineSplited[0]
		 
		data.X[i][0] = lineSplited[1].split(':')[1]
		data.X[i][1] = lineSplited[2].split(':')[1]
		print data.label[i], data.X[i][0], data.X[i][1]





	
