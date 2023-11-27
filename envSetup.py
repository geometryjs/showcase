import shutil

def setupPandoc() -> bool:
    pandocPath = shutil.which("pandoc")
    if pandocPath == None:
        print("Pandoc not found. Skipping build step, commited PDF will be used.")
        return False
    return True