from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.createcont(Contact(name="Alex", surname="Lavre", job="Semant", mainaddress="22, Fearless.ave, Lynn, MA, 01902",
    phone="857-251-5655u", year="1885",secondaddress="85, Shirley ave, Revere, MA, 02151"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+ 1 == len(new_contacts)



#def test_add_empty_contact(app):
 #   if app.group.count() == 0:
 #   app.group.create(Contact(name="test"))
    #app.contact.createcont(Contact(name="", surname="", job="", mainaddress="", phone="", year="", secondaddress=""))
