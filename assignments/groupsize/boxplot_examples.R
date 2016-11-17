
estimates <- read.csv("estimates.csv", header=FALSE)

boxplot(estimates,
        las   = 2, 
        at    = c(1,2,3,5,6,7,9,10,11),
        names = c(),
        col=(c("#ff9900", "#6699ff", "#99ff66")))

small  <- estimates[,1:3] 
medium <- estimates[,4:6]
large  <- estimates[,7:9]

