from menu import start_menu
from cpu_alarm import start_cpu_alarm_thread
from ram_alarm import start_ram_alarm_thread
if __name__ == "__main__":
    start_cpu_alarm_thread()
    start_ram_alarm_thread()
    start_menu()