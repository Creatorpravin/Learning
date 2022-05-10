import time

append = "nameserver 8.8.8.8\n"

time.sleep(2.4)

with open("/etc/resolv.conf", "a") as f:
    f.writelines(append)
