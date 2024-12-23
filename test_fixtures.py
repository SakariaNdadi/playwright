import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("Before the test runs")

    page.goto("https://google.com")

    yield

    print("after the test runs")


def test_main_navigation(page: Page):
    expect(page).to_have_url("https://www.google.com/")
