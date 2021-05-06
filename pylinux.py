import paramiko
import csv

def CreatePod(hostname,uname,passwd,commands):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=uname, password=passwd)
        print("Connected to %s" % hostname)
    except paramiko.AuthenticationException:
        print("Failed to connect to % s due to wrong username / password" % hostname)
        exit(1)
    except:
        print("Failed to connect to % s" % hostname)
        #exit(2)

    mcommands = commands.split("#")
    try:
        for cmd in mcommands:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n"
                  "  Executing the command: {} \n"
                  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%".format(cmd))
            stdin, stdout, stderr = ssh.exec_command(cmd)

            err = ''.join(stderr.readlines())
            out = ''.join(stdout.readlines())
            final_output = str(out) + str(err)

            print(err, out, final_output)

    except Exception as e:
            print(e.message)



with open('pywin_doc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1

    for row in csv_reader:
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])
        print("\nStart of {} Task".format(line_count))
        print("################################################### \n ")
        try:
            CreatePod(row[0],row[1],row[2],row[3])
        except:
            line_count += 1
            print("End of task no {} executed Unsuccessfully".format(line_count))
            print("################################################### \n\n")
            print("Task no {} executed Unsuccessfully \n".format(line_count))
        else:
            line_count += 1
            print("End of task no {} executed successfully".format(line_count))
            print("################################################### \n\n")
            print("Task no {} executed successfully \n".format(line_count))
