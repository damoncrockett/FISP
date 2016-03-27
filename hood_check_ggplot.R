library(ggplot2)
df = read.csv("streetview_parcel_CPA.csv")

basemap = ggplot(subset(df,df$lon< -116.9),aes(lon,lat)) + geom_point(color='white',size=1)
basemap

rev(sort(table(df$CPA)))

tmp = subset(df,df$CPA=="RANCHO ENCANTADA")
basemap + geom_point(data=tmp,aes(lon,lat),color="blue")
