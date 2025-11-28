from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

class TablesPage:
    books_table = "[name='BookTable']"
    performance_table = "#taskTable"

    def __init__(self, page: Page):
        self.page = page
        self.books = page.locator(self.books_table)
        self.performance = page.locator(self.performance_table)

    #------BOOKS TABLE (static)----
    def books_row(self):
        return self.books.locator("tr")

    def books_header(self):
        th1 = self.books_row().first  ##--- .first will select first row ---# .last can also use to select las row
        return th1.locator("th")

    def books_header_count(self):
        return self.books_header().count()


    def books_header_list(self):
        header = []
        all = self.books_header()
        for i in range(self.books_header_count()):
            head = all.nth(i).text_content()   #--- to extract data from table cell use .text_content() always
            header.append(head)
        return header

    ##---- PERFORMANCE TABLE (dynamic) -----
    def performance_table_row(self):
        return self.performance.locator("tr")

    def performance_row_text(self,row_name):
        return self.performance.locator("tr", has_text=row_name)

    def performance_cell_value(self,row_name, cell_name):
        headers = self.performance_table_row().locator("th")
        index = None
        for i in range(headers.count()):
            text = headers.nth(i).text_content().strip()
            if text == cell_name:
                index = i
                break
        row = self.performance.locator("tr", has_text=row_name)
        column = row.locator("td")
        return column.nth(index).text_content()








