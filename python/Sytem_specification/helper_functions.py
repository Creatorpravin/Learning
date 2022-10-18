import subprocess


def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, shell=True)

        if result.returncode == 0:
            print("[+] {} - executed successfully".format(command))
            return (result.stdout).decode("utf-8"), True

    except Exception as exceptions:
        print("[-] ---- Failed --- {}".format(exceptions))
        return result.stderr, False
    
    return result.stderr, False

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"  # Get last two decimal pointss
        bytes /= factor