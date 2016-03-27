lats = seq(from = 32.8522562177, 
           to = 32.8707305527, 
           by = 0.0000000001)
lons = seq(from = -117.267083726, 
           to = -117.24521069, 
           by = 0.0000000001)

df = data.frame(lat = sample(lats,2048,replace=T),
                lon = sample(lons,2048,replace=T))

write.csv(df,'random_geo_lj_2.csv')


# lj: -117.267083726 32.8707305527 -117.24521069 32.8522562177
# enc: -117.125159348 32.7608587754 -117.103286166 32.7423844405