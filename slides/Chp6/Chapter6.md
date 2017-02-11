% Chapter 6 - Commodity Forwards and Futures 
% Tyler J. Brough
% \today

# Section 6.1 Introduction to Commodity Forwards 

## Introduction to Commodity Forwards

- Commodity forward prices can be described by the same formula as that for financial forward prices

\begin{equation*}
 F_{0,T} = S_{0} e^{(r - \delta)T}
\end{equation*}


## Introduction to Commodity Forward (Cont'd)

- For financial assets, $\delta$ is the dividend yield

- For commodities, $\delta$ is the commodity lease rate
	* The lease rate is the return that makes an investor willing to buy and then lend a commodity
	* The lease rate for a commodity can typically be estimated only by observing the forward prices


## Introduction to Commodity Forward (Cont'd)

- Differences between commodities and financial assets include
	* Storage costs
	* Carry markets
	* Lease rate
	* Convenience yield


## Introduction to Commodity Forward (Cont'd)

- The set of prices for different expiration dates for a given commodity is called the __forward rate__ (or the
  __forward strip__) for that date

- If on a given date the forward curve is upward sloping, then the market is in __contango__. If the forward curve is
  downward sloping, the market is in __backwardation__
	* Note that forward curves can have portions in backwardation and portions in contango


# Section 6.2 Equilibrium  Pricing of Commodity Forwards 

## Equilibrium Pricing of Commodity Forwards

- As with financial forwards, the commodity forward price is a biased estimate of the expected spot price, $E(S_{T})$,
  with the bias due to the risk premium on the commodity, $r - \alpha$. (___NB___: $r - \alpha = -(\alpha - r)$).

\begin{equation*}
 F_{0,T} = E_{0}(S_{T})e^{-(\alpha - r)T}
\end{equation*}


## Introduction to Commodity Forwards (Cont'd)

- The set of prices for different expiration dates for a given commodity is called the __forward curve__ (or the
  __forward strip__) for that date

- If on a given date the forward curve is upward sloping, then the market is in __contango__. If the forward curve is
  downward sloping, the market is in __backwardation__
	* Note that forward curves can have portions in backwardation and portions in contango


## Equilibrium Pricing of Commodity Forwards

- As with financial forwards, the commodity forward price is a biased estimate of the expected spot price,
  $E_{0}(S_{T})$, with the bias due to the risk premium on the commodity, $r - \alpha$. (Note that $r - \alpha =
  -(\alpha - r)$)

\begin{equation*}
 F_{0,T} = E_{0}(S_{T})e^{-(\alpha - r) T}
\end{equation*}


## Equilibrium Pricing of Commodity Forwards (Cont'd)

- Different commodities have their distinct forward curves, reflecting different properties of
	* Storability
	* Storage costs
	* Production
	* Demand
	* Seasonality


## Short-selling and the Lease Rate

- Suppose we engage in a reverse cash-and-carry for copper. The price of copper today is $\$3$ and the price of copper
  in one year is $F_{0,1}$. The risk-free rate is $10\%$.

\begin{center}
 \includegraphics[width=7cm,height=4cm]{images/table6-3.png}
\end{center}

\vspace{3mm}

- A copper borrower must make an extra payment, a lease payment, due to the difference in the current and forward
  prices.


## Short-selling and the Lease Rate (Cont'd)

- The lease rate is the difference between the commodity discount rate, $\alpha$, and the expected growth rate of the
  commodity price

\begin{equation*}
 \delta_{1} = \alpha - \frac{1}{T} \ln{\left[E_{0}(S_{T}) / S_{0}\right]}
\end{equation*}

\vspace{3mm}

- For a commodity owner who lends the commodity, the lease rate is like a dividend
	* With the stock, the dividend yield, $\delta$, is an observable characteristic of the stock
	* With a commodity, the lease rate, $\delta_{1}$, is income earned only if the commodity is loaned. It is not
	  directly observable, except if there is a lease market


