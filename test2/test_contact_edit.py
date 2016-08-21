from model.contact import Contact
from random import randrange

def test_edit_contact(app):
     if app.contact.count() == 0:
          app.contact.create(Contact(name="test"))
     old_contacts = app.contact.get_contact_list()
     index = randrange(len(old_contacts))
     contact=Contact(name="Loli", surname="Pop", job="Semant", mainaddress="22, Fearless.ave, Lynn, MA, 01902",
     phone="857-251-5655u", year="1885", secondaddress="85, Shirley ave, Revere, MA, 02151")
     contact.id=old_contacts[index].id
     app.contact.edit_contact_by_index(index,contact)
     new_contacts = app.contact.get_contact_list()
     assert len(old_contacts) == len(new_contacts)
     old_contacts[index] = contact
     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
