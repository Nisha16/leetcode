
"""http://stackoverflow.com/questions/9514191/maximizing-profit-for-given-stock-quotes"""
def max_profit(array):
	maximum = 0
	size = len(array)
	profit = 0
	temp = [1] * len(array) # 1 for buy, 0 for sell
	for i in range(size-1,-1,-1):
		ele = array[i]
		if maximum <= ele:
			temp[i] = 0 #buy
			maximum = ele
		profit = profit + maximum - ele
		print "p,m,ele: ", profit, maximum, ele	
		# else:
		# 	temp[i] = 1
		# 	profit = profit - ele
		# 	maximum = ele
	print "Profit: ", profit
	print "temp: ", temp

stock = [1,3,1,2]
max_profit(stock)











