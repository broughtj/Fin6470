# __Chapter 2 (Hull): Futures Market Mechanics__

<br>

Finance 6470: Derivatives Markets <br>
Tyler J. Brough <br>
Last Update: February 14, 2019 <br>
<br>
<br>

## Futures Market Mechanics

<br>

Overview of topics in these notes:

* Clearing houses (FCMs, brokers, etc)
* Margin
    - initial (original)
    - maintenance (variation
* Cointegration

<br>

### __Clearninghouse:__

<br>

* Tasked with balancing all futures transactions/money flows
* Read Williams paper on _Origins of Futures Markets_
* Modern futures exchange a prime example of spontaneou order
* __CH:__ separate corp. or dept. associated with each exchange

<br>

* CH Roles:
    - Matches and reconciles all futures transactions
    - Assures financial integrity of transactions
    - Provides mechanism for delivery
* CH becomes obligor to every futures contract (reduces/manages counterparty risk)
* CH becomes party to and guarantees delivery
* Only members of exchanges can be clearning members (CM)
* CMs deposit large sum of money into a guarantee fund
    - usually must purchase shares of the corp.
    - the guarantee fund is a reserve in case of trader default/bankruptcy
* Exchange members who are not CMs must clear trades through a CM
  and pay a fee for service
* CMs are large/financially sound companies
* Maintains market stability and promotes a secure public image

<br>
    

<br>

* Pit trading vs LOB
* Traders matched through the brokers in pit, or through the LOB
* CH then becomes the counterparty to each futures contract
    - CH is long to the shorts
    - CH is short to the longs
    - CH has no net position (aside from clerical errors)
        + has a so-called _flat book_
    - This allows traders to originate and close out positions w/o search 
      for counterparty
    - CH transforms forward markets to be impersonal and easy to
      negotiate
    - Traders can hold their positions for long durations while
      the otherside may turnover very often


<br>

### __Margin Accounting__

<br>

* CH also performs a banking function
* Every trader must have an account w/ an FCM (possibly through an IB)
* For every trade, traders must deposit money called initial (original)
  margin
    - Serves as a performance bond
    - Both long and short must post margin
    - Usually around 10% of position (depends on trader, and
      volatility of the asset)
    - Brokers can require additional margin beyond exchange margin
      levels if necessary
* After initial margin, traders must often post additional deposits to
  keep a minimum margin level (usually 75% or 80% of initial margin)
    - Varies by contract (volatility)
      

<br>

<br>

* Initial (original) and maintenance (variation) margin applies to members of the clearing corp., who in turn
  apply it to FCMs, and FCMs duplicate this for their customers (IBs, traders)
    - FCMs only need to post on their net positions
    - FCMs can deposit excess margin in interest bearing securities (a non-trivial source of income)
    
<br>

* Margin accounting has the following functions:
    - guarantee performance on futures contracts
    - allows source of funds for daily settlement
    - provides the financial integrity of the system
    
<br>

### __Marking-to-Market__

<br>

* __Settlement price__: final price at the closing bell each day
    - Each delivery month of each contract has a daily settlement price
    - If a trader's position lost money for that day's trading session (depreciated in value)
      the CH debits the trader's account that day
    - If the trader's position appreciates the CH credits the trader's account that day
    - Also called _collects_ and _pays_
    - This process is called _marking-to-market_
    
<br>

__Q:__ What economic (risk management) role does it play?

<br>

__Example:__ two traders in Corn futures

<br>

- Long/Short 5000 bushel contract at $\$2.75$ per bushel
- Initial margin: $\$2000$

<br>

#### __Flow of Money Between Accounts__

<br>
<br>

<table>
    <thead>
        <tr>
            <th>Day</th>
            <th>Settlement Price</th>
            <th>Trader A (Long)<br>Cumulative Profits</th>
            <th>Trader A (Long)<br>Equity in Account</th>
            <th>Trader B (Short)<br>Cumulative Profits</th>
            <th>Trader B (Short)<br>Equity in Account</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>\$2.75</td>
            <td>0</td>
            <td>\$2,000</td>
            <td>0</td>
            <td>\$2,000</td>
        </tr>
        <tr>
            <td>2</td>
            <td>\$2.77</td>
            <td>+100</td>
            <td>\$2,100</td>
            <td>-100</td>
            <td>\$1,900</td>
        </tr>
        <tr>
            <td>3</td>
            <td>\$2.78</td>
            <td>+150</td>
            <td>\$2,150</td>
            <td>-150</td>
            <td>\$1,850</td>
        </tr>
        <tr>
            <td>4</td>
            <td>\$2.71</td>
            <td>-200</td>
            <td>\$1,800</td>
            <td>+200</td>
            <td>\$2,200</td>
        </tr>
    </tbody>
</table>

<br>
<br>

<br>

Let's see some numbers in Python!

<br>


```python
import numpy as np

contractSize = 5000                      # bushels
prc = np.array([2.75, 2.77, 2.78, 2.71]) # dollars per bushel
```


```python
prc
```




    array([2.75, 2.77, 2.78, 2.71])




```python
prcDiff = np.diff(prc)
prcDiff
```




    array([ 0.02,  0.01, -0.07])




```python
cashFlows = prcDiff * contractSize
```


```python
np.cumsum(cashFlows)
```




    array([ 100.,  150., -200.])



<br>

Let's see a longer/more complete simulation!

<br>


```python
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


## Main function

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
```

    Day t=1
    --------
    Settlement Price: 	2.76
    Profit: 		50.00
    Cumulative Profit: 	50.00
    Capital: 		2000.00
    Equity: 		2050.00
    Margin Call: 		0.00
    
    
    Day t=2
    --------
    Settlement Price: 	2.73
    Profit: 		-150.00
    Cumulative Profit: 	-100.00
    Capital: 		2000.00
    Equity: 		1900.00
    Margin Call: 		0.00
    
    
    Day t=3
    --------
    Settlement Price: 	2.68
    Profit: 		-250.00
    Cumulative Profit: 	-350.00
    Capital: 		2350.00
    Equity: 		1650.00
    Margin Call: 		350.00
    
    
    Day t=4
    --------
    Settlement Price: 	2.67
    Profit: 		-50.00
    Cumulative Profit: 	-400.00
    Capital: 		2350.00
    Equity: 		1950.00
    Margin Call: 		0.00
    
    
    Day t=5
    --------
    Settlement Price: 	2.69
    Profit: 		100.00
    Cumulative Profit: 	-300.00
    Capital: 		2350.00
    Equity: 		2050.00
    Margin Call: 		0.00
    
    
    Day t=6
    --------
    Settlement Price: 	2.64
    Profit: 		-250.00
    Cumulative Profit: 	-550.00
    Capital: 		2350.00
    Equity: 		1800.00
    Margin Call: 		0.00
    
    
    Day t=7
    --------
    Settlement Price: 	2.62
    Profit: 		-100.00
    Cumulative Profit: 	-650.00
    Capital: 		2650.00
    Equity: 		1700.00
    Margin Call: 		300.00
    
    
    Day t=8
    --------
    Settlement Price: 	2.63
    Profit: 		50.00
    Cumulative Profit: 	-600.00
    Capital: 		2650.00
    Equity: 		2050.00
    Margin Call: 		0.00
    
    
    Day t=9
    --------
    Settlement Price: 	2.67
    Profit: 		200.00
    Cumulative Profit: 	-400.00
    Capital: 		2650.00
    Equity: 		2250.00
    Margin Call: 		0.00
    
    


<br>
<br>

#### __Margin Calls__

<br>
<br>

When trader's equity in margin account falls below maintenance level, she receives a margin call from her broker/FCM

<br>

__Margin Call and Capital Withdrawal__

<br>

* 5000 bushel corn contract (long) at $\$2.75$ per bushel
* Maintenance margin level is $\$1,750$
* See the actual contract specs: [CME Corn Contract Specifications](https://www.cmegroup.com/trading/agricultural/grain-and-oilseed/corn_contract_specifications.html)

<br>

<table>
    <thead>
        <tr>
            <th>Day</th>
            <th>Settlement Price</th>
            <th>Cumulative Profits</th>
            <th>Capital</th>
            <th>Equity in Account</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>\$2.75</td>
            <td>\$0</td>
            <td>\$2,000</td>
            <td>\$2,000</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2.76</td>
            <td>+50</td>
            <td>2,000</td>
            <td>2,050</td>
        </tr>
        <tr>
            <td>3</td>
            <td>2.73</td>
            <td>-150</td>
            <td>2,000</td>
            <td>1,900</td>
        </tr>
        <tr>
            <td>4</td>
            <td>2.68</td>
            <td>-350</td>
            <td>2,000</td>
            <td>1,650</td>
        </tr> 
        <tr>
            <td><b>Margin Call of \$350</b></td>
            <td></td>
            <td><b>-350</b></td>
            <td><b>2,350</b></td>
            <td><b>2,000</b></td>
        </tr>
    </tbody>
</table>

<br>


__Example of Capital Withdrawal__

<br>

<table>
    <thead>
        <tr>
            <th>Day</th>
            <th>Settlement Price</th>
            <th>Cumulative Profits</th>
            <th>Capital</th>
            <th>Equity in Account</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>2.75</td>
            <td>0</td>
            <td>2,000</td>
            <td>2,000</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2.85</td>
            <td>+500</td>
            <td>2,000</td>
            <td>2,500</td>
        </tr>
        <tr>
            <td><b>Capital withdrawal of \$500</b></td>
            <td></td>
            <td><b>+500</b></td>
            <td><b>1,500</b></td>
            <td><b>2,000</b></td>
        </tr>
    </tbody>
</table>
        


```python

```
