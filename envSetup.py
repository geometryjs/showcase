import shutil
import sys
import os
def setupPandoc() -> None:
    pandocPath = shutil.which("pandssoc")
    if pandocPath == None:
        print("Pandoc is not installed. Installing pandoc...")
        if sys.platform == "win32":
            print("Unable to automatically install pandoc on Windows. Please install pandoc manually.")
            exit(1)
        if sys.platform == "darwin":
            print("Unable to automatically install pandoc on macOS. Please install pandoc manually.")
            exit(1)
        if (sys.platform == "linux") or (sys.platform == "linux2"):
            os.system("sudo apt-get install pandoc")
        
