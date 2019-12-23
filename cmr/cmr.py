import json
import requests
import pandas as pd
import geopandas as gpd
from os import mkdir
from os.path import join, isdir
from shapely.ops import cascaded_union
from shapely.geometry import shape, mapping, box
from datetime import datetime as dt
import json


coll_fields = {
    'cmr_concept_type': ('meta', 'concept-type', ),
    'cmr_concept_id': ('meta', 'concept-id', ),
    'cmr_native_id': ('meta', 'native-id', ),
    'cmr_provider_id': ('meta', 'provider-id', ),
    'cmr_revision_id': ('meta', 'revision-id', ),
    'cmr_revision_date': ('meta', 'revision-date', ),
    'cmr_publication_date': ('umm', 'ProviderDates', 0, 'Date', ),
    'coll_title': ('umm', 'EntryTitle', ),
    'coll_version': ('umm', 'Version', ),
    'coll_doi': ('umm', 'CollectionCitations', 0, 'DOI', 'DOI', ),   
    'coll_abstract': ('umm', 'Abstract', ),
    'coll_shortname': ('umm', 'ShortName', ),
    'coll_status': ('umm', 'CollectionProgress', ),
    #'coll_keywords': ('XX', 'XX', ),
    #'coll_platforms': ('XX', 'XX', ),
    #'coll_datacenters': ('XX', 'XX', ),
    'coll_proclvl': ('umm', 'ProcessingLevel', 'Id', ),
    'coll_proclvl_desc': ('umm', 'ProcessingLevel', 'ProcessingLevelDescription', ),
    'time_min': ('umm', 'TemporalExtent', 'RangeDateTime', 'BeginningDateTime', ),
    'time_max': ('umm', 'TemporalExtent', 'RangeDateTime', 'EndingDateTime', ),
    'lat_min': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'SouthBoundingCoordinate', ),
    'lat_max': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'NorthBoundingCoordinate', ),
    'lon_min': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'WestBoundingCoordinate', ),
    'lon_max': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'EastBoundingCoordinate', ),
}


gran_fields = {
    'cmr_concept_type': ('meta', 'concept-type',),
    'cmr_concept_id': ('meta', 'concept-id',),
    'cmr_native_id': ('meta', 'native-id',),
    'cmr_provider_id': ('meta', 'provider-id',),
    'cmr_revision_id': ('meta', 'revision-id',),
    'cmr_revision_date': ('meta', 'revision-date',),
    'cmr_publication_date': ('umm', 'ProviderDates', 0, 'Date', ),
    'coll_shortname': ('umm', 'CollectionReference', 'ShortName', ),
    'gran_name': ('umm', 'GranuleUR', ),
    'gran_size_mb': ('umm', 'DataGranule', 'ArchiveAndDistributionInformation', 0, 'Size', ),
    'gran_parameters': ('umm', 'MeasuredParameters', ),
    'gran_day_night': ('umm', 'DataGranule', 'DayNightFlag', ),
    'time_min': ('umm', 'TemporalExtent', 'RangeDateTime', 'BeginningDateTime', ),
    'time_max': ('umm', 'TemporalExtent', 'RangeDateTime', 'EndingDateTime', ),
    'lat_min': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'SouthBoundingCoordinate', ),
    'lat_max': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'NorthBoundingCoordinate', ),
    'lon_min': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'WestBoundingCoordinate', ),
    'lon_max': ('umm', 'SpatialExtent', 'HorizontalSpatialDomain', 'Geometry', 'BoundingRectangles', 0, 'EastBoundingCoordinate', ),
}



def cmr_search(endpoint, parameters):
    """ 
    ...
    
    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    # Join query parameters and there values.
    query = "&".join([param+"="+value for param, value in parameters.items()])
    
    # Join the endpoint and query parameters to the request url.
    rurl = "https://cmr.earthdata.nasa.gov/search/{}{}".format(endpoint, query)
    
    # Get the metadata content as JSON.
    response = requests.get(rurl)
    
    # Parse json response to dictionary.
    data = json.loads(response.text)
    
    return(data)



def cmr_selector(dictionary: dict, ordered_keys: tuple, warn: bool=False):
    """
    ...
    
    Parameters
    ----------
    ...
    
    Return
    ------
    ...
    
    """

    def _try(d: dict, k: str):
        """ a safe select function. """
        try:
            return d[k]
        except:
            return None
        
    # Loop over ordered keys and select to appropriate depth. 
    for key in ordered_keys:
        dictionary = _try(dictionary, key)
        if dictionary is None:
            if warn is True:
                print("\n\tWARN: Key select failure [ {} ].".format(key))
            break
        
    # Cannot serialize lists (this func only picks values). Convert.
    if type(dictionary) is list:
        try:
            dictionary = "|".join(dictionary)
        except:
            dictionary = None
        
    # Returns None if the selection was unsuccessful.
    return dictionary

    

def get_df(cmr_data: dict, cmr_keys: dict, max_proj: int=1):
    """ 
    ...
    
    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    
    # Make a list of rows for a table.
    rows = []

    # Loop over COLLECTIONS or GRANULES and select metadata fields.
    for ds in cmr_data["items"]:
        
        # Capture record metadata in a dictionary.
        row_data = {}
        
        # # Try to validate by project count for this dataset.
        # try:
        #     proj_num = len(ds['umm']["Projects"])
        # except:
        #     return pd.DataFrame({})
            
        # # If there are too many projects for this record, skip it.
        # if not proj_num > max_proj:
        
        # Loop over the CMR fields keyset and grab metadata values.
        for k, v in cmr_keys.items():
            row_data[k] = cmr_selector(ds, v)
        
        # Get geometry from spatial extent components.
        try:  
            
            # A few collections do not have bounding boxes, so try.
            row_data['geometry'] = box(
                minx=row_data['lon_min'],
                maxx=row_data['lon_max'],
                miny=row_data['lat_min'],
                maxy=row_data['lat_max'], )
        except:      
            
            # Fall back to global.
            extent = { 'lon_min': -180., 
                        'lon_max': 180., 
                        'lat_min': -90., 
                        'lat_max':  90., }
            
            # Update the row_data and get a geometry.
            row_data.update(extent)
            row_data['geometry'] = box(
                minx=row_data['lon_min'],
                maxx=row_data['lon_max'],
                miny=row_data['lat_min'],
                maxy=row_data['lat_max'], )

        # Append the values of the dictionary as a new row.
        rows.append(list(row_data.values()))

    # Get the list of column names.
    colnames = list(cmr_keys.keys()) + ['geometry']
    
    # Merge the rows into a pandas.DataFrame.
    return pd.DataFrame(rows, columns=colnames)

    # # Get the acces URLs for the dataset.
    # access = get_urls(umm, "datasets")
    
    

def get_gdf(df, crs: str="+init=epsg:4326", geom: str="geometry"):
    """ 
    Convert DataFrame into GeoDataFrame.

    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    return gpd.GeoDataFrame(df, crs=crs, geometry=geom)
