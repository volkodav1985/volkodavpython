from model.group import Group

def test_edit_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name="aaaaa", header="kkk", footer="ccc"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
