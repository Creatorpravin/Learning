import socket

def get_remote_machine_info(remote_host):
    try:
        print("IP ADDRESS", socket.gethostbyname(remote_host))
    except socket.error:
        print(remote_host, socket.error)
    
if __name__ == "__main__":
    get_remote_machine_info("dev.chiefnet.yavar.in")