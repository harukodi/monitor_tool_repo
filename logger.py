import time
class logger:
    def __init__(self):
        self.logger = True
        self.current_time = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime())
        self.path = f"./log-{self.current_time}"
        if self.logger != True:
            print("logger has been disabled")
    
    def append_log(self, log_content):
        try:
            if self.logger == True:
                with open(self.path, "x") as file:
                    file.write(log_content + "\n")
            else:
                pass
        except FileExistsError:
            if self.logger == True:
                with open(self.path, "a") as file:
                    file.write(log_content + "\n")
            else:
                pass


## Add time stamps for the log_content param in the append_log function