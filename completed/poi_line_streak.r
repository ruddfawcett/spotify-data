library(ggplot2)
library(ggthemes)

source('colors.r')

pdf('../pdfs/poi_line_streak.pdf',width=7.46,height=3.7994)

poi = 'streak'

data_by_x = read.csv(file=paste0('../avgs_toppers/avg_',poi,'.csv'), sep=',', header = TRUE)
data_by_x$category <- rep('top_x',nrow(data_by_x))

data_remainder = read.csv(file=paste0('../avgs/avg_',poi,'.csv'), sep=',', header = TRUE)
data_remainder$category <- rep('remainder',nrow(data_remainder))

data <- rbind(data_by_x, data_remainder)

reset <- par(mar=rep(0,4))
plot <- ggplot(data, aes_string(x='year',y=paste0('avg_',poi),fill='category', color='category'), show.legend=FALSE) +
        geom_line(size=1) +
        scale_x_continuous(breaks = seq(1968, 2017, by = 10)) +
        scale_y_continuous(breaks = seq(0, 40, by = 5)) +
        theme_wsj(color='white') +
        geom_vline(xintercept = 2008, size = 0.5, color=grays[2]) +
        scale_colour_manual(values = c(grays[3], '#fcde05')) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm'), legend.position='none')

par(reset)
print(plot)
par(reset)
dev.off()
