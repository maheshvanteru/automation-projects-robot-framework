*** Settings ***
Library     RequestsLibrary

# **** Description ****
# The API Tests are being conducted on Robot requests module (Built-In Robot Library)
# From behind, the built-in method is using already existing python module.

*** Test Cases ***

Test API Response Using Python Request Module
    Create Session    session    https://fake-json-api.mock.beeceptor.com
    ${response}    Get On Session    session    url=/users
    Log    ${response}
    Should Be Equal As Integers    ${response.status_code}    200

