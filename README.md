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
The behavior can be defined via the pyproject.toml
```toml
[tool.touchdesigner]
# Define the projectfile. Should sit in the root-dir of the project.
projectfile = "Project.toe"

# Defines the behaviour how the TD-Install should be searched for 
enforce-version="closest-build"
# Options: ( for example we use the following: Set Version: 2300.12000. Available Version [2025.1000, 2023.2000, 2023.4000]
# strict : looks for the exact version set in the .touchdesigner-version file. 
# closest-build : looks for the closes build to the set version while ignoring other versions. - Example: Will pick 2023.2000
# latest-build : looks for the latest build in the same version. - Example: Will pick 2023.4000
# latest-version : simply takes the latest available installed version. Def not suggestes! - Example: Will pick 2025.1000

```
## Install UV
https://docs.astral.sh/uv/getting-started/installation/

## ENV-Variables
Currently the script looks in the default install-location and expects the folder to have the build-number. 
You can supply additional search paths by setting ```TD_INSTALLSEARCHPATH``` as a : delimited string. 
.env files will be mounted before TouchDesigner starts.

