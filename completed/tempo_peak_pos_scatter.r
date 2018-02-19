library(ggplot2)
library(ggthemes)

source('colors.r')

# pdf('peak_distribution.pdf',width=12.5417,height=4.9722)

data = read.csv(file='../cleaned_data.csv', sep=',', header = TRUE)
reset <- par(mar=rep(0,4))

data_trimmed <- data[data$streak < 40,]
data_consistent <- data[data$streak >= 40,]

plot <- ggplot() +
        geom_point(data = data_trimmed, aes(x=tempo, y=peak_pos, color=streak), alpha=0.5, size=2, position = 'jitter') +
        geom_point(data = data_consistent, aes(x=tempo, y=peak_pos, color=streak), alpha=0.5, size=2, position = 'jitter') +
        geom_rangeframe() +
        theme_wsj(color='white') +
        guides(alpha = FALSE, size = FALSE, color = FALSE) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm')) +
        heat_scale

par(reset)
print(plot)
par(reset)
# dev.off()
