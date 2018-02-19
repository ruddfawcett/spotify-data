# library
library(ggplot2)

data = read.csv(file='cleaned_data.csv', sep=',', header = TRUE)
var <- data$streak

plot <- ggplot(data, aes(factor(1), streak)) +
  coord_flip() +
  geom_boxplot()
  # geom_density(binwidth = 1)

print(plot)
