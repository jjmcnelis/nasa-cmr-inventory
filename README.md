# nasa-cmr-inventory

Process CMR metadata (by project) into tabular and spatial formats for spatial db index.

README contents:

* [projects](#projects): projects table and statistics (below)
* [contents](#contents): list of files included for each project and dataset
* [usage](#usage): example invocation of python module `cmr` as script
* [updates](#updates): details about update tracking

## projects

The first column (*project*) contains the strings passed to CMR collections API:

<table>
  <tr>
    <th>project</th>
    <th>path</th>
    <th>n datasets</th>
    <th>n granules</th>
    <th>last update</th>
  </tr>
  <tr>
    <td>above</td>
    <td><a href="projects/above/">projects/above/</a></td>
    <td>102</td>
    <td>15098</td>
    <td>2019-12-22 22:34:20.070969</td>
  </tr>
  <tr>
    <td>atom</td>
    <td><a href="projects/atom/">projects/atom/</a></td>
    <td>22</td>
    <td>1458</td>
    <td>2019-12-31 14:02:32</td>
  </tr>
  <tr>
    <td>act-america</td>
    <td><a href="projects/act-america/">projects/act-america/</a></td>
    <td>8</td>
    <td>2377</td>
    <td>2019-12-31 14:52:05</td>
  </tr>
  <tr>
    <td>airmoss</td>
    <td><a href="projects/airmoss/">projects/airmoss/</a></td>
    <td>20</td>
    <td>22637</td>
    <td>2019-12-22 22:52:13.948719</td>
  </tr>
  <tr>
    <td>bigfoot</td>
    <td><a href="projects/bigfoot/">projects/bigfoot/</a></td>
    <td>6</td>
    <td>81</td>
    <td>2019-12-22 22:54:23.638429</td>
  </tr>
  <tr>
    <td>boreas</td>
    <td><a href="projects/boreas/">projects/boreas/</a></td>
    <td>303</td>
    <td>7340</td>
    <td>2019-12-22 23:05:04.305273</td>
  </tr>
  <tr>
    <td>carve</td>
    <td><a href="projects/carve/">projects/carve/</a></td>
    <td>1</td>
    <td>60</td>
    <td>2019-12-22 23:05:19.439227</td>
  </tr>
  <tr>
    <td>cms</td>
    <td><a href="projects/cms/">projects/cms/</a></td>
    <td>77</td>
    <td>10230</td>
    <td>2019-12-22 23:14:45.872012</td>
  </tr>
  <tr>
    <td>afrisar</td>
    <td><a href="projects/afrisar/">projects/afrisar/</a></td>
    <td>9</td>
    <td>2623</td>
    <td>2019-12-22 23:15:13.455852</td>
  </tr>
  <tr>
    <td>daymet</td>
    <td><a href="projects/daymet/">projects/daymet/</a></td>
    <td>5</td>
    <td>2928</td>
    <td>2019-12-22 23:17:53.866678</td>
  </tr>
  <tr>
    <td>fife</td>
    <td><a href="projects/fife/">projects/fife/</a></td>
    <td>116</td>
    <td>24875</td>
    <td>2019-12-22 23:20:35.530678</td>
  </tr>
  <tr>
    <td>measures</td>
    <td><a href="projects/measures/">projects/measures/</a></td>
    <td>138</td>
    <td>112786</td>
    <td>2019-12-22 23:27:47.982366</td>
  </tr>
  <tr>
    <td>nacp</td>
    <td><a href="projects/nacp/">projects/nacp/</a></td>
    <td>66</td>
    <td>6203</td>
    <td>2019-12-22 23:37:23.215982</td>
  </tr>
  <tr>
    <td>npp</td>
    <td><a href="projects/npp/">projects/npp/</a></td>
    <td>83</td>
    <td>288</td>
    <td>2019-12-22 23:39:01.889758</td>
  </tr>
  <tr>
    <td>otter</td>
    <td><a href="projects/otter/">projects/otter/</a></td>
    <td>14</td>
    <td>573</td>
    <td>2019-12-22 23:39:30.789025</td>
  </tr>
  <tr>
    <td>prove</td>
    <td><a href="projects/prove/">projects/prove/</a></td>
    <td>4</td>
    <td>19</td>
    <td>2019-12-23 00:11:53.124821</td>
  </tr>
  <tr>
    <td>snf</td>
    <td><a href="projects/snf/">projects/snf/</a></td>
    <td>37</td>
    <td>37</td>
    <td>2019-12-23 00:13:24.769237</td>
  </tr>

</table>

## contents

Each **project** has the following files (e.g. [`projects/above/`](projects/above/)):

* [`projects/above/ds.json`](projects/above/ds.json): UMM-C records for all datasets (API response as JSON)
* [`projects/above/ds.csv`](projects/above/ds.csv): UMM-C records parsed to a table
* [`projects/above/ds.geojson`](projects/above/ds.geojson): UMM-C records table as a GeoJSON
* [`projects/above/ds.shp`](projects/above/ds.shp): UMM-C records table as an ESRI Shapefile
* [`projects/above/ds.kml`](projects/above/ds.kml): UMM-C records table as a KML

And each **dataset** in a project has the following files (e.g. [`projects/above/ABoVE_Arctic_CAP_1658/`](projects/above/ABoVE_Arctic_CAP_1658/)):

* [`projects/above/ABoVE_Arctic_CAP_1658/gr.json`](projects/above/ABoVE_Arctic_CAP_1658/gr.json): UMM-G records for all granules (API response as JSON)
* [`projects/above/ABoVE_Arctic_CAP_1658/gr.csv`](projects/above/ABoVE_Arctic_CAP_1658/gr.csv): UMM-G records parsed to a table
* [`projects/above/ABoVE_Arctic_CAP_1658/gr.geojson`](projects/above/ABoVE_Arctic_CAP_1658/gr.geojson): UMM-G records table as a GeoJSON
* [`projects/above/ABoVE_Arctic_CAP_1658/gr.shp`](projects/above/ABoVE_Arctic_CAP_1658/gr.shp): UMM-G records table as an ESRI Shapefile
* [`projects/above/ABoVE_Arctic_CAP_1658/gr.kml`](projects/above/ABoVE_Arctic_CAP_1658/gr.kml): UMM-G records table as a KML

## usage

*Optional: update path and query settings in [`config.json`](config.json).*

Run as a module by passing a valid project name to [`cmr/__main__.py`](cmr/__main__.py):

```shell
python -m cmr above
```

## updates

Update history is tracked by project in [`projects/projects.json`](projects/projects.json).

*This README is regenerated with every successful run. Last update on `2019-12-31 14:52:05`.*

