import pytest
from widgetastic.widget import View
from widgetastic_patternfly4 import Button

from conftest import CustomBrowser


@pytest.fixture
def browser(selenium):
    selenium.get("http://patternfly-react.netlify.com/components/button")
    return CustomBrowser(selenium)


def test_button_click(browser):
    class TestView(View):
        any_button = Button()
        button1 = Button("Primary")
        button2 = Button("Link to Core Docs")

    view = TestView(browser)
    assert view.any_button.is_displayed
    assert view.button1.is_displayed
    assert view.button2.is_displayed
