import pandas as pd
df = pd.read_fwf('log.txt')
df.to_csv('log.csv')