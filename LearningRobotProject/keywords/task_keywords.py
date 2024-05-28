from libraries.TaskLibrary import Connector
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


def start_log_monitor(log_files, ip, username, password, multi_log="log_1"):
    # if not ip:
    #     ip = server.get("host")
    #     username = server.get("user")
    #     password = server.get("password")
    try:
        log_monitor_end_file_dict = {}
        for log_file in log_files.split(","):
            log_monitor_end_file_dict[log_file] = get_end_of_remote_file(log_file, ip, username, password)
            if log_monitor_end_file_dict[log_file] == 0:
                log_monitor_end_file_dict[log_file] = 1
        BuiltIn().set_test_variable("$monitor_log_end_of_file" + str(multi_log), log_monitor_end_file_dict)
        logger.info(f"Log Monitor started : {log_monitor_end_file_dict}")
    except Exception as e:
        return False


def stop_log_monitor(log_files, ip, username, password, multi_log="log_1"):
    # if not ip:
    #     ip = server.get("host")
    #     username = server.get("user")
    #     password = server.get("password")

    try:
        con = Connector.get_instance()
        log_monitor_end_file_dict = BuiltIn().get_variable_value("$monitor_log_end_of_file" + str(multi_log))
        result = {}
        for log_file in log_files.split(","):
            end_of_file = get_end_of_remote_file(log_file, ip, username, password)
            cmd = f'sed -n "{log_monitor_end_file_dict.get(log_file)},{end_of_file}p" {log_file}'
            logger.info("Command is", cmd)
            output, status = con.execute_command_remotely_and_verify(ip, username, password, cmd)
            result[log_file] = output

        return result
    except Exception as e:
        return False


def get_end_of_remote_file(filename, ip, username, password):
    con = Connector.get_instance()
    cmd = f'wc -l {filename}'
    output, status = con.execute_command_remotely_and_verify(ip, username, password, cmd)
    logger.info(f"Get end of line : {output}")
    output = output.decode("utf-8")
    if not status:
        logger.warn("End of remote file: command execution failed ")
        return 0
    try:
        end_of_file = int(output.split(' ')[0])
        return end_of_file
    except Exception:
        return 0
