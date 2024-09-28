from classes import cpu, ram, disk
from vars import refresh_interval_per_sec
from logger import logger
import time, os, sys, platform

def monitor_render(refresh_interval):
    def move_console_cursor_up(lines):
        sys.stdout.write(f"\033[{lines}A")
        sys.stdout.flush()
    
    time.sleep(refresh_interval)
    print(f"CPU: {cpu.get_cpu_usage()}%")
    print(f"RAM: Currently using {ram.get_ram_stats()['used']} GB of RAM out of {ram.get_ram_stats()['total']} GB available.")
    print(f"Currently using {disk.get_disk_stats()['used']} GB of disk space out of {disk.get_disk_stats()['total']} GB available, with {disk.get_disk_stats()['free']} GB free.")
    move_console_cursor_up(3)

def clear_console():
    os.system("cls")

if __name__ == "__main__":
    logger_class = logger()
    while True:
        clear_console()
        print("1: Start monitoring\nExit: exit")
        user_input = input(":")
        try:
            if int(user_input) == 1:
                clear_console()
                if platform.system() == "Windows":
                    logger_class.append_log("MONITORING_STARTED")
                    while True:
                        monitor_render(refresh_interval_per_sec)
                elif int(user_input) == 2:
                    print("pressed 2")
        except KeyboardInterrupt:
            clear_console()
            exit()
        except:
            if user_input.lower() == "exit":
                exit()
            else:
                pass