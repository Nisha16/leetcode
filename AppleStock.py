def get_max_profit(stock_prices_yesterday):
	max_profit = 0
	for earlier_time, ealrier_price in enumerate(stock_prices_yesterday):
		for later_price in stock_prices_yesterday[earlier_time:]:
			#earlier_time = min(outer_time, inner_time)
			#later_time = max(outer_time, inner_time)

			#ealrier_price = stock_prices_yesterday[earlier_time]
			#later_price = stock_prices_yesterday[later_time]

			potential_profit = later_price - ealrier_price

			max_profit = max(max_profit, potential_profit)

	return max_profit
	#earlier_time, later_time = lambda 