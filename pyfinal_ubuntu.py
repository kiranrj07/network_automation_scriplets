import csv
import time
from netmiko import ConnectHandler


def CreatePod(ipaddress,podName,hostname,commands):
    try:
        def connectSSH(ipaddress):

                linux = {
                'device_type': 'linux',
                'ip': ipaddress,
                'username': 'root',
                'password': 'root@123',
                'port': 22,
                'verbose': True
                }

                connection = ConnectHandler(**linux)
                return connection
    except:
        print("error ConnercHandler")

    try:
        def executeCommand(cmd):
            print("Executing the cmd: ",cmd)
            output = connection.send_command(cmd + '\n')
            print(output+'\n')
            time.sleep(5)
    except:
        print("execption occured @ exwecuteCommand for command {}".cmd)


#Start of the execution
    try:
        connection = connectSSH(ipaddress)
        time.sleep(3)
    except:
        print("Connecting error @ {}".format(ipaddress))


    #Execute multiple commands
    cmds = commands.split("#")

    for i in cmds:
        try:
            print("These is the the command executing {}".format(i))
            executeCommand(i)
        except:
            print("Execute command error @ {}".format(i))

    # Add new user name
    try:
        adduCmd='adduser --disabled-password --shell /bin/bash --gecos {} {} \n'.format(podName,podName)
        print(adduCmd)
        output = connection.send_command(adduCmd)  #, expect_string=r'Enter new UNIX password: ')
        print(output)
    except:
        print("Execute command error @ adduser {} ".format(podName))


    #Set password for recently added pod
    try:
        passwd="usermod --password $(echo {} | openssl passwd -1 -stdin) {}".format("root@123",podName)
        output = connection.send_command(passwd)
        print(output)
    except:
        print("Execute command error @ passwd change for pod {}".format(podName))

    # sudo mode for user
    try:
        executeCommand('usermod -aG sudo {}'.format(podName))
    except:
        print("Execute command error @ usermod -aG sudo {}".format(podName))


    # Change hostname
    try:
        executeCommand('hostnamectl set-hostname {}'.format(hostname))
    except:
        print("Execute command hostname error @ {}".format(hostname))


    # Reboot to delete existing user
    try:
        executeCommand('reboot')
    except:
        print("reboot could not be executed, its normal error")

    try:
        connection.disconnect()
        time.sleep(5)
    except:
        print("Error dissconnecting ssh connection for {} ".format(podName))

    try:
        connection = connectSSH(ipaddress)
        time.sleep(5)
    except:
        print("Error making connection again for {}".format(podName))

    # delete existing user
    try:
        executeCommand('sudo deluser pod')
    except:
        print("Error deleting user for {}".format(podName))

    # Ending SSH Connecting at the end
    try:
        connection.disconnect()
        time.sleep(5)
    except:
        print("Ending the connection for pod @ {}".format(podName))


with open('python_doc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])
        print("\nStart of {} Task".format(line_count))
        print("################################################### \n ")
        CreatePod(row[0],row[1],row[2],row[3])
        line_count += 1
        print("End of task no {} executed successfully".format(line_count))
        print("################################################### \n\n")
        print("Task no {} executed successfully".format(line_count))