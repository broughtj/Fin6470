% Chapter 3 - Hedging Strategies Using Futures
% Tyler J. Brough
% \today{}

# Introduction

## Introduction

- One kind of participant in futures markets is the **hedger**.
- Hedgers use futures markets to transfer risk.
- A **perfect hedge** entirely illiminates the risk faced by the hedger. These are very rare!
- We will want to think carefully about how to measure the performance of a hedge.
- In this chapter we restrict our attention to **hedge-and-forget** (or simply static) hedging strategies.
- At first, we will ignore daily settlement - that is, we will treat futures like forward contracts.


# Section 3.1 - Basic Principles

## Basic Principles

Consider the following scenario:

- A company knows that over the next three months:
	* It will gain $\$10,000$ for every $\$0.01$ increase in the price of a commodity.
	* It will lose $\$10,000$ for every $\$0.01$ decrease in the price of a commodity.
- To hedge the company should take a short futures position.
	* For every $0.01$ increase in the price of the commodity:
		+ The futures position will lead to a loss of $\$10,000$
		+ But the position in the commodity will increase in value by precisely $\$10,000$ to offset the losses.
	* For every $0.01$ decrease in the price of the commodity:
		+ The futures position will lead to a gain of $\$10,000$
		+ But the position in the commodity will lose value by $\$10,000$ to offset the gains in the futures contract.

## Short Hedges

- A **short hedge** is one that involves a short futures position
- It is appropriate when one has a position in the asset (and expects to sell it in the future)
- Ex: a rancher who will take cattle to auction in October would use a short hedge to transfer cattle price risk


## Long Hedges

- A **long hedge** is one that involves a long futures position
- Long hedges are appropriate when the company knows it will be purchasing an asset at some time in the future
- Ex: An airline must purchase jet fuel and so uses a long futures position to lock-in the purchase price


# Section 3.2 - Arguments For & Against Hedging

## Arguments in Favor of Hedging

- Companies should focus on the main business they are in and take steps to minimize risks arising from interest rates, exchange rates, and other market variables


## Arguments against Hedging

- Shareholders are usually well diversified and can make their own hedging decisions
- It may increase risk to hedge when competitors do not
- Explaining a situation where there is a loss on the hedge and a gain on the underlying can be difficult
	* *Question:* Could the use of options change the scenario?


# Section 3.3 - Basis Risk

## Are Perfect Hedges Too Good To Be True?

In practice, hedging is not so straightforward. For at least these reasons:

1. The asset that requires hedging differs from the one underlying the futures contract
2. Uncertainty over the date when the asset will be purchased or sold
3. The hedge may require the futures contract to be closed prior to the delivery date


## Basis Risk

The **basis** is defined as:

$$\mbox{Basis} = \mbox{Spot price} - \mbox{Futures price}$$

- If the asset to be hedged and the underlying asset are identical then basis should be zero at expiration
- But prior to expiration basis can be positive or negative


## Basis Continued

- Basis is random over time
	* An increase in basis is called a **strengthening of the basis**
	* A decrease in basis is called a **weakening of the basis**


\begin{center}
  \includegraphics[width=8cm,height=5cm]{OFOD9_03-01.eps}
\end{center}


## Some Notation

To examine the nature of basis risk we will use the following notation:

- $S_{1}$ : Spot price at time $t_{1}$
- $S_{2}$ : Spot price at time $t_{2}$
- $F_{1}$ : Futures price at time $t_{1}$
- $F_{2}$ : Futures price at time $t_{2}$
- $b_{1}$ : Basis at time $t_{1}$, that is $b_{1} = S_{1} - F_{1}$
- $b_{2}$ : Basis at time $t_{2}$, that is $b_{2} = S_{2} - F_{2}$


## An Example


## Contract Size

A key factor that affects the basis risk is the choice of contract, which has two components:

1. The choice of the asset underlying the futures contract
	* It is rare that the underlying asset is identical to the asset being hedged
	* When it is not careful analysis is required to choose the contract
2. The choice of the delivery months
	* It is rare that the hedging timeline lines up with the delivery period
	* A rule of thumb is to choose a delivery month that is as close as possible, but later than, the hedging expiration


# Section 3.4 - Cross Hedging

## Cross Hedging

- **Cross hedging** is when the asset to be hedged differs from the underlying asset
- Ex: The airline which wishes to hedge jet fuel must choose a futures contract with a related underlying asset such as heating oil
- The **hedge ratio** is the ratio of the size of the position taken in futures to the size of the exposure
	* If the asset to be hedged is identical to the underlying asset this is often $1$
	* When cross hedging this often the value that minimizes the variance of the hedged position


## Calculating the Minimum Variance Hedge Ratio

The minimum variance hedge ratio depends on the relationship between changes in the spot price and changes in the futures price.

