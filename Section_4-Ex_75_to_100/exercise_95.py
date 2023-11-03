class Question95:
    def __init__(self):
        self.path = "database/output95.txt"

    def input_from_user(self):
        res = []
        inp = input("Enter Comma Separated: ")
        lst = inp.split(",")
        for element in lst:
            res.append(element.strip() + "\n")
        return res

    def loading_to_file(self):
        content = self.input_from_user()
        with open(self.path, "w") as f:
            f.writelines(content)


obj = Question95()
obj.loading_to_file()
