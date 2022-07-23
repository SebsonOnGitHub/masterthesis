#!/usr/bin/env python

### Insert dates
import pandas as pd

df_combined = pd.read_csv('combined.csv', header = None)

df_combined_sorted = df_combined.sort_values([0, 3], ascending=[True, True])

df_combined_sorted.to_csv('combined_sorted.csv', index=False, header=None)

### Extract dates
#import pandas as pd

#df_category = pd.read_csv('category_raw.csv', header = None, encoding='latin-1')
#df_page_to_category = pd.read_csv('page_to_category.csv', header = None)

#timestamps_1 = df_category.iloc[:,3]
#timestamps_2 = df_category.iloc[:,4]
#timestamps_final = []

#for i in range(len(timestamps_1)):
#    if len(timestamps_1[i]) == 19 and timestamps_1[i][0:4].isnumeric():
#        timestamps_final.append(timestamps_1[i])
#    else:
#        timestamps_final.append(timestamps_2[i])

#df_page_to_category[3] = timestamps_final

#df_page_to_category.to_csv('combined.csv', index=False, header = None)


### Merge Documents
#df_page = pd.read_csv('page_small_raw.csv', header = None)
#df_category = pd.read_csv('category_small_raw.csv', header = None)


#df_merged = pd.merge(df_page, df_category, on=[0])

#df_merged.to_csv('page_to_category.csv', index=False, header=None)