Define:

- $\Delta S$ : the change in spot price $S$ during the life of the hedge
- $\Delta F$ : the change in futures price $F$ during the life of the hedge

We will denote the minimum variance hedge as $h^{\ast}$. The formula for $h^{\ast}$ is:

$$h^{\ast} = \rho \frac{\sigma_{S}}{\sigma_{F}}$$

Where:

- $\sigma_{S}$ is the standard deviation of $\Delta S$
- $\sigma_{F}$ is the standard deviation of $\Delta F$
- $\rho$ is the correlation of the two

## The Optimal Number of Contracts

To calculate the number of contracts that should be used in hedging, we define the following:

- $Q_{A}$    : Size of position being hedged (units)
- $Q_{F}$    : Size of one futures contract (units)
- $N^{\ast}$ : Optimal number of futures contracts for hedging

The futures contracts should be on $h^{\ast} Q_{A}$  units of the asset.

The number of contracts is given by:

$$N^{\ast} = \frac{h^{\ast} Q_{A}}{Q_{F}}$$


## Tailing the Hedge

- So far we have been treating futures as though they were forward contracts.
- When we actually use futures it's like there are a series of daily hedges.
- To reflect this we usually calculate the correlation between daily futures and spot prices

To do this we denote:

- $\hat{\rho}$       : the daily correlation between spot and futures prices
- $\hat{\sigma_{S}}$ : the daily standard deviation of the spot price
- $\hat{\sigma_{F}}$ : the daily standard deviation of the futures price

## Tailing the Hedge Continued

- If $S$ and $F$ are the current spot and futures prices then the standard deviations of one-day prices changes are:
	* $S\hat{\sigma_{S}}$
	* $F\hat{\sigma_{F}}$
- The one-day hedge ratio then becomes:

$$\hat{\rho}\frac{S\hat{\sigma_{S}}}{F\hat{\sigma_{F}}}$$


## Tailing the Hedge Continued

The number of contracts needed to hedge over the next day is:

$$N^{\ast} = \hat{\rho} \frac{S\hat{\sigma_{S}} Q_{A}}{F\hat{\sigma_{F}} Q_{F}}$$

Using this result is called *tailing the hedge*. We can write this as:

$$N^{\ast} = \hat{h}\frac{V_{A}}{V_{F}}$$

Where:

- $V_{A} = S Q_{A}$ : is the dollar value of the position being hedged
- $V_{F} = F Q_{F}$ : is the dollar of one futures contract
- $\hat{h}$ is defined similarly to $h^{\ast}$ as:

$$\hat{h} = \hat{\rho}\frac{\hat{\sigma_{S}}}{\hat{\sigma_{F}}}$$


## Tailing the Hedge Continued

- It can be shown that a forward contract can be replicated by a dynamic trading strategy involving futures.
- The initial exposure from purchasing a forward contract with maturity at date $T$ is equivalent to the
exposure of $P(0,T) = e^{rT}$ futures where $r$ is the risk-free interest rate.
- The adjustment of the hedge ratio from $1$ to the lower value $P(0,T)$ is the tailed position.
- Tailing the hedge makes more of a difference the further into the future the maturity date $T$ is.

## Tailing the Hedge Continued

In theory this suggests that we should change the futures position every day to reflect the latest
values of $V_{A}$ and $V_{F}$. In practice, day-to-day changes in the hedge are very small and
usually ignored.

Later we will explore dynamic hedging strategies. Is it possible to beat a static hedge?


# Section 3.5 - Stock Index Futures

## Stock Index Futures

- We can use stock index futures to hedge exposures to equity prices.
- A **stock index** tracks changes in the value of a hypothetical portfolio of stocks.
- Weights for particular stocks in the portfolio equal the proportion in the hypothetical index.


## Stock Indices

**Table 3.3** shows futures prices for contracts on $3$ different stock Indices
as of May 14, 2013.

\begin{center}
  \includegraphics[width=12cm,height=18cm]{Table3-3.pdf}
\end{center}

## Stock Indices Continued

- The *Dow Jones Industrial Average* is based on a portfolio consisting of $30$ blue-chip stocks.
	* Weights are proportional to prices
	* CME trades two contracts based on the index:
		+ one that is $\$10$ times the index
		+ one that is $\$5$ time the index (the Mini)
- The *Standard and Poor's 500 Index* (SP500) is based on a portfolio of $500$
	* $400$ Industrials
	* $40$ utilities
	* $20$ transportation Companies
	* $40$ financial institutions
	* Two contracts trade on the SP500:
		+ one that is $\$250$ times the index
		+ one that is $\$50$ times the index (the Mini)

## Stock Indices Continued

