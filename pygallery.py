__author__ = 'Garfield'

import os
import exif

rootdir = '/volume1/photo'
target_root = '/volume1/share/photo'
max_num = {}
ignore_list = ['@eaDir']

def handle_file(path):
    print('checing', path, '...')
    if not os.path.isfile(path):
        raise FileNotFoundError

    if not os.path.splitext(path)[1].upper() == '.JPG':
        return

    print('processing', path, '...')
    date = exif.get_date(path)
    target_dir = os.path.join(target_root, str(date.year))
    if not os.path.exists(target_dir):
        print('making dir:', target_dir)
        os.makedirs(target_dir)
    target_dir = os.path.join(target_dir,str(date.month))
    if not os.path.exists(target_dir):
        print('making dir:', target_dir)
        os.makedirs(target_dir)
    target_dir = os.path.join(target_dir, str(date.day))
    if not os.path.exists(target_dir):
        print('making dir:', target_dir)
        os.makedirs(target_dir)
    m_num = 0
    if target_dir in max_num.keys():
        m_num = max_num[target_dir]

    target_path = os.path.join(target_dir, "%05d" % m_num + '.JPG')
    print('making:', '|' + path + '|', '|' + target_path + '|')
    if os.path.exists(target_path):
        os.remove(target_path)
    os.link(path, target_path)
    max_num[target_dir] = m_num + 1

for root, subdirs, files in os.walk(rootdir):
    for ignore in ignore_list:
        if ignore in subdirs:
            subdirs.remove(ignore)
    for file in files:
        handle_file(os.path.join(root, file))

print('finished!!!')