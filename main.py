import wmi

w = wmi.WMI()

def get_cpu_serial():
    for cpu in w.query("Select * FROM Win32_Processor"):
        print(F"CPU Serial Number: {cpu.ProcessorID}")

def get_gpu_serial():
    for gpu in w.query("SELECT * FROM Win32_VideoController"):
        print(f"GPU Serial Number: {gpu.PNPDeviceID}")
    
def get_ram_serial():
    for ram in w.query("SELECT * FROM Win32_PhysicalMemory"):
        print(f"RAM Serial Number: {ram.SerialNumber}")

def get_disk_serial():
    for disk in w.query("SELECT * FROM Win32_DiskDrive"):
        print(f"Disk Serial Number: {disk.SerialNumber}")
    
def get_motherboard_serial():
    for motherboard in w.query("SELECT * FROM Win32_BaseBoard"):
        print(f"Motherboard Serial Number: {motherboard.SerialNumber}")

def get_hw_id():

    for system in w.query("SELECT * FROM Win32_ComputerSystemProduct"):
        print(f"HWID (UUID): {system.UUID}")

def get_system_info():
    print("Hardware Information:\n")
    get_cpu_serial()
    get_gpu_serial()
    get_ram_serial()
    get_disk_serial()
    get_motherboard_serial()
    get_hw_id()

if __name__ == "__main__":
    get_system_info()
