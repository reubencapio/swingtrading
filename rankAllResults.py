import re
from collections import defaultdict

ranks = defaultdict(list)


ctr1 = 0
ctr2 = 0
ctr3 = 0
ctr4 = 0


def readFile(stock, fileToRead):
	ctr = 0
	with open(fileToRead) as fr:
		for line in fr:
			ctr += 1
			if stock in line:
				return ctr

fw = open("ranksAllStocksFundamentals.txt", "a")
with open('rank_by_bookvalue.txt') as fr:
	for line in fr:
		ctr1 += 1
		stock = line.split('\'')[1::2]
		stock = stock[0]	
		ctr2 = readFile(stock, 'rank_by_debtequity.txt')
		ctr3 = readFile(stock, 'rank_by_freeCashFlow.txt')
		ctr4 = readFile(stock, 'rank_by_pe_ratio.txt')
		fw.write(stock + " , " + str(ctr1) + " , " + str(ctr2) + " , " + str(ctr3) + " , " + str(ctr4) +  " == " +   "\n")
fw.close()


