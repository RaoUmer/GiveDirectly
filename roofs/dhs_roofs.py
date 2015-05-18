"""This module does roof analysis for DHS locations"""

import time
import pandas as pd
import utils


##############################################################################

startTime = time.time()

##############################################################################

# Defining constants
API_KEY = 'AIzaSyAejgapvGncLMRiMlUoqZ2h6yRF-lwNYMM'

##############################################################################

# For testing
verbose = True

##############################################################################

# Import and preview csv data
csvFN = 'IMR1990-2000_NL1992-2012_thresh100.csv'
dhsData = pd.read_csv('./csv/' + csvFN)

if verbose:
    print 'Here is a preview of the DHS data:\n'
    print dhsData.head()
    print 'The number of DHS entries is {}'.format(len(dhsData))

##############################################################################

# Pull images using Google Static Maps API from each DHS location
runSection = 1

if runSection:

    outDir = './images/DHS_locations'
    # Number of samples to take from each location
    samples = 1

    # Create data frame for image metadata
    imageData = pd.DataFrame(columns=['image', 'cellid', 'lat', 'lon'])
    print imageData.head()

    # Sampling images
    for index, row in dhsData.iterrows():
        cellid = int(row['cellid'])
        lat = row['lat']
        lon = row['lon']
        if verbose:
            print 'Sampling from DHS location with index = {}, cellid = {}, lat = {}, and lon = {}'.format(index, cellid, lat, lon)
        # Sampling from the DHS location
        imageData = utils.sample_DHS(imageData, cellid, lat, lon, samples, outDir, API_KEY)
        print imageData.head()
        # For testing
        #if index >= 0:
        #    break

    # Outputting image metadata into csv
    imageData.set_index('image', inplace=True)
    imageData.to_csv('./csv/DHS_images.csv')

##############################################################################

# Use GiveDirectly models to estimate roof counts and ratios for each image
runSection = 0

if runSection:
    pass







##############################################################################

endTime = time.time()
print 'The script took ' + str(endTime - startTime) + ' seconds.'
