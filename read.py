from record import Record
from db import DB

# Initialize db and load records
base = DB()
base.load('data/records.txt')

# Create new record
base.add_record("6,hoopdogz,I love skiing")
rec2 = base.read_record("6")

base.save('data/records.txt')