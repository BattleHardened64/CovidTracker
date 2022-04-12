import os
import csv
import pandas as pd
import requests
import dateutil
from datetime import timedelta, date
from contextlib import closing
from codecs import iterdecode

# iterate over all files within "My_Folder"
for file in os.listdir("."):
    if file.endswith(".csv"):
        tmp = pd.read_csv(os.path.join(".", file))
        tmp.to_csv("mergedFixedWHeader.csv", index=False, header=False, mode='a')