- The *Nasdaq-100* is based on $100$ stocks using the NASDAQ
	* Two contracts traded:
		+ one that is $\$100$ times the index
		+ one that is $\$20$ times the index (the Mini)

As mentioned in chapter 2, futures contracts on stock indices are cash settled.

- Contracts are marked-to-market either on the opening or closing price of the index on the last trading day
	* Ex: the SP500 contracts are closed out at the opening price of the index on $3^{rd}$
	  Friday of the delivery month.

## Hedging and Equity Portfolio

Stock index futures can be used to hedge well-diversified equity portfolios that tracks
one of the indices.

Define:

- $V_{A}$ : the current value of the portfolios
- $V_{F}$ : the current value of one futures contract (the futures price times the contract size)


## Hedging and Equity Portfolio Continued

- If we assume the hedge ratio to be $1.0$ then the number of futures contracts to
be shorted is:

$$N^{\ast} = \frac{V_{A}}{V_{F}}$$

Suppose that a portfolio valued at $\$5,050,000$ tracks the SP500. Also:

- The index is $1,010$ and each futures is on $\$250$ times the index
- $V_{A} = 5,050,000$
- $V_{F} = 250 \times 1010 = 252,500$
- This means we need $20$ futures contracts (short) to hedge the exposure


## Hedging and Equity Portfolio Using the CAPM

- When the portfolio does not track the index we can use the CAPM (see appendix to chapter 3).
- The key parameter from the CAPM is the $\beta$:
	* When $\beta = 1.0$ the portfolio tracks the index
	* When $\beta = 2.0$ the return on the portfolio tends to be twice the index
	* When $\beta = 0.5$ the return on the portfolio tends to be half the index
- A portfolio with $\beta = 2.0$ is twice as sensitive to movements in the index as a portfolio with $\beta = 1.0$
	* So we need to use twice as many futures contracts, etc


## Hedging and Equity Portfolio Using the CAPM

Using the CAPM $\beta$ the new hedge ratio becomes:

$$N^{\ast} = \beta \frac{V_{A}}{V_{F}}$$

- This assumes that $\hat{h} = \beta$, unsurprisingly


## Hedging and Equity Portfolio Using the CAPM

Assume the following:

- The value of the SP500 index is $= 1,000$
- The nearby SP500 futures price is $= 1,010$
- The value of the portfolio $=\$5,050,000$
- The risk-free rate is $r = 4\%$ per annum
- The dividend yield on the index is $= 1\%$ per annum
- The portfolio beta is $\beta = 1.5$
- One contract is for $\$250$ times the index


## Hedging and Equity Portfolio Using the CAPM

- $V_{F} = 252,500$ as before

Using the CAPM we get the following optimal hedge ratio:

$$1.5 \times \frac{5,050,000}{252,500} = 30$$

Suppose the index turns out to be $900$ in $3$ months, and the futures price is
$902$. The gain from the short futures position is then:

$$30 \times (1010 - 902) \times 250 = \$810,000$$


## Hedging and Equity Portfolio Using the CAPM

- The loss on the index is $10\%$
- The index pays a dividend of $0.25\%$ per $3$ months
- Thus an investor would have earned a return of $-9.75\%$

By the CAPM we see that

$$1.0 + [1.5 \times (-9.75 - 1.0)] = -15.125$$

## Hedging and Equity Portfolio Using the CAPM

The expected value of the portfolio at the end of $3$ months is:

$$\$5,050,000 \times (1 - 0.15125) = \$4,286,187$$

The expected value of the hedged position is then:

$$\$4,286,187 + \$810,000 = \$5,096,187$$


## Changing the beta of the Portfolio

In this example above the $\beta$ of the portfolio was changed to $\beta = 0.0$. In general,
to change from a portfolio beta of $\beta$ to $\beta^{\ast}$, where $\beta > \beta^{ast}$,
a short position in:

$$(\beta - \beta^{\ast}) \frac{V_{A}}{V_{Q}}$$

is required. When $\beta^{\ast} > \beta$, a long position is required:

$$(\beta^{\ast} - \beta) \frac{V_{A}}{V_{Q}}$$


# Section 3.6 - Stack & Roll

## The Stack and Roll

- Sometimes the expiration date of a hedge is later than the delivery dates of available futures contracts
- The hedger must then *roll the hedge* forward by closing out the original position and taking a new one
- Hedges can be rolled forward many times in a procedure known as the **stack and roll**


## The Stack and Roll

- Time $t_{1}$   : Short futurec contract 1
- Time $t_{2}$   : Close out futures position 1, short futures contract 2
- Time $t_{3}$   : Close out futures position 2, short futures contract 3
- Time $t_{n-1}$ : Close out futures position $n-1$, short futures contract $n$
- Time $t_{n}$   : Close out futures contract $n$
