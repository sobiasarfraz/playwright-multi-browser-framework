from contextlib import nullcontext

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from screenshot_helper import take_screenshot
import pytest
import logging

logger = logging.getLogger()
def test_homepage_url_title(page):
    logging.info("url test")
    take_screenshot(page, "main page")
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_title("Automation Testing Practice")


@pytest.mark.parametrize("names, emails, phones, addresses",
                             [
                                 ("Sofia", "sob@gmail.com", "123456789", "320 dawson ln"),
                                 ("Asif", "asif@gmail.com", "123456789", "123 dawson ln"),
                                 ("Araz", "araiz@gmail.com", "1234876543", "567 dawson ln")
                             ])
def test_fill_form(login, page, names, emails, phones, addresses):
    #---- going to fill the form----
    login.fill_form(names, emails, phones, addresses)
    expect(login.name).to_have_value(names)
    expect(login.email).to_have_value(emails)
    expect(login.phone).to_have_value(phones)
    expect(login.address).to_have_value(addresses)

def test_form_allows_empty_name(login):
    login.fill_form("", "sob@gmail", "1234567890", "320 dawson ln")
    expect(login.name).to_have_value("")                     # bug: should reject

def test_form_allows_invalid_email(login):
    login.fill_form("Tim", "bad-email", "1234567890", "320 dawson ln")
    expect(login.email).to_have_value("bad-email")           # bug: no validation

def test_form_allows_short_phone(login):
    login.fill_form("sun", "sob@gmail", "0", "320 dawson ln")
    expect(login.phone).to_have_value("0")                   # bug: no min length

def test_name_field_character_limit(login):
    long_name = "A" * 20
    login.fill_form(long_name, "sob@gmail", "1234567890", "320 dawson ln")
    expect(login.name).to_have_value("A" * 15)    # edge: name limited to 15 chars

def test_form_accepts_special_characters_in_name(login):
    login.fill_form("Jin!@#$%^&*()", "sob@gmail", "1234567890", "320 dawson ln")
    expect(login.name).to_have_value("Jin!@#$%^&*()")       # edge: accepts symbols like !@#$% in name

def test_form_data_does_not_persist_after_refresh(login, page):
    login.fill_form("Temp", "temp@test.com", "000", "Temp")
    page.reload()
    expect(login.name).to_be_empty()

def test_radio_btn(login):
    login.radio_button()
    expect(login.radio).to_be_checked()

def test_radio_btn_cannot_unchecked(login):
    login.radio_button()
    login.radio_button()
    expect(login.radio).to_be_checked()   # edge: radio buttons remain selected once clicked


def test_checkbox(login, page):
    login.checkbox_box()
    boxes = login.checkbox
    count_boxes = boxes.count()
    print(f"total no of checkboxes are: {count_boxes}")
    for i in range(count_boxes):
        expect(boxes.nth(i)).to_be_checked()
    take_screenshot(page, "checkboxes_selected")

def test_checkbox_can_be_unchecked(login,page):
    page.reload()
    login.checkbox.first.click()
    #expect(login.checkbox.first).to_be_checked()
    login.checkbox.first.click()
    expect(login.checkbox.first).not_to_be_checked()    # edge: clicking a checked box unchecks it again

    #---- drop down ------
def test_first_dropdown(login):
    login.first_dropdown_select("usa")
    expect(login.dropdown_one).to_have_value("usa")
    expect(login.dropdown_one.locator("option:checked")).to_have_text("United States")

def test_second_dropdown(login):
    login.second_drop_select("green")
    expect(login.dropdown_two).to_have_value("green")
    expect(login.dropdown_two.locator("option:checked")).to_have_text("Green")

def test_second_dropdown_count(login):
    count = login.get_second_dropdown_options_count()
    logging.info(f"Number of options in dropdown: {count}")
    #print(f"Number of options in dropdown: {count}")
    assert count > 0, "dropdown should contain options"

    #----- date pickers-----
def test_first_calendar(dates):
    dates.choose_first_calendar("2025", "December", "14")
    actual_date = dates.start_date_picker.input_value()
    logging.info(f"first selected date is: {actual_date}")
    #print(f"selected date is: {actual_date}")
    expect(dates.start_date_picker).to_have_value(actual_date)

def test_second_calendar(dates):
    dates.choose_second_calendar("2025", "Dec", "18")
    actual_second_date = dates.end_date_picker.input_value()
    logging.info(f"second selected date is: {actual_second_date}")
    #print(f"second selected date is: {actual_second_date}")
    expect(dates.end_date_picker).to_have_value(actual_second_date)

