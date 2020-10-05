*** Settings ***
Documentation     Simple example for creating keyword resource.
Library    SeleniumLibrary
Resource    library.robot
Suite Setup    launch browser    https://www.amazon.in
Suite Teardown    custom_keywords.MyKeywords.close_browser

*** Variables ***
${WEBSITE URL}      https://www.amazon.in
${BROWSER}          Chrome

*** Test Cases ***

Select Category
    select_category    Mobiles, Computers    All Mobile Phones

Search item
    search item    Apple iphone XS

Select Brand
    select_brand    Apple

Save Screenshot and data
    save_screenshot
    write_to_file




