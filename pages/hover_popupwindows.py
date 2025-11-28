from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

class HoverNewWindow:
    hover_trigger = "text=Point Me"
    hover_link_one = '//*[@id="HTML3"]/div[1]/div/div/a[1]'
    hover_link_two = '//*[@id="HTML3"]/div[1]/div/div/a[2]'
    new_tab_button = "text=New Tab"
    popup_button = "text=Popup Windows"
    def __init__(self, page: Page):
        self.page = page
        self.hover_me = page.locator(self.hover_trigger)
        self.hover_option_one = self.page.locator(self.hover_link_one)
        self.hover_option_two = self.page.locator(self.hover_link_two)
        self.new_tab = self.page.locator(self.new_tab_button)
        self.popup_window = self.page.locator(self.popup_button)

    def hover(self):
        self.hover_me.hover()

    def hover_suboption_one(self):
        self.hover_option_one.click()

    def hover_suboption_two(self):
        self.hover_option_two.click()

    #---- now handling new tab and new window
    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_object:
            self.new_tab.click()            # triggers new tab
        new_tab1 =  new_page_object.value   # new Page object
        new_tab1.wait_for_load_state("domcontentloaded")
        return new_tab1      # return to test for further actions

    def open_new_window(self):
        with self.page.context.expect_page() as new_window_object:
            self.popup_window.click()            # triggers new tab
        new_window =  new_window_object.value   # new Page object
        new_window.wait_for_load_state("domcontentloaded", timeout=10000)
        return new_window    # return to test for further actions


