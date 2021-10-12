with open('stock_fundamentals.txt') as fr:
	fw = open("rank_by_pe_ratio.txt", "a")
	stock_pe = {}
	stock = 'STOCK'
	for line in fr:
		line = line.strip()
		if 'ticker' in line:
			line = line.split()
			stock = line[2]
			stock_pe[line[2]] = -1
		if 'priceToEarningsRatio' in line:
			line = line.split()
			stock_pe[stock] = float(line[2])

	stock_pe = sorted(stock_pe.items(), key=lambda x: x[1], reverse=True)
	for k in stock_pe:
		fw.write(str(k) + "\n")
	
	fw.close()


with open('stock_fundamentals.txt') as fr:
	fw = open("rank_by_bookvalue.txt", "a")
	stock_pe = {}
	stock = 'STOCK'
	for line in fr:
		line = line.strip()
		if 'ticker' in line:
			line = line.split()
			stock = line[2]
			stock_pe[line[2]] = -1
		if 'priceToBookValue' in line:
			line = line.split()
			stock_pe[stock] = float(line[2])

	stock_pe = sorted(stock_pe.items(), key=lambda x: x[1], reverse=True)
	for k in stock_pe:
		fw.write(str(k) + "\n")
	
	fw.close()
	
with open('stock_fundamentals.txt') as fr:
	fw = open("rank_by_debtequity.txt", "a")
	stock_pe = {}
	stock = 'STOCK'
	for line in fr:
		line = line.strip()
		if 'ticker' in line:
			line = line.split()
			stock = line[2]
			stock_pe[line[2]] = -1
		if 'debtToEquityRatio' in line:
			line = line.split()
			stock_pe[stock] = float(line[2])

	stock_pe = sorted(stock_pe.items(), key=lambda x: x[1], reverse=True)
	for k in stock_pe:
		fw.write(str(k) + "\n")
	
	fw.close()
	
with open('stock_fundamentals.txt') as fr:
	fw = open("rank_by_freeCashFlow.txt", "a")
	stock_pe = {}
	stock = 'STOCK'
	for line in fr:
		line = line.strip()
		if 'ticker' in line:
			line = line.split()
			stock = line[2]
			stock_pe[line[2]] = -1
		if 'freeCashFlow' in line:
			line = line.split()
			stock_pe[stock] = float(line[2])

	stock_pe = sorted(stock_pe.items(), key=lambda x: x[1], reverse=True)
	for k in stock_pe:
		fw.write(str(k) + "\n")
	
	fw.close()