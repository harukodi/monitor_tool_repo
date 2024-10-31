import psutil as pul
import time
import threading
from disk import disk
import sys
disk_alarms = []

current_alarm_threshold = None
enable_disk_alarm = False

def check_current_disk_percentage():
    return disk.get_disk_stats()['percent']

def trigger_alarm(threshold):
    global current_alarm_threshold

    if current_alarm_threshold is None or threshold > current_alarm_threshold:
        print(f"\nAlarm Triggered: {dict(disk_alarms)[threshold]} at {threshold}% DISK usage!")
        current_alarm_threshold = threshold

def reset_alarm():
    global current_alarm_threshold
    current_alarm_threshold = None

def monitor_disk_alarm():
    global current_alarm_threshold
    while True:
        if enable_disk_alarm == True:
            disk_usage = check_current_disk_percentage()
            sorted_alarms = sorted(disk_alarms, key=lambda x: x[0], reverse=True)
            triggered = False
            
            for threshold, message in sorted_alarms:
                if disk_usage >= threshold:
                    trigger_alarm(threshold)
                    triggered = True
                    break
    
            if not triggered and current_alarm_threshold is not None:
                reset_alarm()

            time.sleep(1)
        else: 
            time.sleep(1)

def append_disk_alarm(threshold, message):
    disk_alarms.append((threshold, message))
    print(f"Alarm added: {message} at {threshold}%")
    time.sleep(1.2)
    
def start_disk_alarm_thread():
    cpu_alarm_thread = threading.Thread(target=monitor_disk_alarm, daemon=True)
    cpu_alarm_thread.start()