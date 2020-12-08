from base.basepage import BasePage

class AppiumDemoPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _appium_demo_title = ("Appium Demo", "text")
    _contact_us_form_button = "com.code2lead.kwad:id/ContactUs"

    def click_contact_us_form_button(self):
        self.clickElement(self._contact_us_form_button)

    def wait_for_appium_demopage_to_load(self):
        self.waitForElement(*(self._appium_demo_title))
