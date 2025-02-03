from datetime import datetime

def test_create_new_project(app):
    base_part = "TestProject"
    random_part = datetime.now().strftime("%m%d%Y%H%M%S.%f")
    data = f"{base_part}{random_part}"
    old_list_of_projects = app.soap.list_of_projects(username="administrator", password="root")
    app.project.create_new(project=data)
    #new_list_of_projects = app.soap.list_of_projects(username="administrator", password="root")
    old_list_of_projects.append(data)
    assert sorted(old_list_of_projects) == sorted(app.soap.list_of_projects(username="administrator", password="root"))
    #print(app.soap.list_of_projects(username="administrator", password="root"))
    #print(lt)
    #assert app.soap.list_of_projects(username="administrator", password="root")
