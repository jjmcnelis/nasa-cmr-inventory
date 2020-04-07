# nasa-cmr-inventory

Process CMR metadata (by project) into tabular and spatial formats for spatial db index.

* [contents](#contents): list of files included for each project and dataset
* [usage](#usage): example invocation of python module `cmr` as script
* [updates](#updates): details about update tracking

## contents

Each **project** has the following files (e.g. [`projects/podaac/ghrsst/`](projects/podaac/ghrsst/)):

* [`projects/podaac/ghrsst/ds.json`](projects/podaac/ghrsst/ds.json): UMM-C records for all datasets (API response as JSON)
* [`projects/podaac/ghrsst/ds.csv`](projects/podaac/ghrsst/ds.csv): UMM-C records parsed to a table
* [`projects/podaac/ghrsst/ds.geojson`](projects/podaac/ghrsst/ds.geojson): UMM-C records table as a GeoJSON
* [`projects/podaac/ghrsst/ds.shp`](projects/podaac/ghrsst/ds.shp): UMM-C records table as an ESRI Shapefile
* [`projects/podaac/ghrsst/ds.kml`](projects/podaac/ghrsst/ds.kml): UMM-C records table as a KML

And each **dataset** in a project has the following files (e.g. [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/)):

* [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.json`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.json): UMM-G records for all granules (API response as JSON)
* [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.csv`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.csv): UMM-G records parsed to a table
* [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.geojson`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.geojson): UMM-G records table as a GeoJSON
* [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.shp`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.shp): UMM-G records table as an ESRI Shapefile
* [`projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.kml`](projects/podaac/ghrsst/GOES13-OSISAF-L3C-v1.0/gr.kml): UMM-G records table as a KML

## usage

*Optional: update path and query settings in [`config.json`](config.json).*

Run as a module by passing a valid project name to [`cmr/__main__.py`](cmr/__main__.py):

```shell
python -m cmr ghrsst
```

### update all projects

This wrapper script calls CMR collections endpoint to retrieve all of the unique project names for the input CMR provider (set `__PROVIDER__` in [`update.py`](update.py)).

```shell
./update.py
```

## updates

Update history is tracked by project in [`projects/podaac/projects.json`](projects/podaac/projects.json).

*The PROVIDER.md ([PODAAC.md](PODAAC.md)) is regenerated with every successful run.*
