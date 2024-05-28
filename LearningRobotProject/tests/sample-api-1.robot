*** Settings ***
Library     ../libraries/APILibrary.py

# **** Description ****
# The API Tests are being conducted on python requests module (Custom from Python)

*** Test Cases ***

Test API Response Using Python Request Module
    ${response}=    Get API Response    https://fake-json-api.mock.beeceptor.com/users
    Log   ${response.json()}
    Should Be Equal As Numbers    ${response.status_code}    200

