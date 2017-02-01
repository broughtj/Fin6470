% Chapter 2 - Mechanics of Futures Markets
% Tyler J. Brough
% \today

# Section 2.1 - Background

## Background

Derivatives are now actively traded all over the world.

Some derivatives exchanges:

- [\textcolor{blue}{\textit{CME Group}}](<www.cmegroup.com>), a merger from former exchanges:
	* The Chicago Board of Trade
	* The Chicago Mercantile Exchange
	* The New York Mercantile Exchange
- [\textcolor{blue}{\textit{InterContinental Exchange}}](<www.theice.com>), which is acquiring
	* [\textcolor{blue}{\textit{NYSE Euronext}}](<www.euronext.com>)
	* [\textcolor{blue}{\textit{Eurex}}](<www.eurexchange.com>)
	* [\textcolor{blue}{\textit{BM\&F BOVESPA}}](<www.bmfbovespa.com.br>)
	* [\textcolor{blue}{\textit{Tokyo Financial Exchange}}](<www.tfx.co.jp>)
	

## An Example

See here for the [\textcolor{blue}{\textit{CME Group's Corn Contract}}](<http://goo.gl/JpXSRY>).

- On June 5 a trader in NYC instructs his broker to buy $5,000$ bushels for delivery in September.
	* The broker issues orders for their trader to buy (take a long position)
	* Each corn contract is for the delivery of exactly $5,000$ bushels
- At about the same time, a trader in Kansas instructs a broker to sell $5,000$ bushels of corn for September delivery.
	* The broker issues orders for their trader to sell (take a short position) in one corn contract
- A price is determined and the deal is done
- In tradition (old style) open outcry markets the two traders (from different brokers) would meet on the trading floor to determine the trade price
- With electronic markets, a computer system called a **matching engine** matches the two traders

## Example Continued

- The NYC trader has a *long futures position* in one contract
- The Kansas trader has a *short futures position* in one contract
- The transaction price agreed upon is the current *futures price* for September corn (say $600$ cents per bushel)
	* Like all other prices this price is determined by the forces of supply and demand

## Closing Out Positions

- The vast majority of contracts do not lead to physical delivery of the underlying
- Most traders close out their positions prior to delivery (as specified in the contract)
	* This means taking an offsetting (opposite) position relative to the original one
	* i.e. the NYC trader would sell (go short) one contract, and the Kansas trader would buy (go long) one contract just prior to the delivery date (say August 25)
	* In each case, the trader's gain is determined by the difference between the futures price on June 5 and the day the contract is closed out
- Delivery is so uncommon that traders often forget how the delivery process works (see *Business Snapshot 2.1*)
- We will however review the delivery process later, because this is how the futures price is tied to the spot price!


# Section 2.2 - Specification of a Futures Contract

## Futures Contracts

- Available on a wide range of assets
- Exchange traded
- Specifications need to be defined:
	* What can be delivered,
	* Where it can be delivered, &
	* When it can be delivered
- Settled daily


## The Asset

- When the underlying is a commodity, there can be variation in quality 
	* The contract must then stipulate the grade(s) of what is acceptable for delivery
- Ex: ICE has specified the asset in its orange juice futures contract as frozen concentrates that are:
	* US Grade A with Brix value of not less than $62.5$ degrees
- For some contracts there is a variation in grades, but prices vary with the grades
	* Ex: CMD Group's corn futures contracts (No. 1 yellow, No. 2 yellow, etc)
- The asset for financial futures are typically unambiguous (e.g. Japanese yen)
	* Treasury bond and Treasury note futures (range of maturities)
	

## The Contract Size

- Contract size specifies the amount of the asset to be delivered under one contract
- An important issue for the exchange:
	* If too large, small traders will be unable to take positions
	* If too small, trading can become expensive (fees per contract)
- The correct size depends upon the likely end user
- Typical values for agricultural futures from $\$10,000$ to $\$20,000$
- Typical values for financial futures (e.g. Treasury bonds) something like $\$100,000$
- A recent trend is to introduce "mini" contract sizes
	* [\textcolor{blue}{\textit{CME Group E-Mini SP500 Contract}}](<http://goo.gl/Y4tjiA>)
	* [\textcolor{blue}{\textit{CME Group E-Mini NASDAQ 100 Contract}}](<http://goo.gl/1akYiJ>)


## Delivery Arrangements

- The place of delivery must be specified in the contract
- This is especially important for commodities that entail significant transportation costs
- ICD frozen concentrate OJ delivery is to exchange-licensed warehouses in FL, NJ, or DE
- The price received by the short party is sometimes adjusted according to location
- Price tends to be higher for locations relatively farther away from the main sources of the commodity


## Delivery Months

- Contracts referred to by delivery date (e.g. July corn)
- The exchange must specify the precise period during the month when delivery can be made
- Delivery months vary by contract to meet needs of traders
	* Ex: CME Group Corn delivery months of Mar, May, Jul, Sep, and Dec
- At a given time, contracts trade for the closest delivery month and a number of subsequent delivery months
- The exchange determines when a particular delivery month will begin trading
- Trading typically ceases a few days before the last day of of the delivery period


## Price Quotes

- The exchange determines how prices will be quoted
	* Ex: US crude oil futures contracts quoted in dollars and cents
	* Ex: Treasury bond and Treasury note futures prices are quoted in dollars and thirty-seconds of a dollar


## Price Limits and Position Limits

- Most contracts have daily price limits determined by the exchange
	* *limit down* is the state when the price declines from the previous day's closing price by the daily price limit
	* *limit up* is the state when the price increases from the previous day's closing price by the daily price limit
	* A *limit move* is a daily price change in either direction equal to the daily price limit
- Usually trading ceases for the day when the contract is either limit up or limit down
- In some cases the exchange can step in and change the limits
- The idea of price limits is to prevent large price movements due to excess speculation
- This can be an artificial barrier to trading 
- *Position limits* are the maximum number of contracts that a speculator may hold.
	* The purpose is to prevent undue influence (*e.g. Hunt Brothers*)


# Section 2.3 - Convergence of Futures Price to Spot Price

## Price Convergence 

- As the delivery period is approached, the futures price converges to the spot price
- At delivery the futures price should be equal to the spot price
	* The futures contract converts to a physical position in the asset
- This is no-arbitrage logic


## Basic No-Arbitrage Logic at Delivery

To see this suppose that at delivery the futures price is above the spot price. Then there
is a clear arbitrage strategy:

1. Sell (i.e. short) a futures contract
2. Buy the asset
3. Make delivery

- This should lead to an arbitrage profit equal to the difference between the futures and spot prices.
- As traders exploit this arbitrage, the futures price will converge to the spot price 
- *Question:* how to would it work if the futures price were below the asset at delivery?


## Price Convergence Continued

Relationship between futures price and spot price as delivery approaches: (a) futures price above spot price;
(b) futures price below spot price.

\begin{center}
  \includegraphics[width=10cm,height=5cm]{OFOD9_02-01.eps}
\end{center}


# Section 2.4 - The Operation of Margin Accounts

## Counter-party Risk and Margins

- Bilateral trade has obvious risks concerning the trustworthiness of the counter party
	* This can be due to dishonesty and fraud
	* Or it may be simply the trader may lack the resources to honor the agreement
- One key role of the exchange is to organize trading to avoid default
- Margin accounts are essential in this process


## Daily Settlement

- Consider an investor who buys two Dec gold futures contracts on the NYMEX (part of the CME Group)
- Suppose that current futures price is $\$1,450$ per ounce
- The contract size is $100$ ounces, so the investor has contract to buy $200$ ounces at this price
- The broker will require the investor to post margin into an account
- The initial amount that must be deposited is known as the *initial margin*
- Suppose that this is $\$6,000$ per contract, so $\$12,000$ total
- At the end of each trading day the margin is adjusted to reflect the investor's gain or loss
- This is known as *daily settlement* or *marking to market*


## Daily Settlement

\begin{center}
  \includegraphics[width=15cm,height=14cm]{Table2-1.pdf}
\end{center}


## The Clearing House and Its Members

- A *clearing house* (CH) acts as an intermediary in futures trading. 
- The CH guarantees performance of both parties
- Brokers must be CH members or work through other brokers who are members
- The CH collects information to calculate the net positions of members
- CH members must post *initial margin*, margin that reflects the number of contracts to be cleared (calculated on net positions)
- CH members must contribute a guaranty fund


## Credit Risk

- The purpose of margin is guarantee that the trader who earns a profit gets paid
- Historically this has been a very successful system
- October 19, 1987 tested the system severely
	* The SP500 index declined by over $20\%$ 
	* Long SP500 futures traders had large negative margin balances
	* Those that couldn't pay had their positions closed out
	* Some brokers went bankrupt who had guaranteed their clients
	* But the CH's had sufficient funds to ensure short traders were paid


# Section 2.5 - Over-The-Counter (OTC) Markets

## OTC Markets

- OTC markets are where traders agree to trade derivatives without involving an exchange
- *Credit risk* has been a characteristic of these types of trading organization
- To reduce credit risk, OTC markets have borrowed ideas from exchanges


## Central Counterparies

- *Central counterparies* (CCP's) are clearing houses for standard OTC markets
- CCP's play a similar role as those of exchange clearing houses
- Members of a CCP must post initial margin and daily variation margin
- Members also contribute to a guaranty fund


## CCP's Continued

- When A and B agree on a transaction, they can present the trade to the CCP
- The CCP becomes the counterparty to both A (long) and B (short)
- The CCP agrees to:
	1. Buy the asset from B in one year for the agreed price, and
	2. Sell the asset to A in one year for the agreed price.
	3. It takes the credit risk of both A and B 
- Traders in a CCP cleared market post initial margin and daily variation margin
- Traders must trade through a CCP member firm
- Regulation since 2007 has basically required all OTC transactions be cleared through a CCP


## Bilateral Clearning

- Transactions not cleared through a CCP are cleared bilaterally.
- In such a market, traders A and B enter into a master agreement covering all trades 
	* The most common form of a master agreement is a *International Swaps and Derivatives Association* (ISDA) Master Agreement.
- Typically the ISDA contains a *credit support annex* (CSA) requiring collateral - this functions similar to margin
	* Typical arrangements in CSA's require daily valuations
	* Initial margin has been rare
	* Regulation since 2012 has changed this requiring initial and variation margin


## Bilateral vs. CCP's

Figure 2.2 (a) The traditional way in which OTC markets have operated: a series of bilateral agreements between traders; 
(b) how OTC markets would operate with a single central counterparty (CCP) acting as a clearing house.

\begin{center}
  \includegraphics[width=9cm,height=5.5cm]{OFOD9_02-02.eps}
\end{center}


## Futures Trades vs. OTC Trades

- Regardless of clearing mechanism, initial margin typically earns interest
- Daily variation margin on futures exchanges does not earn interest
- OTC transactions are typically not valued daily
	* Daily variation margin in OTC markets, whether through a CCP or with a CSA, usually do earn interest
- Securities can usually be used to satisfy margin/collateral requirements
	* Security values are usually reduced by a certain amount for margin
	* This is called a *haircut*


# Section 2.6 - Market Quotes

## Market Quotes

- See page 36 of the text for Table 2.2, which presents examples of price quotations (CME Group)
- Go to [\textcolor{blue}{\textit{CME Group}}](<www.cmegroup.com>) for current price quotes.


## Some Terms 

- *Settlement price* is the price used for calculating daily gains/loses and margin requirements
	* It is usually the last trade price of a daily trading session
- *Trading volume* is the number of contracts traded in a day
- *Open interest* is the number of contracts outstanding
	* Equal to the number of long positions (equivalently the number of short positions)
- A *normal market* is the case when quoted prices are increasing as a function of maturity
- An *inverted market* is the case when quoted prices are a decreasing function of maturity


# Section 2.7 - Delivery

## Delivery

- The vast majority of futures positions **DO NOT** result in physical delivery
- Yet the possibility of delivery is crucial for price determination
- Exchanges determine the delivery period, and it varys by underlying asset
- The short position in a transaction typically decides when within the delivery period to deliver and 
  files an "intent to deliver" with the CH
	* The CH then chooses a long counterparty to take delivery
	

## Cash Settlement

- Some contracts, such as financial futures, are settled in cash
- For some assets it is inconvenient (or even impossible) to make physical delivery
	* Ex: the SP500 contract would require delivering 500 individual stocks in exactly the right portfolio weights
	* This would necessitate enormous transactions costs
- Cash settled contracts are all closed out on a predetemined date
- The settlement price is the *spot price* either at open or close of that trading day
	* Ex: the SP500 contract settlement price is the level of the SP500 upon open on the third Friday of the delivery month


# Section 2.8 - Types of Traders and Trades

## Trader Types

- There are two main types of traders on futures exchanges:
	1. *Futures commission merchants* (FCMs) - which are brokers that execute orders on behalf of clients and charge a commission
	2. *Locals* - who trade on their own accounts
- Traders taking positions in futures, whether locals or through FCMs can be categorized as:
	* *Hedgers* 
	* *Speculators*
	* *Arbitrageurs* 
	
	
## Orders

There are different types of orders:

- *Market orders* are the simplest type of order. It is an instruction to transact at the available price immediately available
- *Limit orders* specifies a particular price - the *limit price* - and can only be executed at this price or one more favorable
	* A *limit buy order* is an order to buy at a price no greater than the limit price
	* A *limit sell order* is an order to sell at a price no less than the limit price
	* Limit order aggregate in the *limit order book* while waiting to be executed
	* Limit orders must also specify a quantity to be traded
- A *stop order* or *stop-loss order* is executed at the most favorable price once a bid or offer has been made at the stop price


## Orders Continued

- A *stop-limit order* is a combination of a stop-loss order and a limit order
	* It becomes a limit order at the limit price once the stop price has been reached 
	* It must specify a limit price and a stop price
- A *discretionary order* or *market-not-held* order is market order than can be delayed by the broker in an attempt to achieve a better price
- A *time-of-day* order specifies a particular time of day when the order can be executed
	* An *open order* or *good-till-canceled order* is one that can be excuted until end of trading
	* A *fill-or-kill order* must be executed immediately or not at all
- A *market-if-touched* (MIT) order becomes a market order once a trade occurs at a specified price or one more favorable


# Section 2.9 - Regulation

## US Regulation

- Futures market (most) are requlated by the [\textcolor{blue}{\textit{Commodity Futures Trading Commission (CFTC)}}](<www.cftc.gov) 
- The [\textcolor{blue}{\textit{National Futures Association}}](<www.nfa.futures.org>) is a self-regulatory body set up to implement CFTC policies
- Participants in futures markets must be licensed and registered by the NFA (series 3 & 30 exams)
- The Dodd-Frank Act signed by Obama in 2010 significantly expanded the role of the CFTC 
	* See [\textcolor{blue}{here}](<http://streetwiseprofessor.com/?p=9472>) for commentary by Craig Pirrong


## Trading Irregularities

- Futures markets typically operate incredibly efficiently and in the public interest
- A *market corner* is a situation where a trader takes a massive long position and can thereby exercise some market control on spot prices
- See the [\textcolor{blue}{\textit{monograph by Williams}}](<http://goo.gl/GMhedr>) for a fascinating case concerning the infamous Hunt Brothers
- See also the Pirrong paper for a discussion of the [\textcolor{blue}{\textit{Ferruzzi Soybean Episode}}](<http://aler.oxfordjournals.org/content/6/1/28.short>)
	* More [\textcolor{blue}{here}](<http://streetwiseprofessor.com/?p=8572>)
- We will discuss other forms of price manipulation 
	
# Section 2.10 - Accounting and Taxes

## Accounting and Taxes

- Read this section on your own at your leisure


# Section 2.11 - Forward vs. Futures Contracts

## Comparing Forwards and Futures

\begin{center}
  \includegraphics[width=9cm,height=5cm]{Table2-3.pdf}
\end{center}