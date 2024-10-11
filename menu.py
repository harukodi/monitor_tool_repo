from disk import disk
from cpu import cpu
from ram import ram
from vars import refresh_interval_per_sec
from logger import logger
from cpu_alarm import append_cpu_alarm, cpu_alarms
from ram_alarm import append_ram_alarm, ram_alarms
from disk_alarm import append_disk_alarm, disk_alarms
import time, os, sys, platform, keyboard, msvcrt

logger_class = logger()

def monitor_render():
    try:
        def move_console_cursor_up(lines):
            sys.stdout.write(f"\033[{lines}A")
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
        while True:
            time.sleep(0.1)
            print("SYSTEM MONITOR")
            print("-" * 14)
            print(f"CPU: {cpu.get_cpu_usage()}%")
            print(f"RAM: Currently using {ram.get_ram_stats()['used']} GB of RAM out of {ram.get_ram_stats()['total']} GB available.")
            print(f"Currently using {disk.get_disk_stats()['used']} GB of disk space out of {disk.get_disk_stats()['total']} GB available, with {disk.get_disk_stats()['free']} GB free.")
            print("\nPress CTRL + C to go back")
            move_console_cursor_up(200)
    except KeyboardInterrupt:
        pass

def clear_console():
    os.system("cls")

def hide_console_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    
def show_console_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def wait_function_for_ctrl_c():
    try:
      while True:
          time.sleep(0.1)
    except KeyboardInterrupt:
      pass
    
def show_configured_alarms():
    if len(cpu_alarms) != 0 or len(ram_alarms) != 0 or len(disk_alarms) != 0:
        print("ALARMS")
        print("-" * 40)
        if len(cpu_alarms) != 0:
            for cpu_alarm in cpu_alarms:
                # Showing alarms for cpu where cpu_alarm[1] gets the name of the alarm and cpu_alarm[0] gets the threshold
                print(f"{cpu_alarm[1]}: {cpu_alarm[0]}%")
        if len(ram_alarms) != 0:
            for ram_alarm in ram_alarms:
                # Showing alarms for ram where ram_alarm[1] gets the name of the alarm and ram_alarm[0] gets the threshold
                print(f"{ram_alarm[1]}: {ram_alarm[0]}%")
        if len(disk_alarms) != 0:
            for disk_alarm in disk_alarms:
                # Showing alarms for ram where disk_alarm[1] gets the name of the alarm and disk_alarm[0] gets the threshold
                print(f"{disk_alarm[1]}: {disk_alarm[0]}%")
        print("-" * 40)
        print("Press CTRL + C to go back")
        wait_function_for_ctrl_c()
            
    if len(cpu_alarms) == 0 and len(ram_alarms) == 0 and len(disk_alarms) == 0:
        print("No alarms have been configured\nReturning to the main menu...")
        hide_console_cursor()
        time.sleep(2.2)

def alarm_selection():
    print("-" * 40)
    print("1: Add cpu alarm")
    print("2: Add ram alarm")
    print("3: Add disk alarm")
    print("-" * 40)
    print("Press CTRL + C to go back")
    try:
        input_selection_win = msvcrt.getch().decode('utf-8')
        if input_selection_win == "1":
            clear_console()
            show_console_cursor()
            cpu_threshold_input = int(input("CPU usage threshold 1-100: "))
            cpu_alarm_name = input("CPU alarm name: ")
            append_cpu_alarm(cpu_threshold_input, cpu_alarm_name)
            logger_class.append_log("cpu_alarm_added")
        elif input_selection_win == "2":
            clear_console()
            show_console_cursor()
            ram_threshold_input = int(input("RAM usage threshold 1-100: "))
            ram_alarm_name = input("RAM alarm name: ")
            append_ram_alarm(ram_threshold_input, ram_alarm_name)
            logger_class.append_log("ram_alarm_added")
        elif input_selection_win == "3":
            clear_console()
            show_console_cursor()
            disk_threshold_input = int(input("DISK usage threshold 1-100: "))
            disk_alarm_name = input("DISK alarm name: ")
            append_disk_alarm(disk_threshold_input, disk_alarm_name)
            logger_class.append_log("disk_alarm_added")
    except ValueError:
        clear_console()
        print("Must be a number between 1-100\nReturning to the main menu...")
        time.sleep(2.2)
    except KeyboardInterrupt:
        clear_console()
        
        
def menu_selections():
    global user_input
    clear_console()
    print("-" * 40)
    print("1: Start Monitoring")
    print("2: Add Alarms")
    print("3: Show Configured Alarms")
    print("4: Exit")
    print("-" * 40)
    print("\nPress ENTER to clear console.")
    hide_console_cursor()
    try:
        input_selection_win = msvcrt.getch().decode('utf-8')
        if input_selection_win == "1":
            clear_console()
            logger_class.append_log("MONITORING_STARTED")
            monitor_render()
                
        elif input_selection_win == "2":
            clear_console()
            alarm_selection()
        
        elif input_selection_win == "3":
            clear_console()
            show_configured_alarms()
    
        elif input_selection_win == "4":
            clear_console()
            logger_class.append_log("EXITED")
            exit()
    except UnicodeDecodeError:
        pass

def start_menu():
    while True:
        menu_selections()