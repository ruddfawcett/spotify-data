library(ggplot2)
library(ggthemes)
library(waffle)

source('colors.r')

pdf('../pdfs/modality_waffle_1968-2007.pdf',width=4.7778,height=1.256)

data = read.csv(file='../cleaned_data.csv', sep=',', header = TRUE)
reset <- par(mar=rep(0,4))

info <- c(`Major`=71, `Minor`=29)
# info <- c(`Major`=71, `Minor`=29)
modality <- waffle(info, rows=5, size=0.5, legend_pos='none', colors=c('#fcde05', grays[3]))

par(reset)
print(modality)
par(reset)
dev.off()
