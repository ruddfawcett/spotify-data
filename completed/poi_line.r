library(ggplot2)
library(ggthemes)

source('colors.r')

pdf('../pdfs/valence_poi_line.pdf',width=4.7239,height=3.2927)

poi = 'valence'

data_by_x = read.csv(file=paste0('../avgs_toppers/avg_',poi,'.csv'), sep=',', header = TRUE)
data_by_x$category <- rep('top_x', nrow(data_by_x))
data_by_x_left <- subset(data_by_x, year < 1979)
data_by_x_right <- subset(data_by_x, year > 1979)

data_remainder = read.csv(file=paste0('../avgs/avg_',poi,'.csv'), sep=',', header = TRUE)
data_remainder$category <- rep('remainder', nrow(data_remainder))
data_remainder_left <- subset(data_remainder, year < 1979)
data_remainder_right <- subset(data_remainder, year > 1979)

data <- rbind(data_by_x, data_remainder)

oldpar <- par(mar=rep(0,4))
plot <- ggplot() +
        geom_line(data=data_by_x_left, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_line(data=data_by_x_right, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_line(data=data_remainder_left, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_line(data=data_remainder_right, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_line(data=data_remainder_left, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_line(data=data_remainder_right, size=1, aes_string(x='year',y=paste0('avg_',poi), color='category')) +
        geom_vline(xintercept = 1979, size = 0.5, color=grays[2]) +
        geom_vline(xintercept = 2008, size = 0.5, color=grays[2]) +
        scale_x_continuous(breaks = seq(1968, 2017, by = 10)) +
        # scale_y_continuous(breaks = seq(0, 1, by = 0.1)) +
        theme_wsj(color='white') +
        scale_colour_manual(values = c('#fcde05', grays[3]  )) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm'), legend.position='none')

par(reset)
print(plot)
par(reset)
dev.off()
