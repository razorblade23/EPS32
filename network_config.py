import network
import picoweb
class ApConfig:
    def __init__(self, ssid: str, hidden: bool, authmode: int, password: str, max_clients: int) -> None:
        self.ssid = ssid
        self.hidden = hidden
        self.authmode = authmode
        self.password = password
        self.max_clients = max_clients
        self.initialize_ap()
        self.config_ap()
    
    def initialize_ap(self):
        self.ap = network.WLAN(network.AP_IF)
    
    def config_ap(self):
        self.ap.config(essid=self.ssid, hidden=self.hidden, authmode=self.authmode, password=self.password, max_clients=self.max_clients)
        #self.ap.ifconfig(('192.168.0.10', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    
    def toggle_ap(self, state: bool):
        self.ap.active(state)

    def show_info(self):
        print(self.ap.ifconfig())
        ip_adress, netmask, something, dns = self.ap.ifconfig()
        return ip_adress, netmask, something, dns

ap = ApConfig(ssid='SmartDarts', hidden=False, authmode=4, password='12345678', max_clients=8)

class ConnectToAp:
    def __init__(self, ssid, password) -> None:
        self.ssid = ssid
        self.password = password
    
    def connect(self):
        ssid = self.ssid
        password =  self.password
        
        self.station = network.WLAN(network.STA_IF)
        
        if self.station.isconnected() == True:
            print("Already connected")
            return
        
        self.station.active(True)
        self.station.connect(ssid, password)
        
        while self.station.isconnected() == False:
            pass
        
        print("Connection successful")
        print(self.station.ifconfig())
    
    def show_info(self):
        ip_adress, netmask, something, dns = self.station.ifconfig()
        return ip_adress, netmask, something, dns

samsung = ConnectToAp('Samsung', '12345678')



