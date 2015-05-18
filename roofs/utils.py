"""This module contains useful functions for analyzing roof ratios for DHS locations"""

import urllib
import numpy as np
import pandas as pd


##############################################################################

def sample_DHS(image_data, cellid, lat, lon, samples, folder, api_key, random=True, height=400, width=400, zoom=19):
    """
    Uses the Google Static Maps API to get a certain number of samples from the given DHS location.
    :param image_data: Data Frame containing image metadata to be updated
    :param cellid: Cell ID of DHS location
    :param lat: Latitude of DHS location
    :param lon: Longitude of DHS location
    :param api_key: Google Static Maps API key
    :param folder: Output directory to store images in
    :param random: Samples randomly according to a normal distribution
    :param height: Height of image in pixels
    :param width: Width of image in pixels
    :param zoom: Zoom level of image
    """
    print 'Sampling {} images from DHS cell {} at lat = {} and lon = {}'.format(samples, cellid, lat, lon)
    urlPattern = 'https://maps.googleapis.com/maps/api/staticmap?center=%0.6f,%0.6f&zoom=%s&size=%sx%s&maptype=satellite&key=%s'
    latIm = lat
    lonIm = lon
    for i in xrange(1, samples + 1):
        # For samples past the first one, perturb lat/lon with uniform distribution between -0.25 and 0.25 degrees (corresponding to the half degree aggregated DHS data)
        if i > 1:
            latIm = lat + np.random.uniform(-0.25, 0.25)
            lonIm = lon + np.random.uniform(-0.25, 0.25)
        url = urlPattern % (latIm, lonIm, zoom, height, width, api_key)
        outImage = '%s_%0.6f_%0.6f.png' % (cellid, latIm, lonIm)
        # Save center image into output directory with correct name
        fp = '%s/%s' % (folder, outImage)
        urllib.urlretrieve(url, fp)
        print 'Sample {} for DHS cell {} saved'.format(i, cellid)
        # Update image metadata data frame
        im_data = pd.DataFrame({'image': [outImage], 'cellid': [cellid], 'lat': [latIm], 'lon': [lonIm]})
        image_data = pd.concat([image_data, im_data])
    return image_data

##############################################################################





##############################################################################



##############################################################################
