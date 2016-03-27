f = read.csv('/Users/damoncrockett/Desktop/US_HSV_modes_top60_cities_urban-areas.csv')
f = f[c("lat","lon","urban_areas","city")]

la = subset(f,f$urban_areas == "Los Angeles--Long Beach--Anaheim, CA")
nyc = subset(f,f$urban_areas == "New York--Newark, NY--NJ--CT")
chi = subset(f,f$urban_areas == "Chicago, IL--IN")
dallas = subset(f,f$urban_areas == "Dallas--Fort Worth--Arlington, TX")
dc = subset(f,f$urban_areas == "Washington, DC--VA--MD")
houston = subset(f,f$urban_areas == "Houston, TX")
sd = subset(f,f$urban_areas == "San Diego, CA")
sf = subset(f,f$urban_areas == "San Francisco--Oakland, CA")
austin = subset(f,f$urban_areas == "Austin, TX")
sa = subset(f,f$urban_areas == "San Antonio, TX")
vegas = subset(f,f$urban_areas == "Las Vegas--Henderson, NV")
phoenix = subset(f,f$urban_areas == "Phoenix--Mesa, AZ")

library(ggmap)

center_la = c(lon=-118.2500, lat=34.0500)
center_nyc = c(lon=-74.0059, lat=40.7127)
center_chi = c(lon=-87.6847, lat=41.8369)
center_dallas = c(lon=-96.7970, lat=32.7767)
center_dc = c(lon=-77.0164, lat=38.9047)
center_houston = c(lon=-95.3698, lat=29.7604)
center_sd = c(lon=-117.1625, lat=32.7150)
center_sf = c(lon=-122.4167, lat=37.7833)
center_austin = c(lon=-97.7500, lat=30.2500)
center_sa = c(lon=-98.5000, lat=29.4167)
center_vegas = c(lon=-115.1739, lat=36.1215)
center_phoenix = c(lon=-112.0667, lat=33.4500)

la_map = get_map(location = center_la, 
             source = "osm",
             zoom = 10,
             color = "bw")

nyc_map = get_map(location = center_nyc, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

chi_map = get_map(location = center_chi, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

dallas_map = get_map(location = center_dallas, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

dc_map = get_map(location = center_dc, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

houston_map = get_map(location = center_houston, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

sd_map = get_map(location = center_sd, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

sf_map = get_map(location = center_sf, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

austin_map = get_map(location = center_austin, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

sa_map = get_map(location = center_sa, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

vegas_map = get_map(location = center_vegas, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")

phoenix_map = get_map(location = center_phoenix, 
                 source = "osm",
                 zoom = 10,
                 color = "bw")



# maps

ggmap(la_map) + 
  geom_point(data = la, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(nyc_map) + 
  geom_point(data = nyc, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(chi_map) + 
  geom_point(data = chi, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(dallas_map) + 
  geom_point(data = dallas, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(dc_map) + 
  geom_point(data = dc, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(houston_map) + 
  geom_point(data = houston, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(sd_map) + 
  geom_point(data = sd, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(sf_map) + 
  geom_point(data = sf, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(austin_map) + 
  geom_point(data = austin, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(sa_map) + 
  geom_point(data = sa, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(vegas_map) + 
  geom_point(data = vegas, aes(x = lon, y = lat),
             size = 1,
             color = "blue")

ggmap(phoenix_map) + 
  geom_point(data = phoenix, aes(x = lon, y = lat),
             size = 1,
             color = "blue")




# hist

ggplot(la,aes(lon)) + geom_histogram(color="white",fill="grey50") +
  theme(panel.background = element_rect(fill = "grey50"),
        panel.grid.major = element_line(color = "grey50"),
        panel.grid.minor = element_line(color = "grey50"),
        plot.background = element_rect(fill = "grey50"),
        legend.position="none",
        axis.text = element_text(size=rel(0.7), color='white'),
        text = element_text(color='white', size = 10)) +
  labs(x='LONGITUDE',y='COUNT',title="LA")


# check

library(ggplot2)
lat_strip = subset(f,f$lat>33 & f$lat<35)
la_area = subset(lat_strip,lat_strip$lon > -119 & lat_strip$lon < -117)
ggplot(la_area,aes(lon,lat)) + geom_point()

la = f[f$city=='Los Angeles',]
ggplot(la,aes(lon,lat)) + geom_point()
lala = f[f$urban_areas=='Los Angeles--Long Beach--Anaheim, CA',]
ggplot(lala,aes(lon,lat)) + geom_point()
