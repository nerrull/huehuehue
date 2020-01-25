from qhue import Bridge, QhueException, create_new_username
import time
import random
from collections import deque

from algo import Circle


class HueController:
    BRIDGE_IP= '192.168.1.69'
    username="BOVln7LRExP7e--M3-R62PcMMyE8DDknQz3zecab"
    
    def __init__(self):
        self.bridge = Bridge(self.BRIDGE_IP, self.username)
        

    def setlight(self, lightid='14', on=True, hue=200, bri=128):
        self.bridge.lights[lightid].state(on=on)
        if on:
            self.bridge.lights[lightid].state(bri=bri, hue=hue)
    
    def setLightTemp(self, lightid, on=True,ct=300):
        self.bridge.lights[lightid].state(on=on)
        if on:
            self.bridge.lights[lightid].state(ct=ct);

    def listLights(self):
        lights = self.bridge.lights()
        for num, info in lights.items():
            if info["state"]["reachable"]:
                print("{:16} {}".format(info['name'], num))

if __name__=="__main__":        
    hc = HueController()
    hc.listLights()