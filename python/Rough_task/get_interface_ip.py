import os

interface = 'wlp0s20f3'

ip = os.popen("ip addr show "+interface).read().split("inet ")[1].split("brd")[0]

print(ip)
