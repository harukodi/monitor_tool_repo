import psutil as pul

class cpu:
    @staticmethod
    def get_cpu_usage(interval=1):
        return pul.cpu_percent(interval=interval)