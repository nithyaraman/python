#!usr/bin/python
import paramiko
import socket
import time

def paramiko_config() :
    try :
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect("192.168.100.233", port = 22,username ="v170",
                    password ="pwd", timeout =10.0,pkey = None)
        print "connected"
        connection = ssh.invoke_shell()
        connection.send("ls" +"\n"+ "ls"+"\n")
        connection.send("ls" +"\n"+ "ls"+"\n")
        time.sleep(1)
        print connection.recv(9999)

    except paramiko.SSHException :
        print "ssh failed"
    except socket.error :
        print "ssh failed"

        ssh.close()
paramiko_config()

