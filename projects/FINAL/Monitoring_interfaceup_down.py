import os
import psutil
import time
import json
import logging
from os import environ, getlogin
from psutil import virtual_memory, getloadavg
import requests as requests
import jsonpickle

print(psutil.net_if_stats())

def datainfo():  
       
    class NETWORK:
        def get_status(status: bool):
            return "Up" if status else "Down"

        def show_stat(self):
            net_stat = psutil.net_if_stats()
            net = []
            for key, value in net_stat.items():
                net.append({'interface': value.isup})
            out = net[0]
            return out

        def show_mtu(self):
            net_stat = psutil.net_if_stats()
            net = []
            for key, value in net_stat.items():
                net.append({'mtu': value.mtu})
            out = net[0]
            return out

    
    
    info_net = NETWORK()
    net_dict = [info_net.show_stat(), info_net.show_mtu(), info_net.get_status()]
    
    return net_dict


print(datainfo())


# do UP/Down вместо True/False