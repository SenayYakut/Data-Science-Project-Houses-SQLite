
import cs50
from sys import argv, exit

#If the incorrect number of command-line arguments are provided
if len(argv) != 2:
    print("missing command-line argument")
    exit(1)
# set up a database connection
db = cs50.SQL("sqlite:///students.db")    
# query the students table in the students.db database for all of the students in the specified house.    
rows = db.execute("SELECT * FROM students WHERE house = ?", argv[-1])
for row in rows:
    print(row["first"] + " " + row["middle"]+ " " if(row["middle"]) else ""+ " " + row["last"] + ", born" + str(row["birth"]))