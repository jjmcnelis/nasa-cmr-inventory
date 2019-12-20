


def get_df_dataset(datasets: dict):
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

    # Loop over datasets and select key metadata fields.
    for ds in datasets["items"]:

        # Select the top level fields: 'umm' and 'meta'
        umm, meta = ds["umm"], ds["meta"]

        # If there is exactly one project, process the dataset to a row.
        if len(umm["Projects"])==1:
            
            # Get the CollectionCitations field from 'umm'.
            citations = umm["CollectionCitations"][0]
            
            # Get the time bounds for the dataset.
            time = umm["TemporalExtents"][0]["RangeDateTimes"][0]
            
            # Get a dictionary of spatial information.
            spatial = get_extent(umm, glbl=True, shply=True)
            
            # Get the acces URLs for the dataset.
            access = get_urls(umm, "datasets")
            
            # Append it as an ordered row to the rows list.
            rows.append((
                umm["EntryTitle"],                  # (1) dataset title
                umm["ShortName"],                   # (1) dataset short name
                citations["DOI"]["DOI"],            # (1) dataset doi
                meta["concept-id"],                 # (1) cmr dataset idr
                meta["provider-id"],                # (1) cmr data center id
                time["BeginningDateTime"],          # (1) start time
                time["EndingDateTime"],             # (1) end time
                *list(spatial['extent'].values()),  # (4) lat/lon envelope
                spatial['global'],                  # (1) global coverage flag
                *access,                            # (5) access urls
                umm["CollectionProgress"],          # (1) publication status
                get_science_keywords(umm),          # (1) science keywords (str)
                spatial['shapely'],                 # (1) wkt geometry (str)
            ))

    # Merge the rows into a pandas.DataFrame.
    return pd.DataFrame(rows, columns=[
        "dataset_title",
        "dataset_shortname",
        "dataset_doi",
        "cmr_conceptid",
        "cmr_providerid",
        "extent_mintime",
        "extent_maxtime",
        "extent_minlon",
        "extent_minlat",
        "extent_maxlon",
        "extent_maxlat",
        "extent_global",
        "web_reference",
        "web_documentation",
        "web_data",
        "web_sdat",
        "web_thredds",
        "publication_status",
        "publication_keywords",
        "geometry"
    ])


def get_extent(umm, glbl: bool=False, shply: bool=False):
    """ 
    ...
    
    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    out = {}
    
    # Try to select some required spatial metadata.
    try:
        umm_extent = umm["SpatialExtent"]
        umm_geometry = umm_extent["HorizontalSpatialDomain"]["Geometry"]
        umm_bounds = umm_geometry["BoundingRectangles"][0]
        out['extent'] = {
            'minx': float(umm_bounds["WestBoundingCoordinate"]), 
            'miny': float(umm_bounds["SouthBoundingCoordinate"]), 
            'maxx': float(umm_bounds["EastBoundingCoordinate"]), 
            'maxy': float(umm_bounds["NorthBoundingCoordinate"]), }
        out['global'] = False if glbl else None
    
    # If no bounding rectangle field is present, use global extent. 
    except: 
        out['extent'] = {'minx': -180, 'miny': -90, 'maxx': 180, 'maxy': 90}
        out['global'] = True if glbl else None
    
    # Add a shapely box vector to the dictionary.
    out['shapely'] = box(**out['extent'])
    
    # Only return the requested items.
    out = out['extent'] if (not glbl and not shply) else out
    return out



def get_science_keywords(umm):
    """ 
    ...
    
    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    keywords = []
    for keyset in umm["ScienceKeywords"]:
        for keyword, value in keyset.items():
            if value not in keywords:
                keywords.append(value)
    return "|".join(keywords)



def get_urls(umm, search):
    """ """
    if search=="datasets":
        url_landingpage = None
        url_documentation = None
        url_datapool = None
        url_sdat = None
        url_thredds = None
        for RelatedUrls in umm["RelatedUrls"]:
            try:
                if RelatedUrls["Relation"][0]=="DATA SET LANDING PAGE":
                    url_landingpage = RelatedUrls["URLs"][0]
                elif RelatedUrls["Description"]=="ORNL DAAC Data Set Documentation":
                    url_documentation = RelatedUrls["URLs"][0]
                elif RelatedUrls["Relation"][0]=="GET DATA":
                    url_datapool = RelatedUrls["URLs"][0]
                else:
                    for url in RelatedUrls["URLs"]:
                        if "webmap" in url:
                            url_sdat = url
                        elif "thredds" in url:
                            url_thredds = url
                        else:
                            pass
            except:
                pass
        return((url_landingpage,
                url_documentation,
                url_datapool,
                url_sdat,
                url_thredds))
    elif search=="granules":
        url_datapool = None
        for RelatedUrls in umm["RelatedUrls"]:
            try:
                if RelatedUrls["Type"]=="GET DATA":
                    url_datapool = RelatedUrls["URL"]
            except:
                pass
        return(url_datapool)
    else:
        return(None)
 
 
 def get_granule_parameters(umm):
    """ """
    granule_parameters = []
    for param in umm["MeasuredParameters"]:
        for name, value in param.items():
            if value not in granule_parameters:
                granule_parameters.append(value)
    return(granule_parameters)