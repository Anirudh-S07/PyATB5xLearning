class BaseTest:

    def open_browser(self):
        print("Starting the Browser")

    def close_browser(self):
        print("Close Browser")

    def read_from_excel(self):
        print("Read from Excel")


class TestCase1(BaseTest):

    def test1(self):
        self.open_browser()
        print("Test Case 1 Executed")
        self.close_browser()


class TestCase2(BaseTest):

    def test1(self):
        self.open_browser()
        print("Test Case 2 Executed")
        self.close_browser()

