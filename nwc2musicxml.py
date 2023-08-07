import argparse
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
def initLog(file_name):
    with open(log_file_name, 'w') as logger:
        logger.write('nwc to musicxml converter\n')
        logger.write(str(datetime.datetime.now()) + '\n\n')

# -----------------
def printStep(step, file_name):
    print(f'{step}: {file_name}', end='\r', flush=True)

# -----------------
def printAndLogError(file_name, post=''):
    log_file_name = 'converter.log'
    log_path = Path(log_file_name)
    if not log_path.exists():
        initLog(log_file_name)

    with open(log_file_name, 'a') as logger:
        logger.write(f'Error:')
        logger.write(f'\n  {file_name}')
        logger.write(f'\n  {error_string}\n\n')

    print(f'Error while processing <{file_name}>')

# -----------------
def parseFile(file_path: Path):
    # seems there is some cache mechanism in music21. Ensure file is reloaded.
    file_path.touch()
    # configure music21
    instrument._ID = 0

    printStep('Parsing', str(file_path))
    return converter.parse(str(file_path))

# -----------------
def writeFile(m21_converter, file_path: Path):
    printStep('Writing', str(file_path))
    m21_converter.write(fmt="musicxml", fp=str(file_path))

# -----------------
def convertFiles(original_files, destination_dir_path):
    errors = 0
    for current_file_path in original_files:
        output_path = Path(destination_dir_path,  Path(current_file_path.name)).with_suffix('.musicxml')

        try:
            c = parseFile(current_file_path)
            writeFile(c, output_path)
        except Music21Exception as e:
            printAndLogError(str(current_file_path), str(e))
            errors += 1
            continue

        # overwrite last line
        sys.stdout.write("\033[K")

    return errors

# -----------------
def parseArguments():
    parser = argparse.ArgumentParser(description='NWC to musicxml converter')
    parser.add_argument('source_files', nargs='+', help='the files to parse.')
    parser.add_argument('destination_dir', help='Existing output directory')

    args = parser.parse_args()

    args.source_files.sort()
    original_pathes = [Path(x).resolve() for x in args.source_files]
    destination_dir_path = Path(args.destination_dir).resolve()

    return original_pathes, destination_dir_path


# -----------------
def finalize(nb_errors):
    print("finished")

    if errors > 0:
        print(f'terminated with {errors} error(s). See converter.log for more infos.')


# -----------------
if __name__ == '__main__':
    original_files, destination_dir = parseArguments()
    errors = convertFiles(original_files, destination_dir)
    finalize(errors)
