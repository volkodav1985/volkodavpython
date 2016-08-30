from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact=Contact(firstname="Alex", lastname="Lavre", company="Semant", address="22, Fearless.ave, Lynn, MA, 01902", homephone="88888",mobilephone="8899999", workphone="77444",
    secondphone="55555", year="1885",secondaddress="85, Shirley ave, Revere, MA, 02151")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", company="", address="",
                      homephone="", mobilephone="", workphone="",
                      secondphone="", year="", secondaddress="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

