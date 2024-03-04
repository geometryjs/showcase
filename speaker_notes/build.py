import os

def build() -> None:
    os.chdir("speaker_notes")
    os.chdir("src")

    # Build the speaker_notes
    os.system("pdflatex ./index.tex --output-directory=../../build/speaker_notes")
    os.system("pdflatex ./index.tex --output-directory=../../build/speaker_notes") # Run twice to fix table of contents

    os.chdir("./..")
    os.chdir("./..")

    # Copy the presen tation the dist directory
    os.system("copy \".\\build\\speaker_notes\\index.pdf\" \".\\dist\\speaker_notes.pdf\"")
