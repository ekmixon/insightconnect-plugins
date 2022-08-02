import pexpect

import komand


class Cmd:
    def __init__(self, logger):
        self.logger = logger

    def call(self, command, password=None):
        """
        Calls a command. In case of any errors (exit code != 0) logs them and
        raises OSError. If password is given, waits for '[Pp]assword.*:' prompt
        and sends it to the command (the password is not logged).
        """
        self.logger.info(f"Call: Executing: {command}")

        try:
            if password:
                child = pexpect.spawn(command)
                child.delaybeforesend = None
                index = child.expect(["[Pp]assword.*: ", ".* done\."], timeout=30)
                if index == 0:
                    child.sendline(password)
                    self.logger.info("Call: Password entered")
                stdout = stderr = child.read().decode()
                exit_code = child.wait()
                child.close()
                self.logger.info(stdout)
            else:
                proc = komand.helper.exec_command(command)
                exit_code = proc["rcode"]
                stderr = proc["stderr"].decode()
                stdout = proc["stdout"].decode()
        except pexpect.exceptions.TIMEOUT:
            raise TimeoutError(
                f'Timeout occurred for "{command}". Please make sure that the Git repository is available and that the provided credentials are correct. If the issue persists, please contact Komand support'
            )

        except Exception as e:
            self.logger.error(f"Call: Unexpected exception: {str(e)}")
            raise e

        if exit_code != 0:
            raise OSError(
                f"Command execution failed: {command}\nExit code: {exit_code}\n{stderr}"
            )


        self.logger.info("Call: Command executed successfully")
        return stdout.rstrip()
