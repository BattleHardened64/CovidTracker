import csv
import math
import pandas
import chardet
import numpy as np
import dateutil
import random
import uuid

def fn_rd_data(filename):
    data=pandas.read_csv(filename)
    return data

fname = "/Users/kt/Documents/JSON Project/01-30-2022.csv" # change to whatever your file is named
result = fn_rd_data(fname)
print(result)
