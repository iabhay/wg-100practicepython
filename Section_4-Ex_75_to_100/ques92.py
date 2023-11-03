# .py file counter
# Hint - glob.glob1
import fnmatch
import os
import glob


class Question92:
    def __init__(self):
        self.dir_path = r'database\files'

    def file_counter(self):
        count = len(fnmatch.filter(os.listdir(self.dir_path), '*.py*'))
        print('File Count:', count)

    def file_count_using_glob(self):
        file_list = glob.glob1(self.dir_path, "*.py")
        print(len(file_list))


obj = Question92()
obj.file_count_using_glob()
