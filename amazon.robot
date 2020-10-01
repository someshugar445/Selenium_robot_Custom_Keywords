*** Settings ***
Documentation     Simple example for creating keyword resource.
Library    SeleniumLibrary
Resource    library.robot
Suite Setup    launch browser    https://www.amazon.in
Suite Teardown    custom_keywords.AmazonUI.close_browser

*** Variables ***
${WEBSITE URL}      https://www.amazon.in
${BROWSER}          Chrome

*** Test Cases ***

Select Category
    select_category    Mobiles, Computers    All Mobile Phones

Search item and get page details
    search item    iphoneX
    save_screenshot
    print_data









