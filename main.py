import subprocess
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from tomllib import load as loadToml
import argparse

from typing import Literal


def main(backend:Literal["TouchDesigner", "TouchPlayer"]):
    with Path("pyproject.toml").open("rb") as projectFile:
        projectData = loadToml( projectFile )
    
    tdSearchPaths = [ "C:\\Program Files\\Derivative" ] + environ.get("TD_INSTALLSEARCHPATH", "").split(":")
    tdVersion = Path(".touchdesigner-version").read_text()
    executeableName = f"{backend}.exe"
    projectFile = projectData.get("project", {}).get("projectfile", "Project.toe")

    load_dotenv()

    for searchPath in tdSearchPaths:
        tdExecuteable = Path(searchPath, f"TouchDesigner.{tdVersion}", "bin", executeableName)
        if tdExecuteable.is_file():
            print( tdExecuteable )
            tdProcess = subprocess.Popen([str(tdExecuteable),  projectFile])
            print( tdProcess.wait() )
            break
        raise Exception(f"TD-Installation for veruon {tdVersion} not found!")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='UV TD-Launcher',
                    description='Searches the TouchDesigner-Installation and executes the project-file.',
                    epilog='Also takes care of the ENV and stuff.')
    
    parser.add_argument("backend", default = "TouchDesigner", choices=["TouchDesigner", "TouchPlayer"], help= "Which backend to use to execute the projectFile.")
    args = parser.parse_args()

    main( args.backend )

