import subprocess
import requests


def ping(hostname):
    # hostname = "192.168.0.103"

    for ip in hostname:
        output = subprocess.Popen(["ping.exe", ip], stdout=subprocess.PIPE).communicate()[0]

        if ('unreachable' in str(output)):
            sendMessage = "This IP " + ip + " is not responding please have a check. "
            bot_token = '1746736941:AAF47LodT67WPPVWo4tOQES6gJrbfdic7vE'
            bot_chatID = '1082782882'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + sendMessage
            response = requests.get(send_text)

            result = 'unreachable'

        elif ('timed out' in str(output)):
            sendMessage = "This " + ip + " is not responding please have a check: "
            bot_token = '1746736941:AAF47LodT67WPPVWo4tOQES6gJrbfdic7vE'
            bot_chatID = '1082782882'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + sendMessage
            response = requests.get(send_text)

            result = 'time-out'
        else:
            result = 'success'

        arr = output.split()
        print(str(arr[-1]).replace('b', ''))
        avg = str(arr[-1]).replace('b', '')
        #return result + avg


hostname = ["10.1.1.71", "10.1.1.82", "10.1.1.83", "10.1.1.84", "10.1.1.85", "10.1.1.86", "10.1.1.87", "10.1.1.88", "10.1.1.89", "10.1.1.90"]
data=ping(hostname)
print(data)