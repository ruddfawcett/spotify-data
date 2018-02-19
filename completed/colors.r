primaries <- c('#00b140', '#ff6900', '#e4002b', '#0689d8', '#c800a1')
grays <- c('#242424', '#646464', '#cfcfcf', '#f0f0f0')

heat_scale <- scale_colour_gradientn(colours = c(primaries[5], primaries[4], primaries[1], primaries[2], primaries[3]), limits=c(1, 87))

primary_scale_colour <- function() {
  scale_colour_manual(values = primaries)
}

gray_scale_colour <- function() {
  scale_colour_manual(values = grays)
}
