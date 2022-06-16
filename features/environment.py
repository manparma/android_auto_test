import os
import time
from behave import *
from appium import webdriver
from selenium.webdriver.common import desired_capabilities


def before_feature(context, feature):

    # print(context.__dict__)
    # context.driver.install_app('/manishparmar/PycharmProjects/android_auto_test/data/app/hGn899QrHN_Test.apk');

    # targetapp = context.config.userdata["app"]
    # app = os.path.join(os.path.dirname(__file__),
    #                    '../../.'
    #                    './data/app/',
    #                    targetapp)
    # app = os.path.abspath(app)

    """
    *******************************************************************
    Appium driver properties
    *******************************************************************
    """

    #context.driver = webdriver.Chrome(
        #command_executor=context.appiumaddress,
    desired_capabilities={
        #'app': app,                                              # use to install the app
        "automationName": "uiautomator2",
        'appPackage': '',            # use to start a previously installed app
        #'appActivity': '',  # use to start a previously installed app
        'appActivity': '',  # use to start a previously installed app
        # 'fullReset': 'false',                                  # use to start a previously installed app
        'noReset': 'true',                                       # required for background/foreground.
        'platformName': 'Android',
        'platformVersion': '11',
        'clearDeviceLogsOnStart': 'true',
        'deviceName': '17101JECB11994',                                # serial of device - 17101JECB11994
        # 'autoGrantPermissions': 'true',
        'unlockType': 'pin',
        'unlockKey': '0000'
    }
    context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                      desired_capabilities=desired_capabilities)
    context.driver.reset()


