from record import Record
from db import DB

import sys

base = DB()
base.load('data/records.txt')

if (sys.argv[1] == "add"):
  base.add_record("{},{},{}".format(sys.argv[2], sys.argv[3], sys.argv[4]))
  base.save('data/records.txt')