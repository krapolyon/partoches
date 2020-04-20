import glob
import os
import sys
from music21 import converter
from music21 import instrument

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
for current_file in original_files:
    print(f"processing {current_file}", end='\r', flush=True)
    try:
        current_file = os.path.abspath(current_file)
        instrument._ID = 0
        c = converter.parse(current_file)
    except Exception:
        failed_files.append(current_file)
        print(f"fail to parse {current_file}")
        continue
    try:
        filename = current_file.split('/')[-1]
        new_file = dest_dir + '/'
        new_file += filename.replace("nwc", "musicxml")
        c.write(fmt="musicxml", fp=new_file)
    except Exception:
        failed_files.append(current_file)
        print('')
        print(f"fail to write {new_file}")
        continue

    sys.stdout.write("\033[K")

if len(failed_files) > 0:
    print('terminated with errors')

print("finished")
