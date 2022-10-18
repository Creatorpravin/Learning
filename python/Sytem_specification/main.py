from python_dependency_installer import PythonDependencyInstaller

if __name__ == "__main__":

    py_dep = PythonDependencyInstaller()

    from utility_manager import DeviceUtilityManager
    dev_utils = DeviceUtilityManager()

    print(dev_utils.get_interface_info())

    print("[+] Done")