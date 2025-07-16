# TD UV Prefab
This is a baseproject that shows how UV can be used as the project- and dependency-manager for TouchDesigner.
This prefab contains some automated setup running from TD for .vscode

## How to
Use uv to install packages.
```uv add $package```

To run the project use 

```uv run edit``` to launch TouchDesigner

```uv run designer``` to launch TouchDesigner and set NODE_ENV to production

```uv run player``` to launch TouchPlayer and set NODE_ENV to production

The touchlauncher package will use the .touchdesigner-version file to determin the correct TouchDesigner-Installation and path.
The entrypoint file is determined by the projectfile entry in the pyproject.toml

## Install UV
https://docs.astral.sh/uv/getting-started/installation/

## ENV-Variables
Currently the script looks in the default install-location and expects the folder to have the build-number. 
You can supply additional search paths by setting ```TD_INSTALLSEARCHPATH``` as a : delimited string. 
.env files will be mounted before TouchDesigner starts.

