from disk import disk
from cpu import cpu
from ram import ram
from vars import refresh_interval_per_sec
from logger import logger
import time, os, sys, platform

logger_class = logger()

def monitor_render(refresh_interval):
    def move_console_cursor_up(lines):
        sys.stdout.write(f"\033[{lines}A")
        sys.stdout.flush()
    
    time.sleep(refresh_interval)
    print(f"CPU: {cpu.get_cpu_usage()}%")
    print(f"RAM: Currently using {ram.get_ram_stats()['used']} GB of RAM out of {ram.get_ram_stats()['total']} GB available.")
    print(f"Currently using {disk.get_disk_stats()['used']} GB of disk space out of {disk.get_disk_stats()['total']} GB available, with {disk.get_disk_stats()['free']} GB free.")
    move_console_cursor_up(100)

def clear_console():
    os.system("cls")

def alarm_selection():
    print("1: Add cpu alarm")
    print("2: Add disk alarm")
    print("3: Add ram alarm")
    alarm_input_type = input("Alarm selection: ")
    if int(alarm_input_type) == 1:
        logger_class.append_log("CPU ALARM ADDED")
        
def menu_selections():
    global user_input
    clear_console()
    print("1: Start monitoring")
    print("2: Add Alarms")
    print("Exit: Exit")
    user_input = input("Selection: ")
    if int(user_input) == 1:
        clear_console()
        logger_class.append_log("MONITORING_STARTED")
        while True:
            monitor_render(refresh_interval_per_sec)
    elif int(user_input) == 2:
        clear_console()
        alarm_selection()

def start_menu():
    time.sleep(1)
    while True:
        try:
            menu_selections()
        except KeyboardInterrupt:
            clear_console()
            logger_class.append_log("EXITED")
            exit()
        except:
            if user_input.lower() == "exit":
                logger_class.append_log("EXITED")
                exit()