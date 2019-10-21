import os
import os.path
import math
import sys


def split_file(filename, size_in_bytes):
    print('Splitting %s, with chunk size %s bytes...' % (filename, size_in_bytes))
    with open(filename) as f:
        rows = f.readlines()

    headers = rows[0]

    total_row_count = len(rows)
    statinfo = os.stat(filename)
    split_count = int(math.ceil(statinfo.st_size / size_in_bytes)) + 1
    split_row_count = total_row_count / split_count

    newdir = filename.split('.')[0]
    os.system('mkdir %s' % newdir)
    os.system('split -l %s %s %s/%s' % (split_row_count, filename, newdir, "split_"))

    output_filenames = sorted(os.listdir(newdir))
    for i in range(0, len(output_filenames)):
        with open('%s/%s' % (newdir, output_filenames[i]), 'r') as f:
            with open('%s/split_%s.csv' % (newdir, i), 'w') as f2:
                if i > 0:
                    f2.write(headers)
                f2.write(f.read())

    for fn in output_filenames:
        os.remove('%s/%s' % (newdir, fn))


if __name__ == '__main__':
    path = sys.argv[1]
    if len(sys.argv) > 2:
        target_size_in_mb = int(sys.argv[2])
    else:
        target_size_in_mb = 200

    if os.path.isdir(path):
        filenames = os.listdir(path)
        for fn in filenames:
            split_file('%s/%s' % (path, fn), target_size_in_mb * 1024 * 1024)
    else:
        split_file(path, target_size_in_mb * 1024 * 1024)

    print('Done splitting %s with chunk size of %s bytes' % (path, target_size_in_mb))
