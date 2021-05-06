import time
# import csv
#
# with open('python_doc.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row[1])
    #     if line_count == 0:
    #
    #         line_count += 1
    #     else:
    #
    #         line_count += 1
    # print(f'Processed {line_count} lines.')


import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.1.1.136',username='root',password='root@123')


#sample to check execute command
stdin,stdout,stderr=ssh_client.exec_command('ls\n')
print(stdout.readlines())
print(stderr.readlines())

#Add new user name
stdin,stdout,stderr=ssh_client.exec_command('adduser pod1\n')
time.sleep(5)
stdin.write('root@123\n')
stdin.write('root@123\n')
print(stdout.readlines())
print(stderr.readlines())

time.sleep(5)
#sudo mode for user
stdin,stdout,stderr=ssh_client.exec_command('usermod -aG sudo pod1\n')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(5)

#Change hostname
stdin,stdout,stderr=ssh_client.exec_command('hostnamectl set-hostname pod1-python1\n')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(5)

#Reboot to delete existing user
stdin,stdout,stderr=ssh_client.exec_command('reboot\n')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(15)

#connect to ssh
ssh_client.connect(hostname='10.1.1.136',username='root',password='root@123')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(5)

#delete existing user
stdin,stdout,stderr=ssh_client.exec_command('sudo deluser user5\n')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(5)

#remove existing files
stdin,stdout,stderr=ssh_client.exec_command('sudo rm -r /home/user5\n')
print(stdout.readlines())
print(stderr.readlines())
time.sleep(5)

#Installing packages if any
stdin,stdout,stderr=ssh_client.exec_command('apt update\n')
print(stdout.readlines())
print(stderr.readlines())
# #Reboot after deletetions
# stdin,stdout,stderr=ssh_client.exec_command('reboot\n')
#
# #login user
# ssh_client.connect(hostname='10.1.1.136',username='root',password='root@123')



#print(stdin.readlines())
print(stdout.readlines())
print(stderr.readlines())