## Short-selling and the Lease Rate (Cont'd)

- The lease rate has to be consistent with the forward price

- Therefore, when we observe the forward price, we can infer what the lease rate would have to be if a lease market
  existed

- The annualized lease rate

\begin{equation*}
 \delta_{1} = r - \frac{1}{T} \ln{F_{0,T} / S}
\end{equation*}


# Section 6.3 Pricing Commodity Forwards by Arbitrage

## No-Arbitrage Pricing Incorporating Storage Costs

- A commodity for which the forward price compensates a commodity owner for costs of storage is called a __carry
  market__

- The cost of storing a physical item such as corn or copper can be large relative to its value

- Moreover, some commodities deteriorate over time, which is also a storage cost


## No-Arbitrage Pricing Incorporating Storage Costs (Cont'd)

- Cash-and-carry arbitrage when the storage costs from time $0$ to $T$ are $\lambda(0,T)$

\begin{center}
 \includegraphics[width=7cm,height=4cm]{images/table6-4.png}
\end{center}

\vspace{3mm}

- A copper borrower must make an extra payment, a lease payment, due to the difference in the current and forward
  prices.


## Short-selling and the Lease Rate (Cont'd)

- The lease rate is the difference between the commodity discount rate, $\alpha$, and the expected growth rate of the
  commodity price

\begin{equation*}
 \delta_{1} = \alpha - \frac{1}{T} \ln{\left[E_{0}(S_{T}) / S_{0}\right]}
\end{equation*}

\vspace{3mm}

- For a commodity owner who lends the commodity, the lease rate is like a dividend
	* With the stock, the dividend yield, $\delta$, is an observable characteristic of the stock
	* With a commodity, the lease rate, $\delta_{1}$, is income earned only if the commodity is loaned. It is not
	  directly observable, except if there is a lease market


## Short-selling and the Lease Rate (Cont'd)

- The lease rate has to be consistent with the forward price

- Therefore, when we observe the forward price, we can infer what the lease rate would have to be if a lease market
  existed

- The annualized lease rate

\begin{equation*}
 \delta_{1} = r - \frac{1}{T} \ln{F_{0,T} / S}
\end{equation*}


# Section 6.3 Pricing Commodity Forwards by Arbitrage

## No-Arbitrage Pricing Incorporating Storage Costs

- A commodity for which the forward price compensates a commodity owner for costs of storage is called a __carry
  market__

- The cost of storing a physical item such as corn or copper can be large relative to its value

- Moreover, some commodities deteriorate over time, which is also a storage cost


## No-Arbitrage Pricing Incorporating Storage Costs (Cont'd)

- Cash-and-carry arbitrage when the storage costs from time $0$ to $T$ are $\lambda(0,T)$

\begin{center}
 \includegraphics[width=7cm,height=4cm]{images/table6-4.png}
\end{center}

\vspace{3mm}

- $F_{0,1}$ should not exceed $(1+R)S_{0} + \lambda(0,1)$. If the forward price were greater, you could undertake a
  simple cash-and-carry after paying storage costs and interest


## No-Arbitrage Pricing Incorporating Storage Costs (Cont'd)

- If $F_{0,T}$ is greater than or equal to $(1+R)S_{0} + \lambda(0,1)$ then storage will occur because the forward
  premium is great enough that sale proceeds in the future compensate for the financial costs of storage $(RS_{0})$ and
  the physical costs of storage ($\lambda(0,1)$)

- When costly storage occurs, the forward rate can rise faster than the interest rate

- We can view storage costs as a negative dividend

- Storage costs can include depreciation of the commodity, which is less a problem for metals such as copper than it is
  for commodities such as strawberries or electricity


## No-Arbitrage Pricing Incorporating Storage Costs (Cont'd)

- If interest rates and storage costs are paid continuously and are proportional to the value of the commodity, and
  there is no arbitrage

