import os

def build() -> None:
    os.chdir("document")
    os.chdir("src")

    # Build the document
    os.system("pdflatex ./index.tex --output-directory=../../dist/showcase")
    os.system("pdflatex ./index.tex --output-directory=../../dist/showcase") # Run twice to fix table of contents

    os.chdir("./..")
    os.chdir("./..")

    # Copy the document to the root of the project
    os.system("copy \".\\dist\\showcase\\index.pdf\" \".\\dist\\showcase.pdf\"")


