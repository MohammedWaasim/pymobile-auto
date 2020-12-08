from base.basepage import BasePage


class ContactUsFormPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _page_title=("Contact Us form","text")
    _name_field="com.code2lead.kwad:id/Et2"
    _email_filed="com.code2lead.kwad:id/Et3"
    _address_field="com.code2lead.kwad:id/Et6"
    _mobile_num_filed="com.code2lead.kwad:id/Et7"
    _submit_button="com.code2lead.kwad:id/Btn2"
    _saved_name = "com.code2lead.kwad:id/Tv2"
    _saved_email = "com.code2lead.kwad:id/Tv7"
    _saved_password = "com.code2lead.kwad:id/Tv5" #currently this is displayed as password instead of address
    _saved_mobile_num = "com.code2lead.kwad:id/Tv6"

    def wait_for_page_to_load(self):
        self.waitForElement(*(self._page_title))

    def enter_name(self,value):
        self.enterText(value,self._name_field)

    def enter_email(self,value):
        self.enterText(value,self._email_filed)

    def enter_address(self,value):
        self.enterText(value,self._address_field)

    def enter_mobile_num(self,value):
        self.enterText(value,self._mobile_num_filed)

    def click_submit(self):
        self.clickElement(self._submit_button)

    def get_saved_name(self):
        return self.getElement(self._saved_name).text

    def get_saved_email(self):
        return self.getElement(self._saved_email).text

    def get_saved_password(self):
        return self.getElement(self._saved_password).text

    def get_saved_mobile_num(self):
        return self.getElement(self._saved_mobile_num).text

