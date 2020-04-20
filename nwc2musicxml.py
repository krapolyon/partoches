import contextlib
import datetime
import glob
import os
import sys

from functools import wraps
from pathlib import Path

from music21 import converter
from music21 import instrument
from music21 import Music21Exception

# -----------------
# Sanitize arguments
if len(sys.argv) != 3:
    print("""
usage : nwc2musicxml source dest

source : the files to parse. Should be one string describing the input.
         Can be a directory. Can contains regexp (is passed to glob.glob())

dest : a directory where to write the files.
""")
    sys.exit(1)

# -----------------
# Init log
log_file_name = 'converter.log'
with open(log_file_name, 'w') as logger:
    logger.write('nwc to musicxml converter\n')
    logger.write(str(datetime.datetime.now()) + '\n\n')

original_files = glob.glob(sys.argv[1])
original_files.sort()
dest_dir = os.path.abspath(sys.argv[2])

# -----------------
def printAndLog(error_type, file_name, error_string):
    global log_file_name
    with open(log_file_name, 'a') as logger:
        logger.write(f'{error_type} error:')
        logger.write(f'\n  {file_name}')
        logger.write(f'\n  {error_string}\n\n')

    colored_error = '\033[31;1merror\033[39;22m'
    print(f'{colored_error} while {error_type} file {file_name}')

# -----------------
def logit(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        global log_file_name
        # with open(log_file_name, 'a') as logger:
            # with contextlib.redirect_stderr(logger):
        return fn(*args, **kwargs)
    return wrapped

@logit
def parseFile(file_path):
    # seems there is some cache mechanism in music21. Ensure file is reloaded.
    Path(file_path).touch()
    return converter.parse(file_path)

@logit
def writeFile(m21_converter, file_path, dest_dir):
    file_name = file_path.split('/')[-1]
    new_file = dest_dir + '/'
    new_file += file_name.replace("nwc", "musicxml")
    m21_converter.write(fmt="musicxml", fp=new_file)

# -----------------
errors = 0
for current_file in original_files:
    print(f"processing {current_file}", end='\r', flush=True)
    try:
        current_file = os.path.abspath(current_file)
        instrument._ID = 0
        c = parseFile(current_file)
    except Exception as e:
        errors += 1
        printAndLog('parsing', current_file, str(e))
        continue
    try:
        writeFile(c, current_file, dest_dir)
    except Exception as e:
        errors += 1
        printAndLog('writing', new_file, str(e))
        raise e
        continue

    sys.stdout.write("\033[K")

if errors > 0:
    formatted_errors = '\033[39;1m' + str(errors) + '\033[39;22m'
    print(f'terminated with {formatted_errors} error(s)')
    sys.exit(1)

print("finished")
