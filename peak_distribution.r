library(ggplot2)
library(ggthemes)

# pdf('peak_distribution.pdf',width=12.5417,height=4.9722)

data = read.csv(file='debut_year_matched.csv', sep=',', header = TRUE)
new_data <- subset(data, debut_year >= 1967 & debut_year <= 2017)
oldpar <- par(mar=rep(0,4))
plot <- ggplot(new_data, aes(x=peak_pos)) +
        geom_histogram(color='white', fill='#ed1d65', binwidth=1) +
        scale_y_continuous(breaks = seq(0, 1000, by = 100)) +
        theme_wsj(color='white') +
        guides(alpha = FALSE) + theme(plot.margin=grid::unit(c(0,0,0,0), "mm"))

# data

par(oldpar)
print(plot)
par(oldpar)
# dev.off()
