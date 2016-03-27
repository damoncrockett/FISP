DIR = "/Users/damoncrockett/Desktop/FISP/GSM/sat_cuts/"
import os

print "reading tile memberships..."
import pandas as pd
t = pd.read_csv("./parcel_tiles.csv")
ex_tiles = list(set(list(t.set_list)))
ex_tiles.remove("unplaced")
print "...done"

from PIL import Image

import shapefile
polygons_sf = shapefile.Reader("/Users/damoncrockett/Desktop/FISP/SD/SD_TILE_SHAPE/SD_TILE_SHAPE.shp")
records = polygons_sf.records()
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
filenames = [item[1] for item in records]

df = pd.DataFrame(filenames,columns=['filename'])
df['bbox'] = polygon_points
BASE = "/Users/damoncrockett/Desktop/FISP/SD/"
df['local_path'] = BASE+df.filename

from shapely.geometry import Polygon
df['bbox_polygon'] = df.bbox.apply(Polygon)

print "finished reading tile data"
print "reading parcel data..."

polygons_sf = shapefile.Reader("/Users/damoncrockett/Desktop/FISP/SanGIS/Parcels/PARCELS.shp")
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
records = polygons_sf.records()
print "...done."


polygons_sd = []
records_sd = []

for i in range(len(records)):
    if records[i][12]=='SD':
        polygons_sd.append(polygon_points[i])
        records_sd.append(records[i])
        
APN = [item[0] for item in records_sd]
d = pd.DataFrame(APN,columns=['APN'])


print "converting from state plane to latlon..."
# Convert from state plane to latlon
from pyproj import Proj
p_from = Proj(init='epsg:2230') # this was in assessor data
conv = 0.3048     # ft to m
tmp = [[p_from(point[0] * conv, point[1] * conv, inverse=True) for point in polygon] for polygon in polygons_sd]
print "...done."


d['bbox'] = tmp

print "making shapely Polygons..."
from shapely.geometry import Polygon
d['polygon'] = d.bbox.apply(Polygon)
d['polygon_bbox'] = d.polygon.map(lambda x:x.bounds)
print "...done."

# This function normalizes latlons, reorders things so we can get pixels
def norm_reorder_px(tup):
    tmp = (
        int(round(((tup[0] - lon_min) / x_range) * w)),
        int(round((1 - (tup[3] - lat_min) / y_range) * h)), # bc in pixels, 0 at top
        int(round(((tup[2] - lon_min) / x_range) * w)),
        int(round((1 - (tup[1] - lat_min) / y_range) * h))  # bc in pixels, 0 at top
        )
    return tmp

print "cropping tiles..."
for ex_tile in ex_tiles:
    im = Image.open(ex_tile)
    h = im.height
    w = im.width
    
    idx = df[df.local_path==ex_tile].index[0]
    points = df.bbox.loc[idx]
    polygon = df.bbox_polygon.loc[idx]
    p = list(set([item for sublist in points for item in sublist]))
    p.sort()
    
    lon_min = p[0]
    lon_max = p[1]
    lat_min = p[2]
    lat_max = p[3]
    
    APNs = t.groupby("set_list").groups[ex_tile] # gives you the indices
    d.APN = d.APN.apply(int)
    parcel_subset = d.loc[APNs] # subset to just those parcels within our chosen tile
    
    x_range = abs(lon_max - lon_min) # abs bc all our lons are negative
    y_range = lat_max - lat_min
    
    l = list(parcel_subset.index)
        
    counter = -1    
    for i in l:
        counter+=1
        print os.path.basename(ex_tile),counter,"of",len(l)
        parcel_apn = parcel_subset.APN.loc[i]
        parcel_geo = parcel_subset.polygon_bbox.loc[i] 
        tmp = im.crop(norm_reorder_px(parcel_geo))
        s = tmp.size
        if s[0]!=0 and s[1]!=0:
            tmp.save(DIR+str(parcel_apn)+".png")
        
print "...done."
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
