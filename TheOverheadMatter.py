import shapefile
polygons_sf = shapefile.Reader("/Users/damoncrockett/Desktop/FISP/SD/SD_TILE_SHAPE/SD_TILE_SHAPE.shp")
records = polygons_sf.records()
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
filenames = [item[1] for item in records]

import pandas as pd
df = pd.DataFrame(filenames,columns=['filename'])
df['bbox'] = polygon_points
BASE = "/Users/damoncrockett/Desktop/FISP/SD/"
df['local_path'] = BASE+df.filename

from shapely.geometry import Polygon
df['bbox_polygon'] = df.bbox.apply(Polygon)

# Parcel data...
polygons_sf = shapefile.Reader("/Users/damoncrockett/Desktop/FISP/SanGIS/Parcels/PARCELS.shp")
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
records = polygons_sf.records()

polygons_sd = []
records_sd = []

for i in range(len(records)):
    if records[i][12]=='SD':
        polygons_sd.append(polygon_points[i])
        records_sd.append(records[i])
        
APN = [item[0] for item in records_sd]
d = pd.DataFrame(APN,columns=['APN'])

# Convert from state plane to latlon
from pyproj import Proj
p_from = Proj(init='epsg:2230')
conv = 0.3048     # ft to m
tmp = [[p_from(point[0] * conv, point[1] * conv, inverse=True) for point in polygon] for polygon in polygons_sd]

d['bbox'] = tmp
d['bbox_polygon'] = d.bbox.apply(Polygon)

tiles = []
counter = -1

for parcel in d.bbox_polygon:
    counter+=1
    for tile in df.bbox_polygon:
        if parcel.within(tile)==True:
            idx = df[df.bbox_polygon==tile].index
            tiles.append(df.local_path[idx].values[0])
        else:
            tiles.append('edge')
    print "join",counter
    
tiles_df = pd.DataFrame(tiles, columns=['tile'])
import numpy as np
tiles_df['parcel_group'] = np.repeat(range(len(d)),len(df))


tiles_df.to_csv("/Users/damoncrockett/Desktop/FISP/tiles_df.csv",index=False)