
class Question94:
    def __init__(self):
        self.path = r'database\urls.txt'

    def file_opener(self):
        content = []
        with open(self.path, "r") as f:
            content = f.readlines()
        return content

    def file_updater(self):
        content = self.file_opener()
        res = []
        for line in content:
            elements = line.strip().split(":")
            new_http = elements[0].replace("s", "", 1)
            new_url = elements[1].replace("/", "://", 1)
            new_element = new_http + new_url + "\n"
            res.append(new_element)

        with open(self.path, "w") as f:
            f.writelines(res)


obj = Question94()
obj.file_updater()
