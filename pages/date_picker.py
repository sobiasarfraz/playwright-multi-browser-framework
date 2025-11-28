from playwright.sync_api import Page

class DatePickerPage:
    start_date = "#datepicker"
    next_month_calendar = ".ui-datepicker-next.ui-corner-all"
    #------ second date -------
    end_date = "#txtDate"
    #----- third date -----
    start_tour = "#start-date"
    #----- fourth date -----
    end_tour = "#end-date"
    #----- submit button------
    submit = ".submit-btn"
    message = "#result"

    def __init__(self, page: Page):
        self.page = page
        self.start_date_picker = page.locator(self.start_date)
        self.next_click = page.locator(self.next_month_calendar)
        #------ second date locators------
        self.end_date_picker = page.locator(self.end_date)
        #------ third date locator----
        self.third_date_picker = page.locator(self.start_tour)
        #------- fourth date selector -------
        self.fourth_date_picker = page.locator(self.end_tour)
        #----- submit button locator------
        self.submit_btn = page.locator(self.submit)
        self.message_txt = page.locator(self.message)

    def day_selector(self, day: str):
        return self.page.locator(f"//a[text()='{day}']")

    def choose_first_calendar(self, year1: str, month1: str, day: str, max_clicks: int = 12):
        self.start_date_picker.click()
        first_month_picker = self.page.locator(".ui-datepicker-month")
        first_year_picker = self.page.locator(".ui-datepicker-year")

        for i in range(max_clicks):
            month = first_month_picker.text_content()
            year = first_year_picker.text_content()
            if month == month1 and year == year1:
                self.day_selector(day).click()
                return True

            self.next_click.click()
        #self.day_selector(day).click()
        print(f"Month {month1} and year {year1} not found in {max_clicks} clicks")
        return False  # failed to select

    def second_day_selector(self, day2: str):
        return self.page.locator(f"//table[contains(@class,'ui-datepicker-calendar')]//a[text()='{day2}']")

    def choose_second_calendar(self, year2: str, month2: str, day2: str):
        self.end_date_picker.click()
        second_year_picker = self.page.locator(".ui-datepicker-year")
        second_month_picker = self.page.locator(".ui-datepicker-month")
        # Wait for the year and month dropdowns to become visible
        second_year_picker.wait_for(state="visible")
        second_month_picker.wait_for(state="visible")

        second_year_picker.select_option(label=year2)
        second_month_picker.select_option(label=month2)
        self.second_day_selector(day2).click()

    def choose_start_tour(self, year: str, month: str, day: str):
        #self.third_date_picker.fill(f"{year}-{month}-{day}")  # "2025-11-18"
        #--- Directly set date value in the input, avoids Playwright fill() errors for type="date"
        #----- zfill(2) makes sure month/day are two digits
        self.page.evaluate(f'document.getElementById("start-date").value = "{year}-{month.zfill(2)}-{day.zfill(2)}"')

    def choose_end_tour(self, year4: str, month4: str, day4: str):
        #self.fourth_date_picker.fill(f"{year4}-{month4}-{day4}")
        self.page.evaluate(f'document.getElementById("end-date").value = "{year4}-{month4.zfill(2)}-{day4.zfill(2)}"')

    def submit_click(self):
        self.submit_btn.click()

    def message_locate(self):
        return self.message_txt.text_content()


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

def dates_cliks_all(self ,year1: str, month1: str, day: str):
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

def second_day(self ,day2: str):
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
    self.third_date().fill(f"{year}-{month}-{day}")  # "2025-11-18"

def forth_date(self):
    return self.page.locator("#end-date")

def forth_dates_click(self ,year4: str, month4: str, day4: str):
    self.forth_date().fill(f"{year4}-{month4}-{day4}")

def submit_date(self):
    return self.page.locator(".submit-btn")

def submit_click(self):
    self.submit_date().click()

def message(self):
    return self.page.locator("#result").text_content()
# def text_message(self):
# messgae = self.message().text_content()
# return messgae
'''


