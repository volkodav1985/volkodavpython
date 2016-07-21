from model.contact import Contact


def test_edit_contact(app):
     if app.group.count() == 0:
          app.group.create(Contact(name="test"))
     app.contact.edit(Contact(name="Loli", surname="Pop", job="Semant", mainaddress="22, Fearless.ave, Lynn, MA, 01902",
                              phone="857-251-5655u", year="1885", secondaddress="85, Shirley ave, Revere, MA, 02151"))
