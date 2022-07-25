import psutil    

class DISK:
    partitions = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('C:\\')

    def show_disk_name(self):
        disk = []
        for partition in self.partitions:
                disk.append({'disk': partition.device})
        out = disk[0]
        return out

    def show_mount_point(self):
        mountpoint = []
        for partition in self.partitions:
                mountpoint.append({'mountpoint': partition.mountpoint})
        out = mountpoint[0]
        return out

    def show_file_system_type(self):
        file_system_type = []
        for partition in self.partitions:
                file_system_type.append({'file_system_type': partition.fstype})
        out = file_system_type[0]
        return out

    def show_total(self):
        total = disk_usage.total
        return total

    def show_used(self):
        used = disk_usage.used
        return used      

info_disk = DISK()

disk_usage = psutil.disk_usage('C:\\')
print(disk_usage.total)

disk_dict = [info_disk.show_disk_name(), info_disk.show_mount_point(), info_disk.show_file_system_type(),info_disk.show_total(),info_disk.show_used()]
print(disk_dict)

