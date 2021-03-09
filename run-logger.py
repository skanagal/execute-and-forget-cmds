
import jsonrpclib
from jsonrpclib import Server
import asyncio


switch=Server("http://admin:admin@172.30.154.65/command-api")


def exec_and_forget_cmd(CMD):
    switch.runCmds( 1, [CMD+'&'])

def main():
    UID= input("Enter UID ")
    CMD='bash timeout 1000 python /mnt/flash/test.py ' + UID + ' "show tech-support"'
    print (CMD)
    exec_and_forget_cmd(CMD)

main()
