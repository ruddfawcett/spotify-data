library(ggplot2)
library(ggthemes)

pdf('streak_year.pdf',width=12.5417,height=4.9722)

data = read.csv(file='year_avg_streak.csv', sep=',', header = TRUE)

reset <- par(mar=rep(0,4))

plot <- ggplot(new_data, aes(x = year, y = avg_streak)) +
        geom_line(size = 1, color='#251AED') +
        scale_x_continuous(breaks = seq(1967, 2017, by = 5)) +
        scale_y_continuous(breaks = seq(0, 20, by = 1)) +
        theme_wsj(color='white') +
        guides(alpha = FALSE) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm'))

par(reset)
print(plot)
par(reset)
dev.off()
