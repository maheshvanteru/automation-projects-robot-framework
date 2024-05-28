from SeleniumLibrary import SeleniumLibrary

class UILibrary(SeleniumLibrary):
    def custom_click(self, locator):
        self.click_element(locator)
