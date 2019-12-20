from cmr import *
import json
import os


def handle_config(cfg: str):
    """ 
    ...

    Parameters
    ----------
    ...
    
    Returns
    -------
    ...
    
    """
    print("# CHECK CFG [ {} ]".format(cfg))
    
    # Read the input JSON.
    with open(cfg, "r") as f:
        config = json.load(f)
        
    # Project name.
    projname = config['options']['project']

    # Assemble and collect paths of configured workspace.
    projdir = config['paths']['projects']
    outdir = os.path.join(projdir, projname)

    # Loop over configured dirs, create those that don't exist.
    for d in [projdir, outdir]:
        if not os.path.isdir(d):
            os.mkdir(d)
            
    # Add the output dir to the paths field.
    config['paths']['outputs'] = outdir

    return config