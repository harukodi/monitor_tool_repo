import time

def fetch_current_time():
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

class logger:
    def __init__(self):
        self.logger = False
        self.current_time = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime())
        self.path = f"./log-{self.current_time}"
        if self.logger != True:
            print("logger has been disabled")
            time.sleep(1)
    
    def append_log(self, log_content):
        try:
            if self.logger == True:
                with open(self.path, "x") as file:
                    current_time = fetch_current_time()
                    file.write(f"{current_time}: {log_content}" + "\n")
                    
        except FileExistsError:
            if self.logger == True:
                with open(self.path, "a") as file:
                    current_time = fetch_current_time()
                    file.write(f"{current_time}: {log_content}" + "\n")
