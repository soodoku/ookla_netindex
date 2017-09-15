

import pandas as pd
import numpy as np

# Load dataset
print("Load input dataset...")
speeds = pd.read_csv('./input/city_daily_speeds.csv')

# Filter out for only US
print("Filter out for only US...")
us_speeds = speeds[speeds.country_code=='US']

# Add 'year' column and drop unused columns
print("Add 'year' column and drop unused columns...")
us_speeds['year'] = us_speeds.date.apply(lambda x: x[:4])
us_speeds.drop(['country', 'country_code', 'region', 'date'], inplace=True, axis=1)

# Add 'over200' column for download speed over 200kbps test count
us_speeds['over200'] = us_speeds.total_tests[speeds.download_kbps > 200]

# Group by 'region_code', 'city' and 'year'
print("Group by 'region_code', 'city' and 'year'...")
year_grp = us_speeds.groupby(['region_code', 'city', 'year'])

# Calculate by group and rearrange for the output format
print("Calculate by group and rearrange for the output format...")
result = year_grp.agg({'download_kbps': np.mean, 'upload_kbps': np.mean, 'over200': np.sum, 'total_tests': np.sum})
result = result.unstack()

# Load and filter out ZIP code dataset
print("Load and filter out ZIP code dataset...")
zipcode = pd.read_csv('./dataset/zip_code_town.csv')
print zipcode.columns
zipcode = zipcode[zipcode.type=='STANDARD']
# Select zipcode data columns
zipcode = zipcode[['zip', 'primary_city', 'state']]

output = result.reset_index()

# Merge output with zipcode
print("Merging the output with ZIP code...")
merge = output.merge(zipcode, left_on=['region_code', 'city'], right_on=['state', 'primary_city'], how='left')

# Rename columns
colsname = []
for i in merge.columns:
    if len(i) == 2:
        if i[1] == '':
            colsname.append(i[0])
        else:
            colsname.append('_'.join(i))
    else:
        colsname.append(i)
print colsname
merge.columns = colsname

# Check all zip code are valid (no duplicates in different state/city pair)
print("Checking no duplicate zipcodes...")
zip_grp = merge.groupby(['zip'])
grp_size = zip_grp.size()
print("ERROR" if len(grp_size[grp_size > 1]) else "OK")

# Save output to CSV file
print("Save output to CSV file...")
merge.to_csv('./output/netindex_by_year.csv')
