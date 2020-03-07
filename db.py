from record import Record

class DB:
  def __init__(self):
    this.records = []

  def load(self, path):

    with open(path) as fp:
      line = fp.readline()
      count = 1

      while line:
        add_record(line)
        line = fp.readline()
        count += 1

    print("I found {} records.".format(count))


  def add_record(self, line):

    contents = line.split(',')
    new_record = Record(contents[0], contents[1], contents[2])
    self.records += new_record
    return new_record


  def read_record(self, id):

    for rec in self.records:
      if (rec.id == id):
        print("Id: {}, User: {}, Contents: {}".format(rec.id, rec.user, rec.contents))