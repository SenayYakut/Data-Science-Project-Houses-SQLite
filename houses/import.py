import cs50
import csv
from sys import argv, exit

# set up a database connection
db = cs50.SQL("sqlite:///students.db")
#If the incorrect number of command-line arguments are provided
if len(argv) != 2:
    print("missing command-line argument")
    exit(1)
    
# Imports the data from characters.csv
with open("characters.csv", "r") as csvFile:
    # reading the file as dictionary
    reader = csv.DictReader(csvFile)
    for row in reader:
        # As we are reading data from dict, it should give us the right data we are looking for
        name = row["name"].split()
        first, middle,last = name[0], name[1] if len(name) == 3 else None, name[2]
        house = row["house"]
        birth = row["birth"]
        
    # Since students table is already provided to us, All i need to do insert the data into students tanle in the students.db   
    db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",first, middle, last, house, birth)    
       
# execute SELECT * FROM students; // Should give us the right data  


