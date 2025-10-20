# TD UV Prefab
This is a baseproject that shows how UV can be used as the project- and dependency-manager for TouchDesigner.

It uses a hack to mount the package-folders defined in the .packagefolder-file just in time, without any raceconditions. [ Blogpost coming ]

Check /local/modules as it could be used for any dependency manager. I just like UV most.

## Install UV
https://docs.astral.sh/uv/getting-started/installation/

## Python Version
Make sure to set the correct python version in .python-version and/or .touchdesigner-version.

## MonkeyBrain
This packkages implements https://github.com/PlusPlusOneGmbH/MonkeyBrain
Use ```uv run mb edit``` to start TD.

Check docks for pyproject.toml settings and additional commands.


## Developing a package
This project can, to some extend even be used as the basis of a TouchDesigner Package. 

For this to work, you need to externalize all important data in to a subdirectory like ```src/PackageName``` which contains an ```__init__.py``` file. 

As an example you can check out the current DevBranch of the TauCeti Repository. 
[TauCeti PresetSystem on Github.com](https://github.com/PlusPlusOneGmbH/TD_TauCeti_Presetsystem/tree/dev)

The package follows the same structure as a default python package. This means you can follow almost any guide for simple python packages. Also, this package then could be published to PyPI.
[Packaging PythonProject on Python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/)