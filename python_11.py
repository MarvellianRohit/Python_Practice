class Device: 

    def __init__(self, device_name, hardware_power):
        self.device_name = device_name
        self.hardware_power = hardware_power

    def describe_device(self):
        print(f"{self.device_name} operates on {self.hardware_power} power!!")


class Laptop(Device):
    def set_os(self, operating_system):
        self.os = operating_system

    def boot_up(self):
        print(f"Booting up {self.device_name} running on {self.os}!")


my_workstation = Laptop("Macbook Pro" , "M3 Max")
my_workstation.describe_device()
my_workstation.set_os("macOS")
my_workstation.boot_up()
    