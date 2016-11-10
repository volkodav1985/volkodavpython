# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", middlename="", lastname="", company="", homephone="",
                    mobilephone="", workphone="", email="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename",20),
            lastname=random_string("lastname", 20), company=random_string("company", 20),
                           homephone=("homephone", 20), mobilephone=("mobilephone",20),
            workphone=("workphone", 20), email=("email",20))
    for i in range(2)
]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, contact):
    for contact in testdata:
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) +1 == len(new_contacts)
        old_contacts.append(contact)
        #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



