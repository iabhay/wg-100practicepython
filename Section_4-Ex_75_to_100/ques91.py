#TEXT/CSV to Database
import tomlkit.items

from database.database_connection import DatabaseConnection
import pandas

class Question91:
    def __init__(self):
        self.DBPATH = "database/database91.db"
        self.input_file = "database/ten_more_countries.txt"

    def database_updater(self):
        data = self.csv_reader()

        with DatabaseConnection(self.DBPATH) as connection:
            cursor = connection.cursor()
            for rank, country_name, area_size in data:
                cursor.execute('INSERT INTO countries (id,country,area) VALUES (?, ?, ?)', (rank, country_name, area_size))

    def csv_reader(self):
        res = []
        with open(self.input_file, "r") as f:
            content = f.readlines()
            for line in content[1:]:
                elements = line.strip().split(",")
                print(elements)
                res.append(elements)
        return res


obj = Question91()
obj.database_updater()