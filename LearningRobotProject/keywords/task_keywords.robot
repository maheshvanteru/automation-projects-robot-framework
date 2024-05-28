*** Settings ***
Library    ../keywords/task_keywords.py
Library    SSHLibrary

*** Keywords ***

Execute Command Remotely And Return
    [Arguments]    ${command}    ${ip}    ${user_name}    ${password}
    [Documentation]    Establishes a SSH connection to the target and returns the output of the command.
    SSHLibrary.Open Connection    ${ip}    timeout=5
    SSHLibrary.Login    ${user_name}    ${password}
    Log    Loggged into ${ip} machine Successfully
    ${result}=    SSHLibrary.Execute Command    ${command}
    log    ${result}
    SSHLibrary.Close Connection
    RETURN    ${result}

Stop Monitoring Log
    [Documentation]    Ex. start log monitor in dr
    ...    This keyword takes four argument
    ...    filename: Data Receiver log file name
    ...    ip: ip of the server
    ...    username: username of the server
    ...    password: password of the server
    [Arguments]     ${log_files}    ${ip}  ${username}  ${password}    ${multiLog}=log_1
    ${stop_log_monitor}=      Stop Log Monitor    ${log_files}   ${ip}  ${username}  ${password}   ${multiLog}
    RETURN    ${stop_log_monitor}

Start Monitoring Log
    [Documentation]    Ex. start log monitor in dr
    ...    This keyword takes four argument
    ...    filename: Data Receiver log file name
    ...    ip: ip of the server
    ...    username: username of the server
    ...    password: password of the server
    [Arguments]     ${log_files}    ${ip}  ${username}  ${password}   ${multiLog}=log_1
    ${Start_Log _Monitor}=  Start Log Monitor    ${log_files}   ${ip}  ${username}  ${password}   ${multiLog}
    RETURN    ${Start_Log _Monitor}

File Should Exist Remotely
    [Arguments]    ${file_path}    ${ip}    ${user_name}    ${password}
    [Documentation]    Validates if a file exists on the remote machine. Returns True if the file exists, False otherwise.
    ${command}    Set Variable    [ -f ${file_path} ] && echo True || echo False
    ${result}=    Execute Command Remotely And Return    ${command}    ${ip}    ${user_name}    ${password}
    RETURN    ${result}

#Check If File Exists On Remote Machine
#    [Arguments]    ${file_path}    ${ip}    ${user_name}    ${password}
#    [Documentation]    Checks if a file exists on the remote machine.
#    ${command}=   Set Variable    test -f ${file_path} && echo "File exists" || echo "File does not exist"
#    ${result}=    Execute Command Remotely And Return    ${command}    ${ip}    ${user_name}    ${password}
#    Log    Command output: ${result}
#    ${file_exists}=    Run Keyword And Return Status    Should Contain    ${result}    File exists
#    RETURN    ${file_exists}
