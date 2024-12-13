import re
from playwright.sync_api import Page, expect


# this test will fail because there is no title named "niks" on the google homepage
def test_has_title(page: Page) -> None:
    page.goto("https://google.com")
    expect(page).to_have_title(re.compile("niks"))


def test_get_feeling_lucky_link(page: Page) -> None:
    page.goto("https://google.com")
    page.get_by_role("button", name="i'm feeling lucky").click()
