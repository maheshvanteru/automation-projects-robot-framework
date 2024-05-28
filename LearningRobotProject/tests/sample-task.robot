*** Settings ***
Resource    ../keywords/task_keywords.robot

# **** Description ****
# The API Tests are being conducted on Robot requests module (Built-In Robot Library)
# From behind, the built-in method is using already existing python module.

*** Variables ***
${SER_INSTALL_PATH}    /opt/Heal
${DATA_RECEIVER_SERV_IP}    192.168.12.32
${DATA_RECEIVER_SERV_USER}      root
${DATA_RECEIVER_SERV_PASSWORD}    auto@123


*** Test Cases ***

Monitor the Remote Logs
	[Tags]    SANITY
	${data_receiver_log}=   set variable    ${SER_INSTALL_PATH}/centralized_logs/${DATA_RECEIVER_SERV_IP}_DATARECEIVER_1/data-receiver.log
	Start Monitoring Log     ${data_receiver_log}      ${DATA_RECEIVER_SERV_IP}      ${DATA_RECEIVER_SERV_USER}      ${DATA_RECEIVER_SERV_PASSWORD}
    Sleep    10
    ${stop_log_monitor}=    Stop Monitoring Log     ${data_receiver_log}      ${DATA_RECEIVER_SERV_IP}      ${DATA_RECEIVER_SERV_USER}      ${DATA_RECEIVER_SERV_PASSWORD}
    Log    ${stop_log_monitor}
    ${LogOutput}=    Convert To String    ${stop_log_monitor}[${data_receiver_log}]
    should not contain    ${LogOutput}    ERROR


# #Generate from ChatGPT.
Verify If DR Log File Created
    ${file_path}=   Set Variable    ${SER_INSTALL_PATH}/centralized_logs/${DATA_RECEIVER_SERV_IP}_DATARECEIVER_1/data-receiver.log
    ${status}=   File Should Exist Remotely    ${file_path}    ${DATA_RECEIVER_SERV_IP}      ${DATA_RECEIVER_SERV_USER}      ${DATA_RECEIVER_SERV_PASSWORD}
    Should Be True    ${status}
