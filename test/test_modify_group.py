from model.group import Group





def test_modify_group_name(app):
     app.session.login(username="admin", password="secret")
     app.group.modify_first_group(Group(name="Loli"))
     app.session.logout()


def test_modify_header(app):
     app.session.login(username="admin", password="secret")
     app.group.modify_first_group(Group(header="Guchi"))
     app.session.logout()