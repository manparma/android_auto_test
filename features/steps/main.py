from behave import *


@given(u'the user is on the home screen')
def step_impl(context):
    # print(context.__dict__)
    context.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Menu']").click()
    #context.driver.find_element_by_xpath('//android.widget.ImageView[contains(@index, "0")]').click()
    pass

