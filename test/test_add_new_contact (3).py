# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.createcont(Contact(name="Alex", surname="Lavre", job="Semant", mainaddress="22, Fearless.ave, Lynn, MA, 01902", phone="857-251-5655u", year="1885",
        secondaddress="85, Shirley ave, Revere, MA, 02151"))
        app.session.logout()

def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.createcont(Contact(name="", surname="", job="", mainaddress="", phone="", year="", secondaddress=""))
        app.session.logout()






