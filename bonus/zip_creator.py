import zipfile
import pathlib

def make_archive(filepaths, destination_dir):
    destpath = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(destpath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



make_archive(filepaths=["bonus1.py", "bonus2.py"],
                 destination_dir="dest")