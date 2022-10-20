from python_dependency_installer import PythonDependencyInstaller

if __name__ == "__main__":

    py_dep = PythonDependencyInstaller()

    from utility_manager import DeviceUtilityManager
    dev_utils = DeviceUtilityManager()

    print(dev_utils.get_interface_info())
    dev_utils.system_information_info()
    dev_utils.boot_time_info()
    dev_utils.cpu_info()
    dev_utils.disk_info()
    dev_utils.get_interface_info()
    dev_utils.io_statistics_info()
    dev_utils.memory_info()
    dev_utils.network_info()

    print("[+] Done")