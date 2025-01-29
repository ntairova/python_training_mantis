from selenium import webdriver

from fixture.james import JamesHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


#from selenium.webdriver import Chrome


class Application:
    def __init__(self, browser, config):
        self.app = Application
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.project = ProjectHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

