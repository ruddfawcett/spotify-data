library(ggplot2)
library(ggthemes)
library(magrittr)
library(dplyr)

source('colors.r')

pdf('../pdfs/key_signature_histogram.pdf',width=7.46,height=3.1256)

data = read.csv(file='../cleaned_data.csv', sep=',', header = TRUE)

reset <- par(mar=rep(0, 4))

# data_trimmed <- data[data$key %in% c('0', '2', '4', '5', '7', '9', '11'),]
# data_consistent <- data[data$key %in% c('1', '3', '6', '8', '10'),]
data_trimmed <- subset(data, debut_year <= 2007)
data_trimmed$category <- rep('old',nrow(data_trimmed))
data_consistent <- subset(data, debut_year > 2008)
data_consistent$category <- rep('new',nrow(data_consistent))

data <- rbind(data_trimmed, data_consistent)

plot_data <- data %>%
  group_by(category, key) %>%
  tally %>%
  mutate(percent = n/sum(n))

plot <- ggplot(plot_data, aes(x=key, y=percent, group=category)) +
# , fill = '#fcde05'
        geom_bar(stat='identity', aes(fill=category), position='dodge', color='white') +
        # geom_bar(data = data, aes(y=..count../sum(..count..), x=key, group=category, fill=category), position = "dodge", color='white') +
        # geom_text(position = "dodge", stat = "identity", aes(label = ..count..), vjust = 2, color='black') +
        scale_x_discrete(limits=0:11, labels= c('C', 'C, D', 'D', 'D, E', 'E', 'F', 'F, G', 'G', 'G, A', 'A', 'A, B', 'B')) +
        scale_y_continuous(labels=scales::percent_format()) +
        theme_wsj(color='white') +
        scale_fill_manual(values = c('#fcde05', grays[3])) +
        guides(alpha = FALSE, fill = FALSE) +
        theme(plot.margin=grid::unit(c(0,0,0,0), 'mm'))

par(reset)
print(plot)
par(reset)
dev.off()
