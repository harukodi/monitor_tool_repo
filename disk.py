import psutil as pul

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