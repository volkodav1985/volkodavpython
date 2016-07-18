from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="aaaaa", header="kkk", footer="ccc"))
