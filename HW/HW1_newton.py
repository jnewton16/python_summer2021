from random import uniform
class Portfolio(object):
    def __init__(self):
        self.cash = 0
        self.stocklist = {}
        self.fundlist = {}
        self.historylist = []
        self.stockprice = {}
        
    def __str__(self):
        return f'''Cash balance: ${self.cash}
Stock holdings: {self.stocklist}
Mutual Fund holdings: {self.fundlist}.'''
     
    def addCash(self, amount):
        self.cash += round(amount,2)
        self.historylist.append('Added ${:.2f} to the portfolio.'.format(round(amount,2)))
        return self.historylist[-1]

    def withdrawCash(self,amount):
        if amount > self.cash:
            print("ERROR: INSUFFICIENT FUNDS")
        else:
            self.cash -= (round(-amount,2))
            self.historylist.append('Withdrew ${:.2f} of cash from the portfolio.'.format(round(amount,2)))
            return self.historylist[-1]

    def buyStock(self,quantity,stock):
        if type(quantity) != int: 
            print('ERROR: CANNOT PURCHASE FRACTIONS OF A STOCK')
        elif self.cash < stock.price*quantity:
            print('ERROR: INSUFFICIENT FUNDS')
        else:
            if stock.symbol not in self.stocklist: 
                self.stocklist[stock.symbol] = quantity
            else:
                self.stocklist[stock.symbol] += quantity
            self.cash -= stock.price*quantity
            self.historylist.append('Purchased {} units of stock {} at ${} per unit.'.format(quantity,stock.symbol,stock.price))
            self.stockprice[stock.symbol] = stock.price
            return self.historylist[-1]

    def sellStock(self,symbol,quantity):
        if symbol not in self.stocklist or self.stocklist[symbol] < quantity:
            print('ERROR: INSUFFICIENT STOCK HOLDINGS')
        elif type(quantity) != int:
            print('ERROR: CANNOT SELL FRACTIONS OF A STOCK')
        else:
            self.stocklist[symbol] -= quantity
            x = self.stockprice[symbol]*uniform(.5,1.5)
            self.cash += round(x,2)*quantity
            self.historylist.append('Sold {} units of stock {} at price of ${:.2f} per unit.'.format(quantity,symbol,round(x,2)))
            return self.historylist[-1]

    def buyMutualFund(self,shares,fund):
        if shares>self.cash: 
            print('ERROR: INSUFFICIENT FUNDS')
        else:
            self.cash -= shares
            if fund.symbol not in self.fundlist:
                self.fundlist[fund.symbol] = shares
            else:
                self.fundlist[fund.symbol] += shares
            self.historylist.append('Purchased {:.2f} units of fund {} at $1 per share.'.format(shares,fund.symbol))
            return self.historylist[-1]

    def sellMutualFund(self,fund,shares):
        if fund not in self.fundlist or self.fundlist[fund] < shares:
            print('ERROR: INSUFFICIENT STOCK HOLDINGS')
        else:
            self.fundlist[fund] -= shares
            x = round(uniform(.9,1.2),2)
            self.cash += x*shares
            self.historylist.append('Sold {:.2f} shares of fund {} at ${} per share.'.format(shares,fund,x))
            return self.historylist[-1]
    
    def history(self):
        for i in range(0,len(self.historylist)):
            print("Transaction {}:".format(i),self.historylist[i])
        
class Stock(object):
    def __init__(self,price,symbol):
        self.price = price
        self.symbol = symbol
                
    def __str__(self):
        print("Stock {} sells for ${} per share.".format(self.symbol,self.price))
    
#use this to link price and symbol
class MutualFund(object):
    def __init__(self,symbol):
        self.symbol = symbol

    def __str__(self):
        print("Mutual Fund {}.".format(self.symbol))

portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20,"HFH")
portfolio.buyStock(5,s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3,mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT",3)
portfolio.sellStock("HFH",1)
portfolio.withdrawCash(50)
portfolio.history()
