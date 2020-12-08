import os

from appium import webdriver

class WebDriverFactory():
    def __init__(self,apptype):
        self.apptype=apptype

    def webDriverInstance(self,app_path):
        if self.apptype=="native":
            desired_caps={}
            desired_caps['platformName']='Android'
            desired_caps['platformVersion']='10'
            desired_caps['deviceName']='MyCell'
            desired_caps['app']=(os.getcwd()+ app_path)
            desired_caps['appPackage']='com.code2lead.kwad'
            desired_caps['appActivity']='com.code2lead.kwad.MainActivity'
            driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        else:
            print("No such apptype supported")
        return driver



