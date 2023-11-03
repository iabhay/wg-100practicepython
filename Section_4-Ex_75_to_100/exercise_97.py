class Question97:
    def __init__(self):
        self.path = r'database\output97.txt'

    def input_from_user(self):
        res = []
        ask_input = ""
        while ask_input != "CLOSE":
            ask_input = input("Enter Value (Write 'CLOSE' for closing and 'SAVE' for saving): ")
            lst = ask_input.strip()
            if lst and lst != "" and lst != "CLOSE" and lst != "SAVE":
                res.append(lst + "\n")
            if lst == "SAVE":
                size = len(res)
                if size > 0:
                    res[size-1] = res[size-1]
                    self.loading_to_file(res)
                res = []

    def loading_to_file(self, content):
        # content = self.input_from_user()
        with open(self.path, "a") as f:
            f.writelines(content)


obj = Question97()
obj.input_from_user()

