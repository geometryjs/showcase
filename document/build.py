import envSetup as setup
import os

def build() -> None:
    os.chdir("document")
    os.chdir("src")

    # Build the document
    os.system("pdflatex ./index.tex --output-directory=../../dist/showcase")

    os.chdir("..")
    os.chdir("..")

