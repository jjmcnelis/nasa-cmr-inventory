# nasa-cmr-inventory

Process CMR metadata (by project) into tabular and spatial formats for spatial db index.

README contents:

* [projects](#projects): projects table and statistics (below)
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
    <td>omg</td>
    <td><a href="projects/podaac/omg/">projects/podaac/omg/</a></td>
    <td>3</td>
    <td>887</td>
    <td>2020-04-06 18:07:25</td>
  </tr>
  <tr>
    <td>iss_rapidscat</td>
    <td><a href="projects/podaac/iss_rapidscat/">projects/podaac/iss_rapidscat/</a></td>
    <td>15</td>
    <td>30000</td>
    <td>2020-04-06 17:46:38</td>
  </tr>
  <tr>
    <td>roses</td>
    <td><a href="projects/podaac/roses/">projects/podaac/roses/</a></td>
    <td>2</td>
    <td>2006</td>
    <td>2020-04-06 17:46:47</td>
  </tr>
  <tr>
    <td>cioss</td>
    <td><a href="projects/podaac/cioss/">projects/podaac/cioss/</a></td>
    <td>3</td>
    <td>53</td>
    <td>2020-04-06 17:46:57</td>
  </tr>
  <tr>
    <td>poes</td>
    <td><a href="projects/podaac/poes/">projects/podaac/poes/</a></td>
    <td>8</td>
    <td>7504</td>
    <td>2020-04-06 17:47:30</td>
  </tr>
  <tr>
    <td>ostm</td>
    <td><a href="projects/podaac/ostm/">projects/podaac/ostm/</a></td>
    <td>2</td>
    <td>4000</td>
    <td>2020-04-06 17:47:44</td>
  </tr>
  <tr>
    <td>quikscat</td>
    <td><a href="projects/podaac/quikscat/">projects/podaac/quikscat/</a></td>
    <td>9</td>
    <td>10003</td>
    <td>2020-04-06 17:48:30</td>
  </tr>
  <tr>
    <td>saral</td>
    <td><a href="projects/podaac/saral/">projects/podaac/saral/</a></td>
    <td>2</td>
    <td>2000</td>
    <td>2020-04-06 17:48:38</td>
  </tr>
  <tr>
    <td>metop</td>
    <td><a href="projects/podaac/metop/">projects/podaac/metop/</a></td>
    <td>7</td>
    <td>12000</td>
    <td>2020-04-06 17:49:16</td>
  </tr>
  <tr>
    <td>aviso</td>
    <td><a href="projects/podaac/aviso/">projects/podaac/aviso/</a></td>
    <td>1</td>
    <td>1</td>
    <td>2020-04-06 17:49:20</td>
  </tr>
  <tr>
    <td>spurs</td>
    <td><a href="projects/podaac/spurs/">projects/podaac/spurs/</a></td>
    <td>35</td>
    <td>4840</td>
    <td>2020-04-06 17:50:35</td>
  </tr>
  <tr>
    <td>smap-sss</td>
    <td><a href="projects/podaac/smap-sss/">projects/podaac/smap-sss/</a></td>
    <td>11</td>
    <td>14550</td>
    <td>2020-04-06 17:51:24</td>
  </tr>
  <tr>
    <td>ghrsst</td>
    <td><a href="projects/podaac/ghrsst/">projects/podaac/ghrsst/</a></td>
    <td>91</td>
    <td>156623</td>
    <td>2020-04-06 17:59:58</td>
  </tr>
  <tr>
    <td>eos</td>
    <td><a href="projects/podaac/eos/">projects/podaac/eos/</a></td>
    <td>121</td>
    <td>86332</td>
    <td>2020-04-06 18:07:11</td>
  </tr>
  <tr>
    <td>reynolds_sst</td>
    <td><a href="projects/podaac/reynolds_sst/">projects/podaac/reynolds_sst/</a></td>
    <td>5</td>
    <td>6053</td>
    <td>2020-04-06 18:07:54</td>
  </tr>
  <tr>
    <td>grace-fo</td>
    <td><a href="projects/podaac/grace-fo/">projects/podaac/grace-fo/</a></td>
    <td>16</td>
    <td>3321</td>
    <td>2020-04-06 18:08:36</td>
  </tr>
  <tr>
    <td>geos-3</td>
    <td><a href="projects/podaac/geos-3/">projects/podaac/geos-3/</a></td>
    <td>1</td>
    <td>3</td>
    <td>2020-04-06 18:08:39</td>
  </tr>
  <tr>
    <td>cygnss</td>
    <td><a href="projects/podaac/cygnss/">projects/podaac/cygnss/</a></td>
    <td>4</td>
    <td>5307</td>
    <td>2020-04-06 18:09:02</td>
  </tr>
  <tr>
    <td>oscar</td>
    <td><a href="projects/podaac/oscar/">projects/podaac/oscar/</a></td>
    <td>2</td>
    <td>659</td>
    <td>2020-04-06 18:09:09</td>
  </tr>
  <tr>
    <td>grace</td>
    <td><a href="projects/podaac/grace/">projects/podaac/grace/</a></td>
    <td>46</td>
    <td>5325</td>
    <td>2020-04-06 18:10:48</td>
  </tr>
  <tr>
    <td>measures</td>
    <td><a href="projects/podaac/measures/">projects/podaac/measures/</a></td>
    <td>147</td>
    <td>122678</td>
    <td>2020-04-06 18:36:19</td>
  </tr>
  <tr>
    <td>envisat</td>
    <td><a href="projects/podaac/envisat/">projects/podaac/envisat/</a></td>
    <td>1</td>
    <td>2000</td>
    <td>2020-04-06 18:36:29</td>
  </tr>

</table>

## updates

Update history is tracked by project in [`projects/podaac/projects.json`](projects/podaac/projects.json).

*This README is regenerated with every successful run. Last update on `2020-04-06 18:36:29`.*
