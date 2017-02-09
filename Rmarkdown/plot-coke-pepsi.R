library(xts)
rm(list=ls())

ko.raw <- read.csv("ko-1970-2015.csv", sep=",", header=T)
pep.raw <- read.csv("pep-1970-2015.csv", sep=",", header=T)

ko.dates <- as.Date(as.character(ko.raw$date), "%Y%m%d")
pep.dates <- as.Date(as.character(pep.raw$date), "%Y%m%d")

pep <- zoo(log(pep.raw$PRC), order.by = pep.dates)
ko <- zoo(log(ko.raw$PRC), order.by = ko.dates)
mts <- merge(pep, ko)

plot(mts, plot.type = "single", col=c("darkblue", "red"), xlab="Time", ylab="Log Price", main = "Coke and Pepsi")





