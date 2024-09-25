import psutil as pul

class cpu:
    @staticmethod
    def get_cpu_usage(interval=1):
        return pul.cpu_percent(interval=interval)

class ram: 
    @staticmethod
    def get_ram_stats():
        used_ram_in_gb = pul.virtual_memory().used / (1024 ** 3)
        total_system_ram = pul.virtual_memory().total / (1024 ** 3)
        total_system_ram_rounded = round(total_system_ram, 1)
        used_ram_in_gb_rounded = round(used_ram_in_gb, 1)
        return {
            'total': total_system_ram_rounded,
            'used': used_ram_in_gb_rounded
            }

class disk:
    @staticmethod
    def get_disk_stats():
        disk = pul.disk_usage('c:\\')
        total_disk_size_gb = disk.total / (1024 ** 3)
        used_disk_gb = disk.used / (1024 ** 3)
        free_disk_gb = disk.free / (1024 ** 3)
        total_disk_size_gb_rounded = round(total_disk_size_gb, 1)
        used_disk_gb_rounded = round(used_disk_gb, 1)
        free_disk_gb_rounded = round(free_disk_gb, 1)
        return {
            'total': total_disk_size_gb_rounded,
            'used': used_disk_gb_rounded,
            'free': free_disk_gb_rounded
            }
        
if __name__ == "__main__":
    print(f"CPU: {cpu.get_cpu_usage()}%")
    print(f"RAM: Currently using {ram.get_ram_stats()['used']} GB of RAM out of {ram.get_ram_stats()['total']} GB available.")
    print(f"Currently using {disk.get_disk_stats()['used']} GB of disk space out of {disk.get_disk_stats()['total']} GB available, with {disk.get_disk_stats()['free']} GB free.")