import envSetup as setup
import os

def build() -> None:
    setup.setupPandoc()
    os.chdir("document")
    os.chdir("src")
    os.system("pandoc -s -f markdown -o ../../dist/document.pdf index.md -H preamble.tex")    

