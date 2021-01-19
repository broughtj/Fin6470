class MarketMaker(object):
    def __init__(self, spot):
        self.__spot = spot

    def show(self):
        pass

    def update(self, spot):
        pass


## Main
spot0 = 40.0
spot_t = [40.50, 39.25, 38.75, 40.0, 40.0]
mm = MarketMaker(spot0)

for t, spot in enumerate(spot_t):
    mm.update(spot)
    mm.show()
