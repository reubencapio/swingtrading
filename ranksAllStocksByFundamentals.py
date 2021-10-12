import re
from collections import defaultdict

stocksFundamentalRank = {}


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


with open('rank_by_bookvalue.txt') as fr:
	for line in fr:
		ctr1 += 1
		stock = line.split('\'')[1::2]
		stock = stock[0]	
		ctr2 = readFile(stock, 'rank_by_debtequity.txt')
		ctr3 = readFile(stock, 'rank_by_freeCashFlow.txt')
		ctr4 = readFile(stock, 'rank_by_pe_ratio.txt')
		sumOfRanks = ctr1+ctr2+ctr3+ctr4
		stocksFundamentalRank[stock] = sumOfRanks
		#fw.write(stock + " , " + str(ctr1) + " , " + str(ctr2) + " , " + str(ctr3) + " , " + str(ctr4) +  " == " + str(ctr1+ctr2+ctr3+ctr4) +  "\n")


stocksFundamentalRank = sorted(stocksFundamentalRank.items(), key=lambda x: x[1], reverse=False)
fw = open("ranksAllStocksFundamentals.txt", "a")
for m in stocksFundamentalRank:
	print(str(m))
	fw.write(str(m) + "\n")
fw.close()
