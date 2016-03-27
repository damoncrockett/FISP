df = read.csv("sd_2013.csv")
library(ggmap)
center_sd = c(lon=-117.1625, lat=32.7150)
sd_map = get_map(location = center_sd, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")


ggmap(sd_map) + geom_point(data = df[df$CPA=="OTAY MESA-NESTOR",], aes(x = lon, y = lat),size = 1,color = "blue")

ggplot(df,aes(lon,lat)) + geom_point()

# NOTE: Ocean Beach polygon is corrupted!!!
