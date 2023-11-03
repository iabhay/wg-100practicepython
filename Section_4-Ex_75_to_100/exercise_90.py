from database.database_connection import DatabaseConnection
import pandas
# Database to CSV using pandas and normal file system both

class Question90:
    def __init__(self):
        self.DBPATH = "database/database90.db"
        self.outputfile = "database/output90.csv"

    def csv_file_generate(self):
        content = self.db_content_reader()
        # with open(self.outputfile, "a") as f:
        #     f.writelines("rank,country,area,population\n")
        #     for row in content:
        #         entry = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "\n"
        #         f.writelines(entry)
        content.columns = ["Rank", "Country", "Area", "Population"]
        content.to_csv(self.outputfile, index=False)

    def db_content_reader(self):
        with DatabaseConnection(self.DBPATH) as connection:
            cursor = connection.cursor()
            content = cursor.execute('SELECT * FROM countries WHERE area>=2000000').fetchall()
            # return content
            df = pandas.DataFrame.from_records(content)
            return df

obj = Question90()
obj.csv_file_generate()
