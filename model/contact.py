from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, homephone=None, workphone=None, mobilephone=None, secondphone=None, address=None, year=None, secondaddress=None, id=None):
        self.firsrtname=firstname
        self.lastname=lastname
        self.company=company
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.secondphone=secondphone
        self.address=address
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


