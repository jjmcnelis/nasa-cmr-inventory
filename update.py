#!/usr/bin/env python3
from subprocess import call
import requests
import json
import sys

__PROVIDER__ = "PODAAC"

# URL to request the list of collections for a CMR provider.
req = "https://cmr.earthdata.nasa.gov/search/collections.umm_json?provider_short_name={}&page_size=1000"

# Get the JSON response for the formatted string.
res = requests.get(req.format(__PROVIDER__))

# Parse the response to a dictionary.
res = json.loads(res.text)

# Get the unique project short names.
prj = list(set([d['umm']['Projects'][0]['ShortName'] for d in res['items']]))

# Loop over the projects and call the processor script for each.
for i, p in enumerate(prj):
    print("# {d} \n# [ {i} / {t} ]: {p}\n# {d} ".format(
        i=i, t=len(prj), p=p, d="-"*60))
    call("python -m cmr {}".format(p.lower()), shell=True)
