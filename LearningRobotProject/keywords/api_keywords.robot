*** Settings ***
Resource   RequestsLibrary

*** Keywords ***

Get API Response From Python Library
    [Arguments]    ${endpoint}
    ${response}=    Get API Response    ${endpoint}
    RETURN    ${response}
