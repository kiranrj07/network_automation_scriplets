
# import os, sys
#
# fname="C:\\Users\tw360\PycharmProjects\whatsapp\venv\file.txt"

import subprocess
import requests
import sched, time
import csv

def ping(hostname):
    for ip in hostname:
        output = subprocess.Popen(["ping.exe", ip], stdout=subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(output)):
            sendMessage = "The IP " + ip + " is not responding please have a check. "
            bot_token = '1668189254:AAHrzyR0eEMiQ7bApgy0Ycgac3afZO9RiLI'
            bot_chatID = '1082782882'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + sendMessage
            response = requests.get(send_text)
            result = 'unreachable'

        elif ('timed out' in str(output)):
            sendMessage = "The IP " + ip + " is not responding please have a check: "
            bot_token = '1668189254:AAHrzyR0eEMiQ7bApgy0Ycgac3afZO9RiLI'
            bot_chatID = '1082782882'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + sendMessage
            response = requests.get(send_text)

            result = 'time-out'
        else:
            result = 'success'

        # arr = output.split()
        # print(str(arr[-1]).replace('b', ''))
        # avg = str(arr[-1]).replace('b', '')
        # return result + avg

s = sched.scheduler(time.time, time.sleep)

def do_something(sc):

    hostname=[]
    with open('ips.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            hostname.append(row[0].replace('ï»¿',''))

    ping(hostname)
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
