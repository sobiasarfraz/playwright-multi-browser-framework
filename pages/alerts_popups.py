from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from screenshot_helper import take_screenshot

class AlertsPopup:
    simple_alert_btn = "#alertBtn"
    confirm_alert_btn = "#confirmBtn"
    prompt_alert_btn = "#promptBtn"
    result_display = "#demo"

    def __init__(self,  page:Page):
        self.page = page
        self.simple_alert = page.locator(self.simple_alert_btn)
        self.confirmation_alert = page.locator(self.confirm_alert_btn)
        self.popup = page.locator(self.prompt_alert_btn)
        self.text_field = page.locator(self.result_display)


    def handle_simple_alert(self):
        alert_text = None

        def alert_handle(dialog):
            nonlocal alert_text

            alert_text = dialog.message
            dialog.accept()

        self.page.once("dialog", alert_handle)   # pass function, no ()
        self.simple_alert.click()
        take_screenshot(self.page, "simple_alert")
        return alert_text

    def confirmation_alert_handle(self, accept=True):
        alert_text = None
        def alert_handle(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", alert_handle)
        self.confirmation_alert.click()
        return alert_text

    def handle_prompt_alert(self, text_to_send="Playwright", accept=True):
        alert_text = None

        def alert_handle(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            if accept:
                dialog.accept(text_to_send)  # send text and accept
            else:
                dialog.dismiss()  # cancel the prompt

        self.page.once("dialog", alert_handle)
        self.popup.click()
        return alert_text

    def get_result(self):
        return self.text_field.inner_text()


