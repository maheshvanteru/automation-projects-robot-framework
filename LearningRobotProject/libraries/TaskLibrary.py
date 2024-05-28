import os
import time
import fnmatch
import paramiko
from stat import S_ISDIR
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

try:
    from scp import SCPClient
except ImportError:
    logger.warn("scpclient module is not available : scp opeartions through automation may not work !")


class Connector:
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("A Connector instance already exists")
        else:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.slave = paramiko.SSHClient()
            self.slave.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    @classmethod
    def get_instance(cls):
        """

        Returns: Connector class object

        """
        if cls.INSTANCE is None:
            cls.INSTANCE = Connector()
        return cls.INSTANCE

    def connect_to_remote_machine(self, ip, username, password):
        """

        Args:
            ip:
            username:
            password:

        Returns:
            ssh object

        """
        for i in range(5):
            try:
                self.client.get_host_keys().clear()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(ip, username=username, password=password, banner_timeout=60)
                break
            except Exception as e:
                logger.warn("SSH exception: going for retry. Retry Count - {0}, Error - {1}".format(i + 1, e))
                time.sleep(2)
                if i == 4:
                    self.client.close()
                    raise Exception("SSH to " + ip + " failed after 5 retries with error :: " + str(e))
        return self.client

    def execute_command_remotely_and_verify(self, ip, username, password, command, pty=True, timeout=600):
        """
        Execute the command in remote machine, get the output and execution status.
        Args:
            ip:
            username:
            password:
            command:
            pty:

        Returns: Tuple (<Output of execution> , <True/False>)

        """
        try:
            ssh_obj = self.connect_to_remote_machine(ip, username, password)
            stdin, stdout, stderr = ssh_obj.exec_command(command, get_pty=pty, timeout=timeout)
            output = stdout.read()
            status = stdout.channel.recv_exit_status()
            return output, True
        except Exception as e:
            self.close_ssh()
            return str(e), False

    def close_ssh(self):
        self.client.close()

    def sftp_walk(self, sftp, remotepath):
        path = remotepath
        files = []
        folders = []
        for f in sftp.listdir_attr(remotepath):
            if S_ISDIR(f.st_mode):
                folders.append(f.filename)
            else:
                # if
                files.append(f.filename)
        # print (path,folders,files)
        yield path, folders, files
        for folder in folders:
            new_path = remotepath + "/" + folder
            for x in self.sftp_walk(sftp, new_path):
                yield x

    def sftp_or_scp_file_copy_to_remote_linux(self, copy_protocol_obj, ip, local_path, remote_path, file_permission):
        status = True
        try:
            path_attr = copy_protocol_obj.stat(remote_path)
            if S_ISDIR(path_attr.st_mode):
                source_file_name = os.path.basename(local_path)
                dest_loc = remote_path + '/' + source_file_name
            else:
                dest_loc = remote_path
        except:
            dest_loc = remote_path
        try:
            copy_protocol_obj.put(local_path, dest_loc)
            if file_permission:
                copy_protocol_obj.chmod(dest_loc, file_permission)
            logger.info("Successfully copied the file {0} to {1} to server {2}".format(local_path, dest_loc, ip))
        except Exception as err:
            logger.warn("Failed to copy {0} to {1} of {2} due to {3}".format(local_path, dest_loc, ip, err))
            status = False
        copy_protocol_obj.close()
        self.client.close()
        return status

    def copy_file_to_linux(self, ip, username, password, local_path, remote_path, file_permission=None):
        """
        Copy a file from a local machine into a remote linux system
        Args:
            ip:
            username:
            password:
            local_path:
            remote_path:
            file_permission:

        Returns:

        """
        self.connect_to_remote_machine(ip, username, password)
        try:
            protocol_obj = self.client.open_sftp()
        except Exception as err:
            logger.warn("Failed to open sftp connection for {0} due to error :: {1}".format(ip, err))
            try:
                logger.info("File copy through sftp failed, trying to copy with scp")
                protocol_obj = SCPClient(self.client.get_transport())
            except Exception as err:
                BuiltIn().fail("Failed to open scp connection for {0} due to error :: {1}".format(ip, err))
        result = self.sftp_or_scp_file_copy_to_remote_linux(protocol_obj, ip, local_path, remote_path,
                                                            file_permission)
        return result

    def copy_folder_to_linux(self, ip, username, password, local_path, remote_path):
        """
        Copy a folder from a local machine into a remote linux system
        Args:
            ip:
            username:
            password:
            local_path:
            remote_path:
            file_permission:
        Returns:
        """
        self.connect_to_remote_machine(ip, username, password)
        scp = SCPClient(self.client.get_transport())
        scp.put(local_path, recursive=True, remote_path=remote_path)

    def check_for_remote_file_existence(self, ip, username, password, filename):
        self.connect_to_remote_machine(ip, username, password)
        try:
            sftp = self.client.open_sftp()
            logger.info(sftp.stat(filename))
            logger.info(f'SUCCESS..!! {filename} file exists in remote path. {ip}')
            return True
        except Exception as e:
            logger.error(f'FAILED..!! {filename} file does not exists in remote path. {ip}' + str(e))
            self.client.close()
            return False

    def copy_file_from_remote_to_local(self, ip, username, password, local_path, remote_path):
        try:
            if self.check_for_remote_file_existence(ip, username, password, filename=remote_path):
                sftp = self.connect_to_remote_machine(ip, username, password).open_sftp()
                sftp.get(localpath=local_path, remotepath=remote_path)
                logger.info(f'SUCCESS..!! file copied from remote: {remote_path} to local: {local_path}')
                return True
        except Exception as e:
            logger.info(f'FAILED..!! file copying failed from remote: {remote_path} to local: {local_path}')
            self.client.close()
            return False


if __name__ == '__main__':
    pass
