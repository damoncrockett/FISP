import pandas as pd
DIR = "/Users/damncrockett/Desktop/FISP/"
df = pd.read_csv(DIR+"parcels_new.csv")

IMG_DIR = DIR+"GSM/sat_cuts/"

pct = 0.1

def resize(im):
    w = int(round(im.width * pct))
    h = int(round(im.height * pct))
    im.resize((w,h))
    
...
    

