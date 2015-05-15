"""
Create a subset to test performance compared to GD Census
"""
__author__ = 'lluiscanet'
import pandas as pd
import numpy as np

total = pd.read_csv('../data/classify_village_area_images.csv')
# comparison = pd.read_csv('../data/GDDKComparison.csv')
# total_subset = pd.DataFrame(total.dropna(axis=0))
# total_subset['village'] = total_subset.village.map(lambda x: x.replace('\'', ''))
# total_subset = pd.merge(total_subset, comparison)
# total_subset.set_index('image', inplace=True)
sample_rows = np.random.choice(total.index.values, 50)
total_subset = total.ix[sample_rows]
total_subset.to_csv('../examine/subset_classify_village_area_images.csv')