\begin{equation*}
 F_{0,T} = S_{0} e^{(r + \lambda)T}
\end{equation*}

\vspace{3mm}

- If the forward price were greater, you could undertake a simple cash-and-carry and earn a profit after paying both
  storage costs and interest on the position


## No-Arbitrage Pricing Incorporating Storage Costs (Cont'd)

- Some holders of a commodity receive benefits from physical ownership (e.g., a commercial user). This benefit is called
  the commodity's __convenience yield__

- If there is a continuously compounded convenience yield, $c$, then

\begin{equation*}
 F_{0,T} \ge S_{0}e^{(r + \lambda - c)T}
\end{equation*}

\vspace{3mm}

- A user who buys and stores the commodity will be compensated for interest and physical storage costs less a
  convenience yield

- The commodity lease rate will be $\delta_{1} = c - \lambda$


# Section 6.5 Corn

## Corn

- Corn is harvested primarily in the fall. In order to be consumed when it is not produced, it must be stored.

\begin{center}
 \includegraphics[width=7cm,height=4cm]{images/figure6-6.png}
\end{center}

\vspace{3mm}

- In a typical year, once the harvest begins, storage is no longer necessary. Those storing corn will plan to deplete
  inventory as harvest approaches and to replenish inventory from the new harvest. The corn price will fall at harvest,
  only to begin rising again after the harvest


# Section 6.6 Energy Markets

## Energy Markets: Electricity

- Electricity has the following characteristics
	* It cannot be easily stored. Therefore, it is not possible to engage in arbitrage
	* At any point in time, the maximum supply of electricity is fixed
	* Demand for electricity varies substantially by season, by day of week, and by time of day


## Energy Markets: Electricity (Cont'd)

- Given these characteristics, electricity forwards have large price swings over the day. Price swings reflect changes
  in the expected spot price, which in turn reflects changes in demand over the day

\begin{center}
 \includegraphics[width=6cm,height=4cm]{images/table6-7.png}
\end{center}

- The forward prices in Table 6.7 provide price discovery, revealing otherwise unobtainable information about the future
  price of the commodity. The prices are best interpreted using equation (6.4)


# Section 6.8 Synthetic Commodities

## Synthetic Commodities

- A synthetic commodity can be created by combining a forward contract with a zero-coupon bond

\vspace{3mm}

| Investment strategy      | Cost at time 0  | Payoff at time T       |
|--------------------------|:---------------:|:----------------------:|
| A long commodity forward |                 |                        | 
| contract at the price    | $0$             | $S_{T} - F_{0,T}$      |  
| $F_{0,T}$                |                 |                        |
|                          |                 |                        |
| A zero-coupon bond that  |                 |                        |
| pays $F_{0,T}$ at time T | $F_{0,T}/(1+R)$ | $F_{0,T}$              |
|--------------------------|-----------------|------------------------|
|                          |                 |                        |
| Total                    | $F_{0,T}/(1+R)$ |  $S_{T} =$ the value   |
|                          |                 |  unit of the commodity |
|                          |                 |  at time $T$           |

## 

\begin{center}
 \includegraphics[width=9cm,height=6cm]{images/table6-1.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm,height=4cm]{images/figure6-1.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm,height=4cm]{images/figure6-2.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm, height=6cm]{images/table6-2.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm,height=4cm]{images/figure6-3.png}
\end{center}


##

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-4.png}
\end{center}

## 

\begin{center}
 \includegraphics[width=9cm, height=6cm]{images/table6-6.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-5.png}
\end{center}


##

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-7.png}
\end{center}


##

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-8.png}
\end{center}


##

\begin{center}
 \includegraphics[width=9cm,height=4cm]{images/figure6-9.png}
\end{center}


##

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-10.png}
\end{center}


## 

\begin{center}
 \includegraphics[width=9cm, height=4cm]{images/figure6-11.png}
\end{center}


