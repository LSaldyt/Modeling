
jitterPlot <- function(filename)
{
    data <- read.csv(filename, header=FALSE)
    pre  <- data[,1] # First column
    post <- data[,2] # Second column

    pre_labels  <- as.list(rep(1, length(pre)))  # [1 for i in len(pre)]
    post_labels <- as.list(rep(2, length(post))) # [2 for i in len(post)]
    #print(pre_labels)
    #print(post_labels)

    # Concatenate pre and post for both data and labels
    x <- c(pre, post)
    y <- c(pre_labels, post_labels)
    print(x)
    print(y)

    plot(y ~ x, pch = 15)
}

png()
jitterPlot("paired_data.csv")
