library(ggplot2)
library(ggthemes)

source('colors.r')

# pdf('../pdfs/peak_pos_histogram.pdf',width=7.46,height=4.1983)

data = read.csv(file='../cleaned_data.csv', sep=',', header = TRUE)

reset <- par(mar=rep(0,4))

plot <- ggplot(data, aes(x=peak_pos)) +
        geom_histogram(data = data, aes(x=peak_pos), color='white', fill = '#fcde05', binwidth = 1) +
        theme_wsj(color='white') +
        # coord_flip() +
        scale_y_continuous(breaks = seq(0, 900, by = 200)) +
        scale_x_continuous(breaks = seq(0, 100, by = 10)) +
        guides(alpha = FALSE) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm'))

par(reset)
print(plot)
par(reset)
# dev.off()
