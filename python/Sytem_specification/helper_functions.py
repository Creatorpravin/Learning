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