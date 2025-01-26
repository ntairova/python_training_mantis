from datetime import datetime
import random


def test_delete_project(app):
    if len(app.project.get_list_of_projects()) == 0:
        base_part = "TestProject"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S.%f")
        data = f"{base_part}{random_part}"
        app.project.create_new(project=data)
    old_list_of_projects = app.project.get_list_of_projects()
    project = random.choice(old_list_of_projects)
    app.project.delete_project(project=project)
    new_list_of_projects = app.project.get_list_of_projects()
    old_list_of_projects.remove(project)
    assert sorted(old_list_of_projects) == sorted(new_list_of_projects)

