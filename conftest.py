import json
import os.path
from fixture.application import Application
import pytest


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    web_login = load_config(request.config.getoption("--target"))['webadmin']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_login["username"], password=web_login["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
     def fin():
         fixture.session.ensure_logout()
         fixture.destroy()
     request.addfinalizer(fin)
     return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "chrome")
    parser.addoption("--target", action="store", default="target.json")










