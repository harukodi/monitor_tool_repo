import psutil as pul

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
