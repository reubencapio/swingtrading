import re
from collections import defaultdict

ranks = defaultdict(list)


ctr1 = 0
ctr2 = 0

mappingStocks = {}

def readFile(stock, fileToRead):
	ctr = 0
	with open(fileToRead) as fr:
		for line in fr:
			ctr += 1
			if stock in line:
				return ctr

	return 1000000	
	
fw = open("ranksAllStocksFundamentals.txt", "a")
with open('stockProfitsSMA.txt') as fr:
	for line in fr:
		ctr1 += 1
		stock = line.split('\'')[1::2]
		stock = stock[0]	
		ctr2 = readFile(stock, 'ranksAllStocksFundamentals.txt')
		mappingStocks[stock] = ctr1 + ctr2
		#print(stock + " , " + str(ctr1 + ctr2) )
		#exit()
		#fw.write(stock + " , " + str(ctr1 + ctr2) + " \n"  )

mappingStocks = sorted(mappingStocks.items(), key=lambda x: x[1], reverse=False)

for m in mappingStocks:
	print(m)
	fw.write(m + " \n"  )
fw.close()


