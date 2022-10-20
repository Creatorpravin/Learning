from python_dependency_installer import PythonDependencyInstaller

if __name__ == "__main__":

    py_dep = PythonDependencyInstaller()

    from utility_manager import DeviceUtilityManager
    dev_utils = DeviceUtilityManager()

    system_information = dev_utils.system_information_info()
    boot_time = dev_utils.boot_time_info()
    cpu_information = dev_utils.cpu_info()
    disk_information = dev_utils.disk_info()
    interface_information = dev_utils.get_interface_info()
    io_statistics_information = dev_utils.io_statistics_info()
    memory_information = dev_utils.memory_info()
    network_information = dev_utils.network_info()

    #print(dev_utils.get_interface_info())
    print(system_information.system)
    # dev_utils.system_information_info()
    # dev_utils.boot_time_info()
    # dev_utils.cpu_info()
    # dev_utils.disk_info()
    # dev_utils.get_interface_info()
    # dev_utils.io_statistics_info()
    # dev_utils.memory_info()
    # dev_utils.network_info()

    print("[+] Done")