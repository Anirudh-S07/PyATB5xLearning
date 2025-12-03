# import OpenBrowser you cannot import the OpenBrowser from browserPackage python package like this
from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import close_browser
from Logs_Package import LogStart

# If you want to avoid package_name.module_name then in the __init__ folder specify which modules that
# you want the package to be easily accessed in the __all__ =[] list then you can import normally


def test_case():
    LogStart()
    start_browser()
    print("Hello Browser")
    close_browser()


test_case()

print("-----------")


class TestCaseExec:
    def test_case(self):
        start_browser()
        print("Hello Browser")
        close_browser()


obj = TestCaseExec()
obj.test_case()
