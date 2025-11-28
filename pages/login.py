from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

class Login:
    name_input = "#name"
    email_input = "#email"
    phone_input = "#phone"
    address_input = "#textarea"
    radio_click = "//input[@value='female']"
    checkbox_click = "//input[@type='checkbox' and contains(@class, 'form-check-input')]"
    dropdown_first = "#country"
    dropdown_second = "#colors"

    def __init__(self, page: Page):
        self.page = page
        self.name = page.locator(self.name_input)
        self.email = page.locator(self.email_input)
        self.phone = page.locator(self.phone_input)
        self.address = page.locator(self.address_input)
        self.radio = page.locator(self.radio_click)
        self.checkbox = page.locator(self.checkbox_click)
        self.dropdown_one = page.locator(self.dropdown_first)
        self.dropdown_two = page.locator(self.dropdown_second)



    def fill_form(self,names, emails, phones, addresses):
        self.name.fill(names)
        self.email.fill(emails)
        self.phone.fill(phones)
        self.address.fill(addresses)
        self.page.wait_for_timeout(1000)


    def radio_button(self):
         self.radio.click()

    def checkbox_box(self):
        all_boxes = self.checkbox
        total = all_boxes.count()
        #print(f"total check boxes are: {total}")
        for i in range(total):
            all_boxes.nth(i).click()


    def first_dropdown_select(self, value1: str):
        drop_selected = self.dropdown_one
        drop_selected.wait_for(state="visible")
        drop_selected.select_option(value=value1)


    def second_drop_select(self, value2: str):
        second_select = self.dropdown_two
        second_select.wait_for(state="visible")
        second_select.select_option(value=value2)

        #self.second_dropdown().wait_for(state="visible").select_option(value=value2)  ---- one line approach

    def get_second_dropdown_options_count(self) -> int:
        # Count options in dropdown
        return self.dropdown_two.locator("option").count()

    '''
    def date_picker(self):
        return self.page.locator("#datepicker")

    def month_picker(self):
        return self. page.locator(".ui-datepicker-month")

    def year_picker(self):
        return self.page.locator(".ui-datepicker-year")

    def day_picker(self, day: str):
        return self.page.locator(f"//a[text()='{day}']")

    def next_click(self):
        return self.page.locator(".ui-datepicker-next.ui-corner-all")

    def dates_cliks_all(self,year1: str, month1: str, day: str):
        self.date_picker().click()
        while True:
            month = self.month_picker().text_content()
            year = self.year_picker().text_content()
            if month == month1 and year == year1:
                break

            self.next_click().click()
        self.day_picker(day).click()

    def second_date(self):
        return self.page.locator("#txtDate")

    def second_year(self):
        return self.page.locator(".ui-datepicker-year")

    def second_month(self):
        return self.page.locator(".ui-datepicker-month")

    def second_day(self,day2: str):
         return self.page.locator(f"//table[contains(@class,'ui-datepicker-calendar')]//a[text()='{day2}']")

    def second_all_click(self, year2: str, month2: str, day2: str):
        self.second_date().click()
        # Wait for the year and month dropdowns to become visible
        self.second_year().wait_for(state="visible")
        self.second_month().wait_for(state="visible")

        self.second_year().select_option(label=year2)
        self.second_month().select_option(label=month2)
        self.second_day(day2).click()

    def third_date(self):
        return self.page.locator("#start-date")

    def third_date_click(self, year: str, month: str, day: str):
        self.third_date().fill(f"{year}-{month}-{day}")  #"2025-11-18"

    def forth_date(self):
        return self.page.locator("#end-date")

    def forth_dates_click(self,year4: str, month4: str, day4: str):
        self.forth_date().fill(f"{year4}-{month4}-{day4}")

    def submit_date(self):
        return self.page.locator(".submit-btn")

    def submit_click(self):
        self.submit_date().click()

    def message(self):
        return self.page.locator("#result").text_content()
    #def text_message(self):
        #messgae = self.message().text_content()
        #return messgae
        '''










