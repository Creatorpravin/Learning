from re import S
from tkinter import E 

f = open("/etc/resolv.conf", "w")
f.write("# Generated by NetworkManager\nnameserver 127.0.0.53\nnameserver 8.8.8.8\n")

