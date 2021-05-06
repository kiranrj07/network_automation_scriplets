#from paramiko import SSHClient
import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
#ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.103',port=22,username='student',password='root@123')

with SCPClient(ssh.get_transport()) as scp:
   scp.put('adduser.ps1', '/')
  # scp.get('test2.txt')