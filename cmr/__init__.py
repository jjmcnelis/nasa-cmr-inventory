from cmr import *
from datetime import datetime as dt
import json
import os

remote_config = "https://raw.githubusercontent.com/jjmcnelis/nasa-cmr-inventory/master/config.json"

readme_template = '''# nasa-cmr-inventory

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
{proj_rows}
</table>

## updates

Update history is tracked by project in [`{updates}`]({updates}).

*This README is regenerated with every successful run. Last update on `{timestamp}`.*

'''

readme_row_template = '''  <tr>
    <td>{proj_name}</td>
    <td><a href="{proj_dir}/{proj_name}/">{proj_dir}/{proj_name}/</a></td>
    <td>{proj_dset}</td>
    <td>{proj_gran}</td>
    <td>{proj_last}</td>
  </tr>
'''


def write_readme(directory: str, readme_path: str):
    """ """
    
    # Get the projects reference json as a dictionary.
    with open(os.path.join(directory, "projects.json"), "r") as f:       
        proj_runs = json.load(f)
    
    # Collect a list of rows for readme table.
    proj_rows = []
        
    # Loop over the projects.
    for proj_name, proj_hist in proj_runs.items():

        # Get the last run info.
        last_run = proj_hist[-1]
        
        # Add a row to the list.
        proj_rows.append(readme_row_template.format(
            proj_dir=directory,
            proj_name=proj_name,
            proj_dset=last_run['ndatasets'],
            proj_gran=last_run['ngranules'],
            proj_last=last_run['timestamp'] ))
    
    # Put the rows in a table and format the readme template.
    readme = readme_template.format(
        proj_rows="".join(proj_rows),
        updates=os.path.join(directory, "projects.json"),
        timestamp=dt.now().__str__().split(".")[0],
    )
    
    # Write the readme.
    with open(readme_path, "w") as f:
        f.write(readme)


def handle_config(project: str):
    """ 
    ...

    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    print("# CHECK CFG ")
    
    # Find config.json in current directory or use URL for GitHub copy.
    if not os.path.isfile("config.json"):
        print("WARN: No config.json in current directory. Read from GitHub.")
        config = json.loads(requests.get(remote_config).text)
    else:
        with open("config.json", "r") as f:
            config = json.load(f)

    # Assemble and collect paths of configured workspace.
    projdir = config['paths']['projects']
    outdir = os.path.join(projdir, project)

    # Loop over configured dirs, create those that don't exist.
    for d in [projdir, outdir]:
        if not os.path.isdir(d):
            os.mkdir(d)
            
    # Add the output dir to the paths field.
    config['paths']['outputs'] = outdir

    return config



