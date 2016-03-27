d = read.csv("SD.csv")
library(ggmap)
head(d)
ggplot(d,aes(lon,lat)) + geom_point(size=1)
