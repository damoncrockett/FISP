import pandas as pd

df = pd.read_csv("./parcels_new.csv")
n = len(df)

import requests
import shutil

BASEPATH = "/data/damoncrockett/FISP/GSV/60/"
BASEURL = "https://maps.googleapis.com/maps/api/streetview?"
KEY= <redacted>
SIZE="size=640x640&"
FOV="fov=60&"

for i in range(n):
    loc_param = df.address.loc[i]
    filestring = str(df.apn.loc[i])
    path = BASEPATH+filestring+".jpg"
    try:
        r = requests.get(BASEURL+KEY+SIZE+FOV+"location="+loc_param,stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        print i,path
    except:
        print 'err'