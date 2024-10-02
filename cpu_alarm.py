import psutil
import time

alarms = []

current_alarm_threshold = None

def check_current_cpu_percentage():
    return psutil.cpu_percent(interval=1)

def trigger_alarm(threshold):
    global current_alarm_threshold

    if current_alarm_threshold is None or threshold > current_alarm_threshold:
        print(f"Alarm Triggered: {dict(alarms)[threshold]} at {threshold}% CPU usage!")
        current_alarm_threshold = threshold

def reset_alarm():
    global current_alarm_threshold
    current_alarm_threshold = None

def monitor_cpu():
    global current_alarm_threshold

    while True:
        cpu_usage = check_current_cpu_percentage()

        sorted_alarms = sorted(alarms, key=lambda x: x[0], reverse=True)

        triggered = False
        for threshold, message in sorted_alarms:
            if cpu_usage >= threshold:
                trigger_alarm(threshold)
                triggered = True
                break

        if not triggered and current_alarm_threshold is not None:
            reset_alarm()

        time.sleep(1)

def append_cpu_alarm(threshold, message):
    alarms.append((threshold, message))
    print(f"Alarm added: {message} at {threshold}%")
    time.sleep(1)