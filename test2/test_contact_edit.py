from model.contact import Contact


def test_modify_contact(app):
     app.contact.modify(Contact(name="Loli", surname="Pop", job="Semant", mainaddress="22, Fearless.ave, Lynn, MA, 01902",
     phone="857-251-5655u", year="1885", secondaddress="85, Shirley ave, Revere, MA, 02151"))
