import os
import zipfile


__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


def clean_cache():
    """
    Create an empty folder named 'cache' in the
    current directory. If it already exists, delete
    everything in the cache folder
    """
    if os.path.exists('cache'):
        for file in os.listdir('cache'):
            os.remove(os.path.join('cache', file))
    else:
        os.mkdir('cache')


def cache_zip(zip_file, cache_dir):
    """Unpack a zip file into a clean cache folder"""
    with zipfile.ZipFile(zip_file, 'r') as zip:
        zip.extractall(cache_dir)


def cached_files():
    """
    Return a list of the absolute paths of all
    the files in the cache
    """
    text_files = map(
        lambda text_file: f'{os.getcwd()}/cache/{text_file}',
        os.listdir('cache'))
    return list(text_files)


def find_password(text_files):
    """
    Read the text in each file and
    find the super secret password
    """
    for text_file in text_files:
        with open(text_file, encoding='utf-8') as file:
            for line in file:
                if 'password' in line:
                    password = line[line.find(' ') + 1:].rstrip()
                    return password
