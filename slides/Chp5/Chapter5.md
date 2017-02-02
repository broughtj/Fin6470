% Chapter 5 - Financial Forwards and Futures 
% Tyler J. Brough
% \today

# Section 5.1 Alternative Ways to Buy a Stock 

## Introduction

- Financial futures and forwards
	- On stocks and indexes
	- On currencies
	- On interest rates
- How are they used?
- How are they priced?
- How are they hedged?


## Alternative Ways to Buy a Stock

- Four different payment and receipt timing combinations
	- Outright purchase: ordinary transaction
	- Fully leveraged purchase: investor borrows the full amount
	- Prepaid forward contract: pay today, receive the share later
	- Forward contract: agree on price now, pay/receive later

- Payments, receipts, and their timing

\begin{center}
 \includegraphics[width=7cm,height=4cm]{images/Picture1.png}
\end{center}


## Pricing Prepaid Forwards

- If we can price the _prepaid_ forward ($F^{P}$), then we can calculate the price
  for a forward contract

$$ 
F = \mbox{Future Value of \quad} F^{P}
$$

- Three possible methods to price prepaid forwards
	- Pricing by analogy
	- Pricing by discounted cash flows
	- Pricing by arbitrage
- For now, assume that there are no dividends


## Pricing Prepaid Forwards (cont'd)

- Pricing by analogy
	- In the absence of dividends, the timing of delivery is irrelevant
	- Price of the prepaid forward contract same as current stock price
	- $F^{P} = S_{0}$ (where the asset is bought at $t=0$, delivered at $t=T$)
- Pricing by discounted present value ($\alpha$: risk-adjusted discount rate)
	- If expected $t=T$ stock price at $t=0$ is $E_{0}(S_{T})$, then $F^{P} = E_{0}(S_{T}) e^{-\alpha T}$
	- Since $t=0$ expected value of price at $t=T$ is $E_{0}(S_{T}) = S_{0}e^{\alpha T}$
	- Combining the two, $F^{P}_{0,T} = S_{0} e^{\alpha T} = S_{0}$


## Pricing Prepaid Forwards (cont'd)

- Pricing by arbitrage
	- ___Arbitrage___: a situation in which one can generate positive cash flow by simultaneously buying
	  and selling related assets, with no net investment and with no risk. Free money!
	- If at time $t=0$, the prepaid forward price somehow exceeded the stock price, i.e., $F^{P}_{0,T} > S_{0}$,
	  an arbitrageur could do the following

\begin{center}
  \includegraphics[width=7cm, height=2cm]{images/Picture2.png}
\end{center}

- The price mechanism will ensure that these sort of arbitrage opportunities cannot persist,
  at equilibrium we can expect: $F^{P}_{0,T} = S_{0}$


## Pricing Prepaid Forwards (cont'd)

- What if there are dividends? Is $F^{P}_{0,T} = S_{0}$ still valid?
	- No, because the holder of the forward will not receive dividends that will be paid to the
	  holder of the stock, $F^{P}_{0,T} > S_{0}$ 
	- $F^{P}_{0,T} = S_{0}$ - PV(all dividends paid from $t=0$ to $t=T$)

- For discrete dividends $D_{t_{i}}$ at times $t_{i}, i = 1, \ldots, n$
	- The prepaid forward price: $F^{P}_{0,T} = S_{0} - \sum\limits_{i=1}^{n} PV_{0}(D_{t_{i}})$
	- For continuous dividends with an annualized yield $\delta$, the prepaid forward price is $F^{P}_{0,T} = S_{0} e^{-\delta T}$


## Pricing Prepaid Forwards (cont'd)

- Example 5.1
	- XYZ stock costs $\$100$ today and is expected to pay a quarterly dividend of $\$1.25$. 
	  If the risk-free rate is $10\%$ compounded continuously, how much does a $1$-year 
	  prepaid forward cost?
	- $F^{P}_{0,1} = \$100 - \sum\limits_{i=1}^{4} \$1.25 e^{-0.025 i} = \$95.30$


