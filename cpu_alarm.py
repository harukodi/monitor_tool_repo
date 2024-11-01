import psutil
import time
import threading
import sys

cpu_alarms = []
current_alarm_threshold = None
enable_cpu_alarm = threading.Event()

def check_current_cpu_percentage():
    return psutil.cpu_percent(interval=1)

def trigger_alarm(threshold):
    global current_alarm_threshold

    if current_alarm_threshold is None or threshold > current_alarm_threshold:
        print(f"\nAlarm Triggered: {dict(cpu_alarms)[threshold]} at {threshold}% CPU usage!")
        current_alarm_threshold = threshold

def reset_alarm():
    global current_alarm_threshold
    current_alarm_threshold = None

def monitor_cpu_alarm():
    global current_alarm_threshold

    while True:
        if enable_cpu_alarm.is_set():
            cpu_usage = check_current_cpu_percentage()
            sorted_alarms = sorted(cpu_alarms, key=lambda x: x[0], reverse=True)
            triggered = False
            
            for threshold, message in sorted_alarms:
                if cpu_usage >= threshold:
                    trigger_alarm(threshold)
                    triggered = True
                    break
    
            if not triggered and current_alarm_threshold is not None:
                reset_alarm()
    
            time.sleep(1)
        else:
            time.sleep(1)

def append_cpu_alarm(threshold, message):
    cpu_alarms.append((threshold, message))
    print(f"Alarm added: {message} at {threshold}%")
    time.sleep(1.2)
    
def start_cpu_alarm_thread():
    cpu_alarm_thread = threading.Thread(target=monitor_cpu_alarm, daemon=True)
    cpu_alarm_thread.start()