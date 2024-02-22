import os

def build() -> None:
    os.chdir("document")
    os.chdir("src")

    # Build the document
    os.system("pdflatex ./index.tex --output-directory=../../build/document")
    os.system("pdflatex ./index.tex --output-directory=../../build/document") # Run twice to fix table of contents

    os.chdir("./..")
    os.chdir("./..")

    # Copy the document the dist directory
    os.system("copy \".\\build\\document\\index.pdf\" \".\\dist\\document.pdf\"")


