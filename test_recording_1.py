import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("To do one")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("To do two")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Maybe three")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Absolutely 4")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="Absolutely").get_by_label("Toggle Todo").check()
    page.locator("li").filter(has_text="To do two").get_by_label("Toggle Todo").check()
    page.locator("li").filter(has_text="Maybe three").get_by_label(
        "Toggle Todo"
    ).check()
    page.locator("li").filter(has_text="To do one").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="All").click()
    page.get_by_role("button", name="Clear completed").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
