
boxPlot <- function(filename)
{
    data <- read.csv(filename, header=FALSE)
    boxplot(data,
            las   = 2, 
            names = c("Pre-Infection", "Post-Infection"),
            ylab  = "Raid size",
            col   = (c("#ff9900")))
}

png()
boxPlot("paired_data.csv")
