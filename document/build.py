import envSetup as setup
import os

def build() -> None:
    os.chdir("document")
    os.chdir("src")

    # Build the document
    os.system("pdflatex ./index.tex --output-directory=../../dist/showcase")
    os.system("pdflatex ./index.tex --output-directory=../../dist/showcase") # Run twice to fix table of contents

    os.chdir("..")
    os.chdir("..")

