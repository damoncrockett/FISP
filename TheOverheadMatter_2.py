import pandas as pd
tiles = pd.read_csv("./tiles_df.csv")

import shapefile
# Forgot I needed this again...
polygons_sf = shapefile.Reader("/Users/damoncrockett/Desktop/FISP/SanGIS/Parcels/PARCELS.shp")
records = polygons_sf.records()

records_sd = []

for i in range(len(records)):
    if records[i][12]=='SD':
        records_sd.append(records[i])
        
APN = [item[0] for item in records_sd]
d = pd.DataFrame(APN,columns=['APN'])    

parcel_groups = tiles.groupby("parcel_group").groups
parcel_group_numbers = parcel_groups.keys()

set_lists = []
counter = -1
for number in parcel_group_numbers:
    idx = parcel_groups[number]
    tmp = list(set(list(tiles.tile[idx])))
    if len(tmp) == 2:
        tmp.remove("edge")
        set_lists.append(tmp[0])
    elif len(tmp) == 1:
        set_lists.append("unplaced")
    else:
        set_lists.append("multiple")
            
    counter+=1
    print counter
     
d['set_list'] = set_lists
d.to_csv("./parcel_tiles.csv",index=False)