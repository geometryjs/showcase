import envSetup as setup
import os

def build() -> None:
    if not setup.setupPandoc(): return None
    os.chdir("document")
    os.chdir("src")
    out = ""
    with open("title.md", "r", encoding="utf-8") as title:
        out = out +  "".join(title.readlines())
    with open("content.md", "r", encoding="utf-8") as content:
        out = out + "".join(content.readlines()).replace("# ", "\\newpage\n# ")

    with open("final.md", "w", encoding="utf-8") as content:
        content.write(out)

    os.system("pandoc final.md -s -f markdown -o ../../static/showcase.pdf -H preamble.tex") 

    os.remove("final.md")

    os.chdir("..")
    os.chdir("..")

