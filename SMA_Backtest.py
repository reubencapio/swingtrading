from datetime import datetime
import backtrader as bt
import yfinance as yf


# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=3,  # period for the fast moving average
        pslow=7   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position




# Create a data feed
data = bt.feeds.YahooFinanceData(dataname='TSLA',
                                 fromdate=datetime(2021, 9, 1),
                                 todate=datetime(2021, 9, 30))
								 
cerebro = bt.Cerebro()  # create a "Cerebro" engine instance
cerebro.adddata(data)  # Add the data feed
cerebro.broker.setcash(100000.0)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.addstrategy(SmaCross)  # Add the trading strategy
# Run over everything
cerebro.run()
# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
#cerebro.plot()  # and plot it with a single command