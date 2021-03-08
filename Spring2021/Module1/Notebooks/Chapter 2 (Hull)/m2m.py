class MarginAccount(object):
    def __init__(self, spot_price, init_margin, var_margin, num_contracts, units):
        self.__ref_price = spot_price
        self.__init_margin = init_margin
        self.__var_margin = var_margin
        self.__num_contracts = num_contracts
        self.__units = units
        self.__equity = init_margin
        self.__capital = init_margin
        self.__profit = 0.0
        self.__cum_profit = 0.0
        self.__margin_call = 0.0

    def show(self):
        print("Settlement Price: \t{0:.2f}".format(self.__ref_price))
        print("Profit: \t\t{0:.2f}".format(self.__profit))
        print("Cumulative Profit: \t{0:.2f}".format(self.__cum_profit))
        print("Capital: \t\t{0:.2f}".format(self.__capital))
        print("Equity: \t\t{0:.2f}".format(self.__equity))
        print("Margin Call: \t\t{0:.2f}".format(self.__margin_call))
        print("\n")

    def update(self, spot_price):
        self.__profit = (spot_price - self.__ref_price) * (self.__num_contracts * self.__units)
        self.__cum_profit += self.__profit
        self.__equity = self.__capital + self.__cum_profit
        
        if self.__equity <= self.__var_margin:
            self.__margin_call = self.__init_margin - self.__equity
        else:
            self.__margin_call = 0.0
        
        self.__capital += self.__margin_call
        self.__ref_price = spot_price


def main():
    spot0 = 2.75
    spot_t = [2.76, 2.73, 2.68, 2.67, 2.69, 2.64, 2.62, 2.63, 2.67]
    units = 5000
    num_contracts = 1
    init_margin = 2000.0
    var_margin = 1750.0

    acc = MarginAccount(spot0, init_margin, var_margin, num_contracts, units) 

    for i, spot in enumerate(spot_t):
        acc.update(spot)
        print("Day t={0:d}".format(i+1))
        print("--------")
        acc.show()

if __name__ == "__main__":
    main()
