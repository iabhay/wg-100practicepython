import fnmatch
import glob
import os
import glob2


class Question92:
    def __init__(self):
        self.dir_path = r'database\subdirs'

    def file_counter(self):
        count = len(fnmatch.filter(os.listdir(self.dir_path), '*.py*'))
        print('File Count:', count)

    def file_count_using_glob(self):
        file_list = glob.glob(f'{self.dir_path}/**/*.py', recursive=True)
        # for file in file_list()
        print(len(file_list))


obj = Question92()
obj.file_count_using_glob()
