__author__ = 'lluiscanet'

# pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools
import pandas as pd

# ShapeHelper is a class defined in utils.py
from housemapper import ShapeHelper
# DataFrame is a two-dimensional data structure. It is the primary pandas data structure
from pandas import DataFrame

# Latitude and longitude offset constants
lat_offset = 0.0021
lon_offset = 0.0019

def append_village_areas(divname):
    """
    Function that reads in "boro/karemo/uranga_village_images.csv" and adds a column with area to the output "boro/karemo/uranga_village_areas_images.csv"
    """
    # Reads in CSV file into DataFrame for boro, karemo, or uranga divisions
    im_vil = pd.read_csv('../data/%s_village_images.csv' % divname.lower())
    # Creates a ShapeHelper object for the given division
    shape_helper = ShapeHelper('../data/shapefiles/fixed_village_shapefiles/%s/%s.shp' % (divname.lower(), divname.lower()),
                               lat_offset, lon_offset)
    # Get a dict of all shape areas keyed by village
    areas = shape_helper.get_shape_areas('village')
    areas_df = DataFrame(areas, index=['area'])
    areas_df = areas_df.transpose()
    areas_df.reset_index(inplace=True)
    areas_df.rename(columns={'index': 'village'}, inplace=True)
    im_vil_areas = pd.merge(im_vil, areas_df, how='left')
    im_vil_areas.set_index('image', inplace=True)
    im_vil_areas.to_csv('../data/%s_village_areas_images.csv' % divname.lower())

def append_village_name(divname):
    """
    Function that reads in "boro/karemo/uranga_images.csv" and adds a column with village to the output "boro/karemo/uranga_village_areas.csv"
    """
    im_ref = pd.read_csv('../data/%s_images.csv' % divname.lower())
    shape_helper = ShapeHelper('../data/shapefiles/fixed_village_shapefiles/%s/%s.shp' % (divname.lower(), divname.lower()),
                               lat_offset, lon_offset)
    im_ref['village'] = im_ref.apply(lambda row: shape_helper.get_point_record_field(row, 'village'), 1)
    im_ref.set_index('image', inplace=True)
    im_ref.to_csv('../data/%s_village_images.csv' % divname.lower())

#Append village names to image record files
append_village_name('boro')
append_village_name('uranga')
append_village_name('karemo')

#Append village areas to shape image record files
append_village_areas('boro')
append_village_areas('uranga')
append_village_areas('karemo')
