# TD UV Prefab
This is a baseproject that shows how UV can be used as the project- and dependency-manager for TouchDesigner.
This prefab contains some automated setup running from TD for .vscode
Also, this automounts the uv-env. 

## How to
Use uv to install packages.
```uv add $package```


To run the project use ```uv run main.py```
Optionaly pass ```TouchDesigner``` or ```TouchPlayer``` as the backend.

## Install UV
https://docs.astral.sh/uv/getting-started/installation/

## ENV-Variables
Currently the stratupscript looks in the default install-location and expects the folder to have the build-number. 
You can supply additional search paths by setting ```TD_INSTALLSEARCHPATH``` as a : delimited string. 

.env files will be mounted before TouchDesigner starts.

