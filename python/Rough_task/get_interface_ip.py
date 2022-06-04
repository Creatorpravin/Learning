from asyncio import subprocess
import os
import subprocess

interface = 'wlp0s20f3'
cmd = "ip addr show "+interface


status = os.popen(cmd).read().split("state ")[1].split(" group")[0]

#print(status)

if status=="DOWN":
  print("Interface is",status)
else:
  ip = os.popen(cmd).read().split("inet ")[1].split("brd")[0]
  print(ip)

