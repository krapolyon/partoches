import glob
import os
import sys
from music21 import converter

if len(sys.argv) != 3:
    print("""
usage : nwc2musicxml source dest

source : the files to parse. Should be one string describing the input.
         Can be a directory. Can contains regexp (is passed to glob.glob())

dest : a directory where to write the files.
""")
    sys.exit()

original_files = glob.glob(sys.argv[1])
original_files.sort()
dest_dir = os.path.abspath(sys.argv[2])

failed_files = []
for f in original_files:
    print(f)
    try:
        f = os.path.abspath(f)
        c = converter.parse(f)
    except Exception:
        failed_files.append(f)
        print(f"fail to parse {f}")
        continue
    try:
        filename = f.split('/')[-1]
        new_file = dest_dir + '/'
        new_file += filename.replace("nwc", "musicxml")
        c.write(fmt="musicxml", fp=new_file)
    except Exception:
        failed_files.append(f)
        print(f"fail to write {new_file}")
        continue

print("finished !")
if len(failed_files) > 0:
    print("failed to convert:")
    print(failed_files)
