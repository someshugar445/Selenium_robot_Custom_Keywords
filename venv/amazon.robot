*** Settings ***
Documentation     Simple example for creating keyword resource.
Library    SeleniumLibrary
Resource    library.robot
Test Setup    sample_login
Test Teardown    myfile.AmazonUI.close_browser

*** Variables ***
${WEBSITE URL}      https://www.amazon.in
${BROWSER}          Chrome

*** Test Cases ***
Open Test Website And Close Browser
#    select_category    Mobiles, Computers    All Mobile Phones
    search item    iphoneX
    select_brand    Apple
    select_screen    5.5
#    save_screenshot
    print_data







