import pdb
import unittest
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.contact_us_form_page import ContactUsFormPage
from pages.demo_home_page import AppiumDemoPage
from utilities.read_data import getYamlData

@pytest.mark.usefixtures("oneTimeSetUp")
class ContactUsFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.cuf= ContactUsFormPage(self.driver)
        self.adp=AppiumDemoPage(self.driver)
        self.test_data=(getYamlData(self.test_data_path,"appium_demo"))['contact_us_form']

    def test_contact_us_form(self):
        self.adp.wait_for_appium_demopage_to_load()
        self.adp.click_contact_us_form_button()
        self.cuf.wait_for_page_to_load()
        self.cuf.enter_name(self.test_data['name'])
        self.cuf.enter_address(self.test_data['address'])
        self.cuf.enter_email(self.test_data['email'])
        self.cuf.enter_mobile_num(self.test_data['mobile'])
        self.cuf.click_submit()
        assert self.cuf.get_saved_name().__contains__(self.test_data['name'])
        assert self.cuf.get_saved_password().__contains__(self.test_data['address'])
        assert self.cuf.get_saved_email().__contains__(self.test_data['email'])
        assert self.cuf.get_saved_mobile_num().__contains__(self.test_data['mobile'])