## Pricing Prepaid Forwards (cont'd)

- Example 5.2
	- The index is $\$125$ and the dividend yield is $3\%$ continously compounded. How
	  much does a $1$-year prepaid forward cost?
	- $F^{P}_{0,1} = \$125 e^{-0.03} = \$121.31$


# Section 5.3 Forward Contracts on Stock

## Pricing Forwards on Stock

- Forward price is the future value of the _prepaid_ forward price
	- No dividends
	- $F_{0,T} = FV(F^{P}_{0,T}) = FV(S_{0}) = S_{0}e^{rT}$
	- Continuous dividends

$$
F_{0,T} = S_{0} e^{(r - \delta)T}
$$


## Pricing Forwards on Stock (cont'd)

- Forward premium 
	- The difference between current forward price and stock price
	- Can be used to infer the current stock price from forward price
	- Definition:
		+ Forward premium: $F_{0,T} / S_{0}$
		+ Annualized forward premium = $(1/T) \ln{(F_{0,T}/S_{0})}$


## Creating a Synthetic Forward

- One can offset the risk of a forward by creating a _synthetic_ forward to offset a 
  position in the actual forward contract
- How can one do this? (assume continuous dividends at rate $\delta$)
	- Recall the long forward payoff at expiration = $S_{T} - F_{0,T}$
	- Borrow and purchase shares as follows

\begin{center}
 \includegraphics[width=6cm, height=2.5cm]{images/Picture3.png}
\end{center}

- Note that the total payoff at expiration is same as forward premium


## Creating a Synthetic Forward (cont'd)

- The idea of creating synthetic forward leads to following
	- Forward = Stock - zero-coupon bond
	- Stock = Forward - zero-coupon bond
	- Zero-coupon bond = Stock - forward
- Cash-and-Carry arbitrage: Buy the index, short the forward

\begin{center}
 \includegraphics[width=7cm, height=2.5cm]{images/Picture4.png}
\end{center}



## Creating a Synthetic Forward (cont'd) 

- Cash-and-carry arbitrage with transaction costs
	- Trading fees, bid-ask spreads, different
	  borrowing/lending rates, the price effect of trading in 
	  large quantities, make arbitrage harder
	- Suppose
		+ Bid-ask spreads: for stock $S^{b} < S^{a}$, and for forward $F^{b} < F^{a}$
		+ Cost $k$ of transacting forward
		+ Interest rate for borrowing and lending are $r^{b} < r^{l}$
		+ No dividends and no time $T$ transaction costs for simplicity
	- Arbitrage possible if
		+ $F^{b} > F^{+} = (S_{0}^{a} + 2k) e^{r^{b}T}$
		+ $F^{a} < F^{-} = (S_{0}^{b} - 2k) e^{r^{l}T}$


## Other Issues in Forward Pricing

- Does the forward price predict the future price?
	- According to the formula $F_{0,T} = S_{0} e^{-(r-\delta)T}$ the forward
	  price conveys no additional information beyond what $S_{0}$, $r$, and $\delta$ provides
	- Moreover, the forward price underestimates the future stock price
- Forward pricing formula and cost of carry

$$
\mbox{Forward Price} = \mbox{Spot Price} + \underbrace{\mbox{Interest to carry the asset} - \mbox{asset lease
rate}}_{\mbox{Cost of carry}, \quad (r - \delta) S} 
$$



# Section 5.4 Futures Contracts

## Futures Contracts

- Exchange-traded "forward contracts"
- Typically features of futures contracts
	- Standardized, with specified delivery dates, locations, procedures
	- A clearinghouse
		+ Matches buy and sell orders
		+ Keeps track of members' obligations and payments
		+ After matching the trades, becomes counterparty
- Differences from forward contracts
	- Settled daily through the mark-to-market process $\rightarrow$ low credit risk
	- Highly liquid $\rightarrow$ easier to offset an existing position
	- Highly standardized structure $\rightarrow$ harder to customize


# Section 5.5 Uses of Index Futures


# Section 5.6 Currency Contracts


# Section 5.7 Eurodollar Futures