def test_third_calendar(dates):
    dates.choose_start_tour("2025", "12", "11")
    selected_date3 = dates.third_date_picker.input_value()
    logging.info(f"third selected date is: {selected_date3}")
    #print(f"third selected date is: {selected_date3}")
    expect(dates.third_date_picker).to_have_value(selected_date3)

def test_fourth_calender(dates, page):
    dates.choose_end_tour("2025", "12", "16")
    selected_date4 = dates.fourth_date_picker.input_value()
    logging.info(f"forth selected date is: {selected_date4}")
    #print(f"forth selected date is: {selected_date4}")
    expect(dates.fourth_date_picker).to_have_value(selected_date4)
    take_screenshot(page, "dates_selected")

def test_submit_btn(dates):
    dates.submit_click()
    expect(dates.submit_btn).to_be_enabled()
    expect(dates.submit_btn).to_have_text("Submit")

def test_message_text(dates):
    message = dates.message_locate()
    print(message)
    expect(dates.message_txt).to_contain_text("You selected a range of 5 days.")

def test_negative_first_calendar_invalid_month(dates):
    success = dates.choose_first_calendar("2025", "Fakemonth", "14")
    assert not success, "Invalid month should not be selectable"

def test_negative_start_date_reject_invalid_date(dates, browser):
    browser_name = browser.browser_type.name
    dates.choose_start_tour("2026", "33", "07")
    value = dates.third_date_picker.input_value()
    if browser_name == "webkit":
        # Safari accepts invalid YYYY-MM-DD strings (known behavior)
        assert value == "" or value.startswith("2026-33"), "WebKit should store the invalid date string"
    else:
        assert value == "", "BUG: App accepted invalid start date"


def test_negative_end_date_reject_invalid_date(dates, browser):
    browser_name = browser.browser_type.name
    dates.choose_end_tour("2026", "15", "33")
    value = dates.fourth_date_picker.input_value()
    if browser_name == "webkit":
        # Safari accepts invalid YYYY-MM-DD strings (known behavior)
        assert value == "" or value == "2026-15-33", "WebKit should store the invalid date string"
    else:
        assert value == "", "BUG: App accepted invalid end date"

def test_books_row_count(tables):
    expect(tables.books_row()).to_have_count(7)

def test_books_column_count(tables):
    expect(tables.books_header()).to_have_count(4)

def test_books_header_list(tables):
    expected_header_list = ["BookName", "Author", "Subject", "Price"]
    extracted_header_list = tables.books_header_list()
    logging.info(f"books table header list: {extracted_header_list}")
    print(extracted_header_list)
    assert extracted_header_list == expected_header_list, \
        f"Expected header list: {expected_header_list} but got: {extracted_header_list}"

def test_books_author_name(tables):
    row = tables.books_row().filter(has_text="Master In Selenium")
    author_name = row.locator("td").nth(1)
    expect(author_name).to_have_text("Mukesh")

def test_negative_books_mismatch_author(tables):
    row = tables.books_row().filter(has_text="Master In Java")
    author_name = row.locator("td").nth(1).text_content()
    assert author_name != "Mukesh", f"Author should not be Mukesh, got {author_name}"

def test_negative_mismatch_book_name(tables):
    row = tables.books_row().filter(has_text="normal book")
    assert row.count() == 0, "Row should not exist for a normal book"

def test_performance_table_exist(tables):
    expect(tables.performance).to_be_visible()

def test_performance_row_exist(tables):
    row_text = tables.performance_row_text("Chrome").text_content()
    logging.info(f"performance table,row have chrome text: {row_text}")
    print(f"row text: {row_text}")
    expect(tables.performance_row_text("Chrome")).to_be_visible()

def test_performance_cell_values(tables):
    cell = tables.performance_cell_value("Chrome", "Memory (MB)")
    logging.info(f"performance table, Chrome Memory cell value is: {cell}")
    print(f"cell value is: {cell}")
    assert "MB" in cell, "cell value is not correct"

def test_performance_empty_cell(tables):
    cpu_cell = tables.performance_cell_value("Firefox", "CPU (%)")
    logging.info(f"performance table, Firefox CPU cell value is: {cpu_cell}")
    print(f"cell value is: {cpu_cell}")
    assert cpu_cell != "", "cell value is null"

