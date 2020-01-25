
from qhue import Bridge, QhueException, create_new_username
#from ipywidgets import interact, interactive, fixed
#import ipywidgets as widgets
import time
import random
from collections import deque

from algo import Circle


BRIDGE_IP= '192.168.1.69'
username="BOVln7LRExP7e--M3-R62PcMMyE8DDknQz3zecab"


hue_order= [5,7,8,6,9,1,3,2,4]

#hue_queue = deque(hue_order)
#hue_queue.rotate(3)

def setlight(lightid='14', on=True, hue=200, bri=128):
    bridge.lights[lightid].state(on=on)
    if on:
        bridge.lights[lightid].state(bri=bri, hue=hue)

if username is None:
    username = create_new_username(BRIDGE_IP)
    print("New user: {} . Put this in the username variable above.".format(username))

bridge = Bridge(BRIDGE_IP, username)
lights = bridge.lights()
for num, info in lights.items():
    print("{:16} {}".format(info['name'], num))

v = random.randint(0,255)


def work_lights():
    for light in hue_order:
        lightid=str(light)
        bridge.lights[lightid].state(on=True)

        bridge.lights[lightid].state( effect="none")
        bridge.lights[lightid].state( sat=15)
        bridge.lights[lightid].state( ct=315)

def shutdown():
    for light in hue_order:
        lightid=str(light)
        bridge.lights[lightid].state(on=False)


def auto_color_sweep():
    c = Circle( 9, epsilon=0.1, radius=0.15)
    lights = c.sweep(1)
    for index, light in enumerate(lights):
        x, y, b = light.getxyb()
        light_id = str(hue_order[index])
        bridge.lights[light_id].state(xy=[x, y], transitiontime=50)
        time.sleep(0.02)
        bridge.lights[light_id].state( effect="none")

    for index, light in enumerate(lights):
        light_id = str(hue_order[index])
        bridge.lights[light_id].state(effect="colorloop")


def run_sweep():
    c = Circle( 9, epsilon=0.1, radius=0.18)
    for i in range(1,1000):
        lights = c.sweep(i)
        for index, light in enumerate(lights):
            x,y,b = light.getxyb()
            light_id = str(hue_order[index])

            t = time.time()

            bridge.lights[light_id].state( xy=[x,y], transitiontime=50)

            t = time.time() - t
            print(t)
            time.sleep(1000)
        print(i)

shutdown()
#work_lights()
auto_color_sweep()