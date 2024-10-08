from disk import disk
from cpu import cpu
from ram import ram
from vars import refresh_interval_per_sec
from logger import logger
from cpu_alarm import append_cpu_alarm, cpu_alarms
from ram_alarm import append_ram_alarm, ram_alarms
import time, os, sys, platform, keyboard, msvcrt

logger_class = logger()

def monitor_render(refresh_interval):
    try:
        def move_console_cursor_up(lines):
            sys.stdout.write(f"\033[{lines}A")
            sys.stdout.flush()
        while True:
            time.sleep(refresh_interval)
            print(f"CPU: {cpu.get_cpu_usage()}%")
            print(f"RAM: Currently using {ram.get_ram_stats()['used']} GB of RAM out of {ram.get_ram_stats()['total']} GB available.")
            print(f"Currently using {disk.get_disk_stats()['used']} GB of disk space out of {disk.get_disk_stats()['total']} GB available, with {disk.get_disk_stats()['free']} GB free.")
            move_console_cursor_up(100)
    except KeyboardInterrupt:
        pass

def clear_console():
    os.system("cls")

def show_configured_alarms():
    try:
        if len(cpu_alarms) != 0 or len(cpu_alarms) != 0:
            print("Alarms")
            print("-" * 40)
            if len(cpu_alarms) != 0:
                for cpu_alarm in cpu_alarms:
                    # Showing alarms for cpu where cpu_alarm[1] gets the name of the alarm and cpu_alarm[0] gets the threshold
                    print(f"{cpu_alarm[1]}: {cpu_alarm[0]}%")
            if len(ram_alarms) != 0:
                for ram_alarm in ram_alarms:
                    # Showing alarms for ram where ram_alarm[1] gets the name of the alarm and ram_alarm[0] gets the threshold
                    print(f"{ram_alarm[1]}: {ram_alarm[0]}%")
            print("-" * 40)
            print("Press CTRL + C to go back")
            while True:
                try:
                  continue
                except KeyboardInterrupt:
                  pass
    except KeyboardInterrupt:
        pass
            
    if len(cpu_alarms) == 0 and len(ram_alarms) == 0:
        print("No alarms have been configured\nReturning to the main menu...")
        time.sleep(2.2)

def alarm_selection():
    print("-" * 40)
    print("1: Add cpu alarm")
    print("2: Add ram alarm")
    print("3: Add disk alarm")
    print("-" * 40)
    
    input_selection_win = msvcrt.getch().decode('utf-8')
    if input_selection_win == "1":
        clear_console()
        cpu_threshold_input = int(input("CPU threshold 1-100: "))
        cpu_alarm_name = input("CPU alarm name: ")
        append_cpu_alarm(cpu_threshold_input, cpu_alarm_name)
        logger_class.append_log("cpu_alarm_added")
    elif input_selection_win == "2":
        clear_console()
        ram_threshold_input = int(input("RAM threshold 1-100: "))
        ram_alarm_name = input("RAM alarm name: ")
        append_ram_alarm(ram_threshold_input, ram_alarm_name)
        logger_class.append_log("ram_alarm_added")
    elif input_selection_win == input_selection_win:
        print("Not an option\nReturning to the main menu...")
        time.sleep(2.2)
        
        
def menu_selections():
    global user_input
    clear_console()
    print("-" * 40)
    print("1. Start Monitoring")
    print("2. Add Alarms")
    print("3. Show Configured Alarms")
    print("5. Exit")
    print("-" * 40)
    print("\nPress ENTER to clear console.")

    input_selection_win = msvcrt.getch().decode('utf-8')
    if input_selection_win == "1":
        clear_console()
        logger_class.append_log("MONITORING_STARTED")
        monitor_render(refresh_interval_per_sec)
            
    elif input_selection_win == "2":
        clear_console()
        alarm_selection()
    
    elif input_selection_win == "3":
        clear_console()
        show_configured_alarms()

    elif input_selection_win == "5":
        clear_console()
        logger_class.append_log("EXITED")
        exit()

def start_menu():
    while True:
        menu_selections()