def test_negative_performance_mismatch_row(tables):
    row = tables.performance_row_text("NonExist")
    assert row.count() == 0, "Row for NonExist should NOT exist"

def test_simple_alert(alerts):
    message = alerts.handle_simple_alert()
    logging.info(f"simple alert, message is: {message}")
    print(message)
    assert message == "I am an alert box!", f"Expected: I am an alert box! ,but got: {message}"

def test_confirmation_alert_accept(alerts, page):
    message = alerts.confirmation_alert_handle()
    logging.info(f"confirmation alert,message is: {message}")
    #self.page.wait_for_timeout(800)
    take_screenshot(page, "confirm_alert_text")
    print(message)
    assert message == "Press a button!", f"expected: Press a button!, but got {message}"
    expect(alerts.text_field).to_have_text("You pressed OK!")

def test_confirmation_alert_dismiss(alerts):
    message = alerts.confirmation_alert_handle(accept=False)
    print(message)
    assert message == "Press a button!", f"expected: Press a button!, but got {message}"
    expect(alerts.text_field).to_have_text("You pressed Cancel!")

def test_prompt_alert_accept(alerts, page):
    message = alerts.handle_prompt_alert()
    logging.info(f"prompt box message is: {message}")
    take_screenshot(page, "prompt_alert_text")
    print(message)
    assert message == "Please enter your name:", f"expected text: Please enter your name: , but got: {message}"
    expect(alerts.text_field).to_have_text("Hello Playwright! How are you today?")

def test_prompt_alert_dismiss(alerts):
    message = alerts.handle_prompt_alert(accept=False)
    print(message)
    assert message == "Please enter your name:", f"expected text: Please enter your name: , but got: {message}"
    expect(alerts.text_field).to_have_text("User cancelled the prompt.")


def test_negative_prompt_empty_input_with_accept(alerts):
    message = alerts.handle_prompt_alert(text_to_send="", accept=True)
    print(message)
    assert message == "Please enter your name:", f"Expected: Please enter your name:, but got: {message}"
    print(alerts.get_result())
    expect(alerts.text_field).to_have_text("User cancelled the prompt.")

def test_negative_prompt_dismiss_with_text(alerts):
    message = alerts.handle_prompt_alert(text_to_send="Engineer", accept=False)
    print(message)
    assert message == "Please enter your name:", f"Expected: Please enter your name:, but got: {message}"
    print(alerts.get_result())
    expect(alerts.text_field).to_have_text("User cancelled the prompt.")

#------hover ----
def test_hover_menu_is_visible_and_has_correct_text(hover):
    expect(hover.hover_me).to_be_visible()
    expect(hover.hover_me).to_have_text("Point Me")

def test_hover_reveals_submenu_items(hover, page):
    hover.hover()
    take_screenshot(page, "hover_options")
    expect(hover.hover_option_one).to_be_visible()
    expect(hover.hover_option_two).to_be_visible()
    expect(hover.hover_option_one).to_have_text("Mobiles")
    expect(hover.hover_option_two).to_have_text("Laptops")

def test_hover_option1_opens_link(hover, page):
    hover.hover()
    hover.hover_suboption_one()                          # negative: Mobiles link is broken (only adds #)
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/#")

def test_hover_option2_opens_link(hover, page):
    hover.hover()
    hover.hover_suboption_two()
    expect(page).to_have_title("Automation Testing Practice")   # negative: Laptops link is broken (only adds #)

def test_new_tab_button_link(hover,page):
    main_url = page.url  # main page URL
    new_tab = hover.open_new_tab()
    assert new_tab.url != main_url  #  must be different
    new_tab.close()

def test_new_tab_button_opens_broken_site(hover):
    new_tab = hover.open_new_tab()
    new_tab.wait_for_load_state("domcontentloaded", timeout=5000)
    url = new_tab.url
    assert "pavantestingtools.com" in url or "error" in url or url in ["", "about:blank", "blank"], f"Unexpected URL: {url}"
    new_tab.close()      # negative: New Tab opens error page

def test_popup_window(hover):
    popup = hover.open_new_window()
    popup.wait_for_url("https://www.selenium.dev/", timeout=5000)
    expect(popup).to_have_url("https://www.selenium.dev/")
    popup.close()

def test_popup_window_opens_selenium_site(hover, page):
    popup = hover.open_new_window()
    popup.wait_for_function("document.title.includes('Selenium')", timeout=5000)
    assert "Selenium" in popup.title()
    popup.close()



