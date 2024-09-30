import psutil
import time

alarms = [
    (20, "Low CPU Alarm"),
    (30, "Medium CPU Alarm"),
    (50, "High CPU Alarm"),
    (70, "Critical CPU Alarm")
]

current_alarm_threshold = None

def check_current_cpu_percentage():
    return psutil.cpu_percent(interval=1)  # Returns CPU usage over 1 second

def trigger_alarm(threshold):
    global current_alarm_threshold

    if current_alarm_threshold is None or threshold > current_alarm_threshold:
        print(f"Alarm Triggered: {dict(alarms)[threshold]} at {threshold}% CPU usage!")
        current_alarm_threshold = threshold

def reset_alarm():
    global current_alarm_threshold
    print("CPU usage dropped below all thresholds. Resetting alarms.")
    current_alarm_threshold = None

def monitor_cpu():
    global current_alarm_threshold

    while True:
        cpu_usage = check_current_cpu_percentage()
        print(f"Current CPU Usage: {cpu_usage}%")

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

def append_alarm(threshold, message):
    alarms.append((threshold, message))
    print(f"Alarm added: {message} at {threshold}%")

# Example usage: append a new alarm
append_alarm(90, "Critical High CPU Alarm")

# Start monitoring CPU usage
monitor_cpu()
