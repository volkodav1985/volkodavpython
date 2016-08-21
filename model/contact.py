from sys import maxsize


class Contact:

    def __init__(self, name=None, surname=None, job=None, mainaddress=None, phone=None, year=None, secondaddress=None, id=None):
        self.name=name
        self.surname=surname
        self.job=job
        self.mainaddress=mainaddress
        self.phone=phone
        self.year=year
        self.secondaddress=secondaddress
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.surname == other.surname and self.name == other.name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


