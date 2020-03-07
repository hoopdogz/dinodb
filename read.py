from record import Record
from db import DB

# Initialize db and load records
base = DB()
base.load('data/records.txt')

# Create new record
base.add_record("6,hoopdogz,I love skiing")

base.add_record("9,hoopdogz,Nothing bad will ever happen")

base.save('data/records.txt')