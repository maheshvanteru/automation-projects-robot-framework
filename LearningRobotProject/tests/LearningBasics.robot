*** Settings ***
Library    Collections

*** Variables ***

# *** Scaler variables ***

# Defined in the *** Variables *** section with a $ sign.
# Accessed in test cases using ${VARIABLE_NAME} syntax.

${USERNAME}         testuser
${PASSWORD}         password123
${URL}              https://example.com

# *** List Variables ***

# List is just like an Array in python but fact that it can hold any datatype.
# Defined with an @ sign.
# Accessed using the index notation @{VARIABLE_NAME}[index].

@{USER_CREDENTIALS}    testuser    password123    admin   2.0

# *** Dictionary Variables ***
# Defined with a & sign.
# Accessed using the key notation &{VARIABLE_NAME}[key].

&{USER_INFO}        username=testuser    password=password123    role=admin

# Built-In methods on variables.

# https://robotframework.org/robotframework/latest/libraries/Collections.html


*** Test Cases ***

Lets Start with Print Statement
    Log  Hello World
    Log To Console    Hello World on Console



Example Scalar Variable
    [Documentation]    This test case demonstrates the use of scalar variables.
    Log    Username is ${USERNAME}
    Log    Password is ${PASSWORD}
    Log    URL is ${URL}



Example List Variable
    [Documentation]    This test case demonstrates the use of list variables.
    Log    Username is ${USER_CREDENTIALS}[0]
    Log    Password is ${USER_CREDENTIALS}[1]
    Log    Role is ${USER_CREDENTIALS}[2]
    
    # Built-in methods on List/array
    Append To List    ${USER_CREDENTIALS}    Linux
    Log   ${USER_CREDENTIALS}

    ${username_from_list}=   Get From List    ${USER_CREDENTIALS}   0
    Log   ${username_from_list}



Example Dictionary Variable
    [Documentation]    This test case demonstrates the use of dictionary variables.
    Log    Username is ${USER_INFO}[username]
    Log    Password is ${USER_INFO}[password]
    Log    Role is ${USER_INFO}[role]

    # Built-in methods on Dictionary
    Set To Dictionary    ${USER_INFO}    email=testuser@example.com
    Log    ${USER_INFO}

    ${password_from_dict}=   Get From Dictionary    ${USER_INFO}    password
    Log   Password from dictionary is ${password_from_dict}

