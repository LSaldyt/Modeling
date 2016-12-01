
boxPlot <- function(data)
{
    boxplot(data,
            las   = 2, 
            names = c('Min + Max', 
                      '2 * Mean', 
                      '2 * Median', 
                      'First Quartile + Third Quartile - Min', 
                      'Max - Min', 
                      '(2 * Median) - Min',
                      'Max + (Standard Deviation / 2) - Min'),
                col=(c("#ff9900")))
}

plotConfidence <- function(filename)
{
    estimates <- read.csv(filename, header=FALSE)
    t(estimates)
    print(estimates)
    boxPlot(estimates)
}

png()
plotConfidence("estimates.csv")
plotConfidence("estimates_shifted.csv")
plotConfidence("estimates_skewed.csv")

