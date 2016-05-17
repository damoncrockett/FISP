import pandas as pd

df = pd.read_csv("/data/damoncrockett/random_geo_lj.csv")

import requests
import shutil

BASEPATH = "/data/damoncrockett/streetview/lj/"
BASEURL = "https://maps.googleapis.com/maps/api/streetview?"
KEY= <redacted>
SIZE="size=640x640&"

n = len(df.index)
for i in range(n):
    loc_param = str(df.lat.loc[i])+","+str(df.lon.loc[i])
    # can't use comma in filename, so use underscore instead
    filestring = str(df.lat.loc[i])+"_"+str(df.lon.loc[i])
    # can't have dots or negative signs in filename; use str.translate()
    path = BASEPATH+filestring.translate(None,"-.")+".jpg"
    print i,path
    try:
        r = requests.get(BASEURL+KEY+SIZE+"location="+loc_param,stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'
        
        
        
df = pd.read_csv("/data/damoncrockett/random_geo_enc.csv")
BASEPATH = "/data/damoncrockett/streetview/enc/"
n = len(df.index)
for i in range(n):
    loc_param = str(df.lat.loc[i])+","+str(df.lon.loc[i])
    # can't use comma in filename, so use underscore instead
    filestring = str(df.lat.loc[i])+"_"+str(df.lon.loc[i])
    # can't have dots or negative signs in filename; use str.translate()
    path = BASEPATH+filestring.translate(None,"-.")+".jpg"
    print i,path
    try:
        r = requests.get(BASEURL+KEY+SIZE+"location="+loc_param,stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'