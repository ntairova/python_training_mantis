class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_new(self, project):
        wd = self.app.wd
        self.open_add_new_project_page()
        # fill project form
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self, project):
        wd = self.app.wd
        self.go_to_project_page_with_project_list()
        wd.find_element_by_link_text(f'{project}').click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        #sleep(5)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_add_new_project_page(self):
        wd = self.app.wd
        self.go_to_project_page_with_project_list()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def go_to_project_page_with_project_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project)

    def get_list_of_projects(self):
        wd = self.app.wd
        project_list = []
        self.go_to_project_page_with_project_list()
        for row in wd.find_elements_by_css_selector("table.width100 tr.row-1"):
            cells = row.find_elements_by_tag_name("td")[0]
            name = cells.text
            project_list.append(name)
        for row in wd.find_elements_by_css_selector("table.width100 tr.row-2"):
            cells = row.find_elements_by_tag_name("td")[0]
            name = cells.text
            project_list.append(name)
        return project_list













