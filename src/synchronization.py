import os
import shutil
import argparse
import time
import logging
from pathlib import Path
import sys

LOG_FILE_PATH = './logs/synch.log'

def _get_logger():

    logger = logging.getLogger('synch folder')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)


    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    return logger

LOGGER = _get_logger() # TO TEST

def sync_copy(source_path, replica_path, test_mode=False):
    if not os.path.exists(replica_path):
        os.makedirs(replica_path)

    for root, _, files in os.walk(source_path):
        replica_root = root.replace(source_path, replica_path, 1)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)
            if os.path.exists(replica_file):
                if os.path.samefile(source_file, replica_file):
                    continue
                os.remove(replica_file)
            shutil.copy2(source_file, replica_root)
            if not test_mode:
                LOGGER.info(f"Copied {source_file} to {replica_file}")

def sync_remove(source_path, replica_path, test_mode=False):

    for root, _, files in os.walk(replica_path):
        source_root = root.replace(replica_path, source_path, 1)
        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_root, file)
            if not os.path.exists(source_file):
                os.remove(replica_file)
                if not test_mode:
                    LOGGER.info(f"Removed {replica_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync two folders.')
    parser.add_argument('--source_path', type=str, default='./source_folder', help='Path of source folder.')
    parser.add_argument('--replica_path', type=str, default='./replica_folder', help='Path of replica folder.')
    parser.add_argument('--log_path', type=str, default='./logs/synch.log', help='Path of replica folder.')
    parser.add_argument('--period', type=int, default=10, help='Sync period in seconds.')
    args = parser.parse_args()
    if args.log_path:
            LOG_FILE_PATH = args.log_path
            LOGGER = _get_logger()
    while True:
        
        sync_copy(args.source_path, args.replica_path)
        sync_remove(args.source_path, args.replica_path)
        time.sleep(args.period)