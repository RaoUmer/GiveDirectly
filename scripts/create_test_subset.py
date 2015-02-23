"""
Create a subset to test performance compared to GD Census
"""
__author__ = 'lluiscanet'
import pandas as pd

total = pd.read_csv('../data/classify_village_area_images.csv')
comparison = pd.read_csv('../data/GDDKComparison.csv')
# Return object with labels on given axis omitted where alternately any or all of the data are missing
total_subset = pd.DataFrame(total.dropna(axis=0))
total_subset['village'] = total_subset.village.map(lambda x: x.replace('\'', ''))
total_subset = pd.merge(total_subset, comparison)
# Set the DataFrame index (row labels) using one or more existing columns. Basically moves the image column to column 1 as "row labels"
total_subset.set_index('image', inplace=True)
total_subset.to_csv('../data/subset_classify_village_area_images.csv')
