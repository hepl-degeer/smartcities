#Degeer Louis

import machine
import utime

button = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)

val = 0
LED_state = 0
flag = 0

def callback(button):
    global flag
    flag = 1
    
button.irq(trigger=button.IRQ_RISING, handler=callback)

while True:
    
    if flag == 1:
        val = val + 1
        flag = 0
    if val == 1:
        LED.value(1)
        utime.sleep(0.5)
        LED.value(0)
        utime.sleep(0.5)
    if val == 2:
        LED.value(1)
        utime.sleep(0.1)
        LED.value(0)
        utime.sleep(0.1)
    if val == 3:
        LED.value(0)
        val = 0
        utime.sleep(1)
    
    

    

        
