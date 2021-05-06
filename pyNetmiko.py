import time
from netmiko import ConnectHandler
import csv


with open('python_doc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[1])
        line_count += 1



def connectSSH(ipaddress):

    linux = {
            'device_type': 'linux',
            'ip': ipaddress,
            'username': 'root',
            'password': 'root@123',
            'port': 22,
            'verbose':True
            }
    connection = ConnectHandler(**linux)
    return connection
try:
    def executeCommand(cmd):
        output = connection.send_command(cmd+'\n')
        print(output)
except:
    print("execption occured")

def sendData(data):
    output = connection.enable(data+'\n')
    print(output)

ipaddress = '10.1.1.136'
connection = connectSSH(ipaddress)

#sample to check execute command
executeCommand('apt update')


#Add new user name
executeCommand('adduser pod6')
time.sleep(5)

#Send passwords
sendData('root@123')
sendData('root@123')

time.sleep(5)

#sudo mode for user
executeCommand('usermod -aG sudo pod1')
time.sleep(5)

#Change hostname
executeCommand('hostnamectl set-hostname pod1-python1')
time.sleep(10)


#Reboot to delete existing user
try:
    executeCommand('reboot')
except:
    print("reboot could not executed")
connection.disconnect()

time.sleep(20)

# #connect to ssh
# ssh_client.connect(hostname='10.1.1.136',username='root',password='root@123')
# print(stdout.readlines())
# print(stderr.readlines())
# time.sleep(5)

#disconnect once reboot started
#connection.disconnect()

#connect again after reboot
connection = connectSSH(ipaddress)

#delete existing user
executeCommand('sudo deluser user5\n')
time.sleep(5)
time.sleep(5)

connection.disconnect()