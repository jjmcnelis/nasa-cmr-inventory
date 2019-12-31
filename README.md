# nasa-cmr-inventory

Process CMR metadata (by project) into tabular and spatial formats for spatial db index.

Each **project** has the following files (e.g. [`docs/above/`](docs/above/)):

* [`docs/above/ds.json`](docs/above/ds.json): UMM-C records for all datasets
* [`docs/above/ds.csv`](docs/above/ds.csv): UMM-C records parsed to a table
* [`docs/above/ds.shp`](docs/above/ds.shp): UMM-C records table as an ESRI Shapefile

And each **dataset** in a project has the following files (e.g. [`docs/above/ABoVE_Arctic_CAP_1658/`](docs/above/ABoVE_Arctic_CAP_1658)):

* [`docs/above/ABoVE_Arctic_CAP_1658/gr.json`](docs/above/ABoVE_Arctic_CAP_1658/gr.json): UMM-G records for all granules
* [`docs/above/ABoVE_Arctic_CAP_1658/gr.csv`](docs/above/ABoVE_Arctic_CAP_1658/gr.csv): UMM-G records parsed to a table
* [`docs/above/ABoVE_Arctic_CAP_1658/gr.shp`](docs/above/ABoVE_Arctic_CAP_1658/gr.shp): UMM-G records table as an ESRI Shapefile

## projects

* [above](docs/above/)
* [act-america](docs/act-america/)
* [afrisar](docs/afrisar/)
* [airmoss](docs/airmoss/)
* [atom](docs/atom/)
* [bigfoot](docs/bigfoot/)
* [boreas](docs/boreas/)
* [carve](docs/carve/)
* [cms](docs/cms/)
* [daymet](docs/daymet/)
* [fife](docs/fife/)
* [measures](docs/measures/)
* [nacp](docs/nacp/)
* [npp](docs/npp/)
* [otter](docs/otter/)
* [prove](docs/prove/)
* safari2000 (FAIL)
* [snf](docs/snf/)

## usage

1. Update [`config.json`](config.json) to the desired project identifier:

```json
{
  "options": {
    "project": "above"
  },
  ...
}
```

2. Run [`cmr`](cmr/) as a Python module:

```shell
python -m cmr config.json
```
