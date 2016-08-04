from sys import maxsize


class Contact:
    def __init__(self, name=None, surname=None, job=None, mainaddress=None, phone=None, year=None, secondaddress=None):
        self.name=name
        self.surname=surname
        self.job=job
        self.mainaddress=mainaddress
        self.phone=phone
        self.year=year
        self.secondaddress=secondaddress



def __repr__(self):
    return "%s:%s" % (self.name, self.surname)


def __eq__(self, other):
    return  self.name == other.name and self.surname==other.surname



