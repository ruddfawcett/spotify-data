library(ggplot2)
library(ggthemes)
library(waffle)

# pdf('peak_distribution.pdf',width=12.5417,height=4.9722)

data = read.csv(file='cleaned_data.csv', sep=',', header = TRUE)

oldpar <- par(mar=rep(0,4))
plot <- ggplot(data, aes(x=mode)) +
        geom_histogram(color='white', fill='blue', binwidth=1) +
        # geom_bar(color='white', fill='blue') +
        # scale_y_continuous(breaks = seq(0, 1000, by = 100)) +
        theme_wsj(color='white') +
        guides(alpha = FALSE) + theme(plot.margin=grid::unit(c(0,0,0,0), "mm"))

par(oldpar)
print(plot)
par(oldpar)
dev.off()
