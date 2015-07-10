"""Package for exif handler"""
__author__ = 'Garfield'

import exifread
import time
from datetime import date

DATE_TAG = 'EXIF DateTimeOriginal'
DATE_FORMAT = '%Y:%m:%d %H:%M:%S'

def get_date(file_path):
    """Retrieve the EXIF original datetime of the given file
    >>> import os
    >>> from datetime import date
    >>> actual = get_date(os.path.join(os.path.dirname(__file__), '../test/DSC04383.JPG'))
    >>> expected = date(2008, 10, 10)
    >>> actual == expected
    True
    """
    file = open(file_path, 'rb')
    tags = exifread.process_file(file, details=False, stop_tag=DATE_TAG)
    if not DATE_TAG in tags:
        return date(1970, 1, 1)
    datetime_str = str(tags[DATE_TAG])
    if datetime_str == '0000:00:00 00:00:00':
        return date(1970, 1, 1)
    datetime_result = time.strptime(datetime_str, DATE_FORMAT)
    return date.fromtimestamp(time.mktime(datetime_result))
