import pytest
from selenium import webdriver


@pytest.mark.google
def test_google():
    driver = webdriver.Chrome()
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url


@pytest.mark.github
def test_github():
    driver = webdriver.Chrome()
    url = "https://github.com/"
    driver.get(url)

    assert driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    assert driver.current_url == url