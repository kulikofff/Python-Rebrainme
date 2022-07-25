from turtle import up
import psutil    

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
net_stat = (info_net.show_stat())
mtu = (info_net.show_mtu())

print(net_stat)
print(mtu)

for value in net_stat:
    if value == 'True':
        print('ok')
    else:
        value = 'test'
        print(value)    

