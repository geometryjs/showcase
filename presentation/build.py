import os

def build() -> None:
    os.chdir("presentation")
    os.chdir("src")

    # Build the presentation
    os.system("pdflatex ./index.tex --output-directory=../../build/presentation")
    os.system("pdflatex ./index.tex --output-directory=../../build/presentation") # Run twice to fix table of contents

    os.chdir("./..")
    os.chdir("./..")

    # Copy the presen tation the dist directory
    os.system("copy \".\\build\\presentation\\index.pdf\" \".\\dist\\presentation.pdf\"")


