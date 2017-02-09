% Time Series Models
% Tyler J. Brough
% \today{}

## Chapter 11: Time Series Models

These notes are based on Chapter 11 of the book [Mathematics & Statistics for Financial Risk
Management](https://goo.gl/BVnAFe) by Michael Miller.

\vspace{5mm}
___Time Series___: an equation or set of equations describing how a random variable or variables evolve(s)
over time.

\vspace{5mm}
_NB_: Could also refer to the observed data sample from such a random variable. 


## Random Walk

One of the conceptually simplest time series models is the so-called random walk.

\begin{eqnarray*}
 x_{t} &=& x_{t-1} + u_{t} \\
 E(u_{t}) &=& 0 \\
 E(u_{t}^{2}) &=&  \sigma^{2} \\
 E(u_{s} u_{t}) &=&  0 \quad \forall \quad s \ne t
\end{eqnarray*}


## 

$x$ is equal to its value in the previous period, plus a random disturbance, $u_{t}$

\vspace{5mm}
$u_{t}$ is zero-mean with a constant variance

- It is implied that $u$'s from different periods will be uncorrelated

- $x_{t-1}$ is referred to as lag of $x_{t}$

\vspace{5mm}
We can also think in terms of changes in $x$

\begin{equation*}
 \Delta x_{t} = x_{t} - x_{t-1} = u_{t}
\end{equation*}


_NB_: $\Delta x_{t}$ has all the properties of the disturbance


##

Evolution over time:

\begin{eqnarray*}
 x_{t} &=& x_{t-1} + u_{t} \\
 x_{t-1} &=& x_{t-2} + u_{t-1} \\
 \vdots \\
 x_{t-i} &=& x_{t-i-1} + u_{t-i}
\end{eqnarray*}

\vspace{5mm}
By recursive substitution, we can see that

\begin{equation*}
 x_{t} = x_{t-1} + u_{t} = x_{t-2} + u_{t-1} + u_{t} = x_{0} + \sum\limits_{i=1}^{t} u_{i}
\end{equation*}


\vspace{5mm}
_NB_: $x_{t}$ is the initial value plus the accumulation of all the disturbances over time (random innovations)


## 

We can now calculate the conditional mean and variance:

\begin{eqnarray*}
 E(x_{t} | x_{0}) &=& x_{0} \\
 Var(x_{t} | x_{0}) &=& t \sigma^{2} 
\end{eqnarray*}


\vspace{5mm}
_NB_: the variance is proportional to time (it is explosive). Volatility is proportional to the square root of time.


##

For a random walk our best guess to predict the next observed value is simply the current value. But the probability of
finding it near the current value becomes increasingly small.

\vspace{5mm}
For all practical purposes this makes a random walk unpredictable (unforecastable) or totally random.

\vspace{5mm}
_NB_: this is a good starting point for modeling prices that are informationally efficient.

\vspace{5mm}
See the paper [Proof that Properly Anticipated Prices Fluctuate Randomly]() by Paul Samuelson.

\vspace{5mm}
Though there are some problems:

1. For equities we expect a positive return over time to compensate risk-averse investors for holding the investment.
2. Prices (typically) cannot be negative 


## The Drift-Diffusion Model

We can add a constant term as follows:

\begin{equation*}
 p_{t} = \alpha + p_{t-1} + u_{t}
\end{equation*}

\vspace{5mm}
The random variable ($p$) is now a function of:

1. The previous value $p_{t-1}$
2. The constant term $\alpha$ 
3. The disturbance term $u_{t}$


##

Just as before:

- Variance of $u_{t}$ is constant over time
- $u$'s are uncorrelated

\vspace{5mm}
If $p{t}$ is the log price, then

\begin{equation*}
 r_{t} = \Delta p_{t} = \alpha + u_{t}
\end{equation*}

\vspace{5mm}
- $\alpha$ often referred to as the drift term
- $u_{t}$  often referred to as the diffusion term

\vspace{5mm}
_NB_: in physics this process is often used to describe the motion of particles (also known as Brownian motion)


## 

When equity returns follow a drift-diffusion process we say that equity markets are perfectly efficient

- the limiting ase of Hayek's information aggregation process
- a simple way to parameterize the Efficient Markets Hypothesis (EMH) from received theory
- mathematically, expected conditional and unconditional returns are equal

\begin{equation*}
 E[r_{t} | r_{t-1} ] = E[r_{t}] = \alpha
\end{equation*}

- If this were not true - if there were some information in the past that was helpful for forecasting tomorrow's return
  then speculators would step in and push prices towards this result!


##

We can still do recursive substitution 

\begin{equation*}
 p_{t} = 2 \alpha + p_{t-2} + u_{t} + u_{t-1} = t \alpha + p_{0} + \sum\limits_{i=1}^{t} u_{i}
\end{equation*}

\vspace{5mm}
And as before:

- $E[p_{t} | p_{0}] = p_{0} + t \alpha$ 
- $Var[p_{t} | p_{0}] = t \sigma^{2}$


\vspace{5mm}
_NB_: variance is still proportional to time, however the mean is no longer constant but rather now moves around at rate
$\alpha$. Thus it is called the _drift_ term. 


## Autoregression

Now modify the model by multiplying the lagged term by a constant:

\begin{equation*}
 r_{t} = \alpha + \rho r_{t-1} + u_{t}
\end{equation*}

\vspace{5mm}

- both $\alpha$ and $\rho$ are constants
- depending on the value of $\rho$, the model's behavior can vary greatly
- when $\left| \rho \right| < 1$ it will produce a stable time series
- when $\rho = 1$ we get the random walk as a special case
- when $\left| \rho \right| > 1$ the system is explosive in a way that is not particularly interesting for financial
  time series


##

This is known as an _autoregressive_ model ($AR(1)$ above)

\vspace{5mm}

We can write down the $AR(p)$ generalization:

\begin{equation*}
 r_{t} = \alpha + \rho_{1} r_{t-1} + \rho_{2} r_{t-2} + \ldots + \rho_{p} r_{t-p} + u_{t}
\end{equation*}


\vspace{5mm}
As before, do recursive substitution

\begin{equation*}
 r_{t} = \alpha \sum\limits_{i=0}^{p} \rho^{i} + \rho^{p} r_{t-p} + \sum\limits_{i=0}^{p-1} \rho^{i}
\end{equation*}


##

The condition mean and variance become:

\begin{eqnarray*}
 E[r_{t} | r_{t-p}]   &=& \frac{1 - \rho^{p}}{1 - \rho} \alpha + \rho^{p} r_{t-p} \\
 Var[r_{t} | r_{t-p}] &=& \frac{1 - \rho^{2p}}{1 - \rho^{2}} \sigma^{2}
\end{eqnarray*}


\vspace{5mm}

_NB_: for $\left| \rho \right| > 1$ the variance grows exponentially.

\vspace{5mm}

For values $\left| \rho \right| < 1$ the process is stable

\vspace{5mm}

If we extend back in time, and let $p$ approach infinity, $\rho^{p}$ becomes increasingly small causing $\rho^{p}
r_{t-p}$ to approach zero

\begin{equation*}
 r_{t} = \frac{1}{1-\rho} \alpha + \sum\limits_{i=0}^{\infty} \rho^{i} u_{t-i}
\end{equation*}


## 

Using some results from geometric series, we can write the mean and variance

\begin{eqnarray*}
 E[r_{t}]   &=& \frac{1}{1 - \rho} \alpha \\
 Var[r_{t}] &=& \frac{1}{1 - \rho} \sigma^{2}
\end{eqnarray*}

\vspace{5mm}
For values of $\left| \rho \right|$ less than one, as $n$ approaches infinity, the initial state of the system ceases to matter. The mean and variance are only a function of the constants.


## Stationarity

We say that a random variable $X$ is stationary if for all $t$ and $n$:

\vspace{5mm}
\begin{eqnarray*}
 E[x_{t}] &=& \mu \quad \mbox{and} \quad \left| \mu \right| < \infty \\
 Var[x_{t}] &=& \sigma^{2} \quad \mbox{and} \quad \left| \sigma^{2} \right| < \infty \\
 Cov[x_{t},x_{t-n}] &=& \sigma_{t,t-n}
\end{eqnarray*}

\vspace{2.5mm}
where $\mu$, $\sigma^{2}$, and $\sigma_{t,t-n}$ are constants.


## Moving Average

Besides $AR(p)$ models, the other major class of time series models is moving average models. An $MA(q)$ sereis takes the form:

\begin{equation*}
 x_{t} = u_{t} + \theta_{1} u_{t-1} + \cdots + \theta_{q} u_{t-q}
\end{equation*}

\vspace{5mm}
We can combine the two to form the $ARMA(p,q)$ model as well:

\begin{equation*}
 x_{t} = \rho_{1} x_{t-1} + \rho_{2} x_{t-2} + \cdots + \rho_{p} x_{t-p} + u_{t} + \theta_{1} u_{t-1} + \cdots + \theta_{q} u_{t-q}
\end{equation*}




