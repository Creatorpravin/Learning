import psutil

class DeviceUtilityManager():
    def __init__(self):
        print("[+] Device Utility Manager Initialization Starts")
        print("[+] Device Utility Manager Initialization Ends")
    
    def get_interface_info(self):
        return psutil.net_if_addrs()