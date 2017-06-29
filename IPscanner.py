
from socket import *
import json

with open('config.conf') as json_data_file:
    config = json.load(json_data_file)

ip_list = []

def start():

    for ip in range(0, 256):

        targetIP = gethostbyname(config["IPscanner"]["start_ip"] + str(ip))

        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.01)
        result = s.connect_ex((targetIP, config["IPscanner"]["port"]))

        if(result == 0) :

            ip_list.append([config["IPscanner"]["start_ip"] + str(ip), str(config["IPscanner"]["port"])])

        s.close()

    return ip_list



print start()
