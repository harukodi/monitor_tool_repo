import psutil as pul
import time
import threading
import sys
ram_alarms = []

current_alarm_threshold = None
enable_ram_alarm = threading.Event()

def check_current_ram_percentage():
    return pul.virtual_memory().percent

def trigger_alarm(threshold):
    global current_alarm_threshold

    if current_alarm_threshold is None or threshold > current_alarm_threshold:
        print(f"\nAlarm Triggered: {dict(ram_alarms)[threshold]} at {threshold}% RAM usage!")
        current_alarm_threshold = threshold

def reset_alarm():
    global current_alarm_threshold
    current_alarm_threshold = None

def monitor_ram_alarm():
    global current_alarm_threshold, enable_ram_alarm
    while True:
        if enable_ram_alarm.is_set():
            ram_usage = check_current_ram_percentage()
            sorted_alarms = sorted(ram_alarms, key=lambda x: x[0], reverse=True)
            triggered = False
            
            for threshold, message in sorted_alarms:
                if ram_usage >= threshold:
                    trigger_alarm(threshold)
                    triggered = True
                    break
    
            if not triggered and current_alarm_threshold is not None:
                reset_alarm()
            time.sleep(1)
        else:
            time.sleep(1)
def append_ram_alarm(threshold, message):
    ram_alarms.append((threshold, message))
    print(f"Alarm added: {message} at {threshold}%")
    time.sleep(1.2)
    
def start_ram_alarm_thread():
    cpu_alarm_thread = threading.Thread(target=monitor_ram_alarm, daemon=True)
    cpu_alarm_thread.start()