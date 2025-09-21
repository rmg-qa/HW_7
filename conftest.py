import pytest
import os
from zipfile import ZipFile
import shutil

filenames = ['tmp/1mb.xlsx', 'tmp/Dummy-PDF-3Pages.pdf', 'tmp/example_2.5kb.csv']


# Создание и перемещение в папку resources
@pytest.fixture(scope='function')
def create_zip_archive():
    with ZipFile('archive.zip', 'w') as my_zip:
        for filename in filenames:
            my_zip.write(filename)
    os.makedirs('resources', exist_ok=True)
    destination_path = os.path.join('resources', 'archive.zip')
    shutil.move('archive.zip', destination_path)
    return destination_path
