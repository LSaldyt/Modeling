options(width=60, keep.source=TRUE, prompt=" ", continue=" ")
set.seed(76543); # recompile will have same random numbers


###################################################
### code chunk number 4: ex (eval = FALSE)
###################################################
#An example with 100 Confidence Intervals (CIs).
#Consider drawing a sample of 25 observations from a normally distributed population with mean 10 and sd 2. Calculate the 95% t-CI. Now do that 100 times. The plot belows reflects the variability of that process. We expect 95 of the 100 CIs to contain the true population mean of 10, that is, on average 5 times out of 100 we draw the incorrect inference that the population mean is in an interval when it does not contain the true value of 10.
library(TeachingDemos)
## # look at examples at bottom of the help page
## ?clt.examp
ci.examp(mean.sim = 10, sd = 2, n = 25
                  , reps = 100, conf.level = 0.95, method = "t")


###################################################
### code chunk number 5: 02_tdist_normal
###################################################
#With higher degrees of freedom, the t distribution gets closer to the normal distribution, as illustrated by this example:
x <- seq(-8, 8, length = 1000)
par(mfrow=c(1,1))
plot(x, dnorm(x), type = "l", lwd = 2, col = "red"
          , main = "Normal (red) vs t-dist with df=1, 2, 6, 12, 30, 100")
points(x, dt(x,  1), type = "l")
points(x, dt(x,  2), type = "l")
points(x, dt(x,  6), type = "l")
points(x, dt(x, 12), type = "l")
points(x, dt(x, 30), type = "l")
points(x, dt(x,100), type = "l")


###################################################
### code chunk number 8: ex
###################################################
#Example data
#Page 13 of ADA1_02_OneSample.pdf
# enter data as a vector
#Example: Age at First Transplant (Revisited) The ages (in years) at first transplant for a sample of 11 heart transplant patients are as follows: 54, 42, 51, 54, 49, 56, 33, 58, 54, 64, 49.
age <- c(54, 42, 51, 54, 49, 56, 33, 58, 54, 64, 49)


###################################################
### code chunk number 9: 02_age
###################################################
#Let's look at the example data.
par(mfrow=c(2,1))
# Histogram overlaid with kernel density curve
hist(age, freq = FALSE, breaks = 6)
points(density(age), type = "l")
rug(age)

# violin plot
library(vioplot)
vioplot(age, horizontal=TRUE, col="gray")


###################################################
### code chunk number 10: ex
###################################################
#Calculating the critical value from a t distribution:
# t.crit
#qt(desired confidence level, degrees of freedom)
#http://stackoverflow.com/questions/11526041/critical-t-values-in-r
#The graph on page 11 of ADA1_02_OneSample.pdf may help clarify the following.
#95% confidence level for two sided test:
qt(1 - 0.05/2, df = length(age) - 1)
#95% confidence level for one sided test:
qt(1 - 0.05, df = length(age) - 1)
#Note that these are the same:
abs(qt(0.05, df = length(age) - 1))
qt(0.95, df = length(age) - 1)
