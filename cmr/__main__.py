#!/usr/bin/env python3
__doc__ = '''
PyABoVE: Generate KML inventory of ABoVE assets.
  version: {}
  author:  {}
  email:   {}

'''.format( "0.1.0", "jjmcnelis", "jjmcn@gmail.com" )
from os.path import join as pjoin
from .cmr import *
from . import *
import sys
import os

try:  # Run config handler. Exit on error.
    config = handle_config(sys.argv[1])
except Exception as e:
    print("ERROR: Bad configuration file."); raise(e)

# Select some items from the config.
outputs = config['paths']['outputs']
project = config['options']['project'] 

### DATASETS: Optionally retrieve new dataset reference files.
if config['cmr']['datasets']['update']:
    print("# QUERY CMR [ DATASETS ]")
    
    # Add the project to the search parameters.
    config['cmr']['datasets']['search']['parameters']['project'] = project
        
    # Request an updated datasets reference.
    datasets = cmr_search(**config['cmr']['datasets']['search'])
    
    # Write dataset reference JSON.
    with open(pjoin(outputs, "ds.json"), "w") as f:
        f.write(json.dumps(datasets, indent=2))

    # Get dataset dictionary as a pandas.DataFrame and write to CSV.
    ddf = get_df(datasets, coll_fields)
    ddf.to_csv(pjoin(outputs, "ds.csv"), index=False)

    # Get the pandas.DataFrame as a GeoDataFrame and write to ESRI Shapefile.
    gdf = get_gdf(ddf)
    gdf.to_file( driver="ESRI Shapefile", 
                 #filename=pjoin(outputs, "ds.shp"))
                 filename=pjoin(outputs, "ds.shp"))

else:  ### If update is false, open existing datasets reference.
    print("# READ REFERENCES [ DATASETS ]")
    ddf = pd.read_csv(pjoin(outputs, "ds.csv"))
    with open(pjoin(outputs, "ds.json"), "r") as f:
        datasets = json.load(f)

### GRANULES: Optionally retrieve new granules reference files.
gran_counter = 0

if config['cmr']['granules']['update']:
    print("# QUERY CMR [ GRANULES ]")
    
    # iterate over datasets and process granules.
    for i, r in ddf.iterrows():

        # Get the dataset short name.
        dsname = r.coll_shortname

        # Get the granules path for this dataset.
        dsgrdir = pjoin(outputs, dsname)

        # Write a folder to the dataset reference directory if none exists.
        if not os.path.isdir(dsgrdir):
            os.mkdir(dsgrdir)

        # Select cmr search configuration for granules.
        search_args = config['cmr']['granules']['search'].copy()

        # Update the null 'collection_concept_id' field.
        search_args['parameters']['collection_concept_id'] = r.cmr_concept_id

        # Call cmr_search to request the dataset's granules.
        print("  - [ {}/{} ]\t{}".format(i+1, ddf.index.size, dsname))
        granules = cmr_search(**search_args)

        # Write granule reference json to the dataset directory.
        with open(pjoin(dsgrdir, "gr.json".format(dsname)), "w") as f:
            f.write(json.dumps(granules, indent=2))

        # Get dataset dictionary as a pandas.DataFrame and write to CSV.
        grdf = get_df(granules, gran_fields)
        
        # If the number of granules is > 0, write to CSV and Shapefile.
        if grdf.index.size > 0:
            grdf.to_csv(pjoin(dsgrdir, "gr.csv"), index=False)

            # Get the pandas.DataFrame as a GeoDataFrame.
            grgdf = get_gdf(grdf)
            
            # Write to ESRI Shapefile.
            grgdf.to_file( driver="ESRI Shapefile", 
                           filename=pjoin(dsgrdir, "gr.shp"))
            
        # Add the granule count to the granule counter.
        gran_counter+=int(grdf.index.size)

### Document what happened this run. Read the projects file.
with open(pjoin(config['paths']['projects'], "projects.json"), "r") as f:
    proj_reference = json.load(f)

# Record some information about this run.
proj_record = {
    'timestamp': dt.now().__str__(), 
    'ndatasets': ddf.index.size, 
    'ngranules': gran_counter, }

# If the project already exists, append this run.
if project in list(proj_reference.keys()):
    proj_reference[project].append(proj_record)
else:
    proj_reference[project] = [ proj_record ]

### Add project to the projects.json if it's not already there.
with open(pjoin(config['paths']['projects'], "projects.json"), "w") as f:
    # Replace the content of the open file.
    f.write(json.dumps(proj_reference, indent=2))
