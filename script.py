##Imports
import pandas as pd 
import numpy as np 
import datetime
from datetime import *
import yaml
import pprint
from pprint import pprint

##Open yaml config in read mode and Load yaml config 
with open('config.yaml', 'r') as config_file: 
    config = yaml.load(config_file, Loader = yaml.FullLoader) 

##Params
file = config['file']['file_name']
separator = config['file']['separator']
df = pd.read_csv(file,sep=separator,index_col=False)
shape = df.shape
rows = shape[0]
columns = shape[1]
col_names = df.columns
pop_counts = df.count()

##Output file info to console
print(f"Analysing {file} at {datetime.now()}")
print('\n')
print(f"File has {rows} rows and {columns} columns")
print('\n')
print("Columns are: ")
pprint(col_names)
print('\n')
print("File populated counts are:")
pprint(pop_counts)
print('\n')
uniques = df.nunique()
for c,v in uniques.items():
    print(f"{c} has {v}/{rows} unique values")
    if v == rows:
        pk = c     
print('\n')        
print(f"Column [{pk}] is totally unique: possible primary key")