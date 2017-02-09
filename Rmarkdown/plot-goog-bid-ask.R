library(xts)

raw <- read.csv("goog-bid-ask.csv", sep=",", header=T)
raw$SPRD <- raw$OFR - raw$BID
tmp <- raw[raw$BID > 0 & raw$OFR > 0, ]
tmp <- tmp[tmp$SPRD < 10, ]
mts <- merge(as.zoo(tmp$OFR), as.zoo(tmp$BID))
names(mts) <- c("ask", "bid")

plot(mts, ylim=c(1000, 1050), plot.type="single", xlab="5 Minutes of Trading", ylab="Bid/Ask Prices", col=c("goldenrod", "darkgreen"))
