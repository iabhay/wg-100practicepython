class Question96:
    def __init__(self):
        self.path = r'database\output96.txt'

    def input_from_user(self):
        res = []
        ask_input = ""
        while ask_input != "CLOSE":
            ask_input = input("Enter Value (Write 'CLOSE' for closing): ")
            lst = ask_input.strip()
            if lst and lst != "" and lst != "CLOSE":
                res.append(lst + "\n")
        return res

    def loading_to_file(self):
        content = self.input_from_user()
        with open(self.path, "a") as f:
            f.writelines(content)


obj = Question96()
obj.loading_to_file()
