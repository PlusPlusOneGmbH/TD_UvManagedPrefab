# TD UV Prefab
This is a baseproject that shows how UV can be used as the project- and dependency-manager for TouchDesigner.

## Install UV
https://docs.astral.sh/uv/getting-started/installation/

## TouchLaunch
This packkages implements https://github.com/PlusPlusOneGmbH/Py_TD_Launch
Use ```uv run edit``` to start TD.

Check docks for pyproject.toml settings and additional commands.


## TDP Packages
Check https://github.com/PlusPlusOneGmbH/TD_Package for an example how a TouchDesigner specific package could look like. 

For this we can run:
```uv add git+https://github.com/PlusPlusOneGmbH/TD_Package#subdirectory=Packages/ExampleComp``` 
And then use
```mod.ExampleComp.ToxFile```

Note: This specific comp is made in 2025 as it adds typing, but can also work in 2023. Check the Experimental-Branch for direct example with this packeg.

