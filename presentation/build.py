import os
import pathlib

def build() -> None:
    build_snippets_carbon()
    os.chdir("presentation")
    os.chdir("src")

    # Build the presentation
    os.system("pdflatex ./index.tex --output-directory=../../build/presentation")
    os.system("pdflatex ./index.tex --output-directory=../../build/presentation") # Run twice to fix table of contents

    os.chdir("./..")
    os.chdir("./..")

    # Copy the presen tation the dist directory
    os.system("copy \".\\build\\presentation\\index.pdf\" \".\\dist\\presentation.pdf\"")


def build_snippets_carbon(dir: pathlib.Path = "./") -> None:
    resources_path = pathlib.Path(os.path.realpath(__file__)).parent.joinpath("resources")
    code_path = resources_path.joinpath("code").joinpath(dir)
    export_path = resources_path.joinpath("snippets").joinpath(dir)

    for child in code_path.iterdir():
        if child.is_file():
            build_snippet(child, export_path)
        else:
            build_snippets_carbon(pathlib.Path(dir).joinpath(child.name))


    


def build_snippet(input_path: pathlib.Path, output_dir: pathlib.Path) -> None:
    filename = input_path.name
    print(f"Building image for {input_path}...")
    os.system(f"carbon-now {input_path} -p showcase-snippet --save-to {output_dir} --save-as {filename}")