# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10),lastname=random_string("lastname", 20),homephone=("homephone", 20), mobilephone=("mobilephone",20),workphone=("workphone", 20),secondaryphone=("secondaryphone,20"))
    for i in range(2)
]



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contacts(app, contact):
    old_contacts = app.group.get_contact_list()
    app.group.create(contact)
    assert len(old_contacts) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)


