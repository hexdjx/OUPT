pip install git+https://github.com/votchallenge/vot-toolkit-python

vot initialize vot2018 --workspace ./vot2018-workspace

配置trackers.ini
for example: 
[OUPT]  # <tracker-name>
label = OUPT
protocol = traxpython

command = import pytracking.run_vot as run_vot; run_vot.run_vot2018('oupt', 'proupt50_vot18')  # Set the tracker name and the parameter name

# Specify a path to trax python wrapper if it is not visible (separate by ; if using multiple paths)
paths = PATH_TO_PYTRACKING

# Additional environment paths
#env_PATH = <additional-env-paths>;${PATH}

vot test OUPT
vot evaluate OUPT
vot analysis OUPT
