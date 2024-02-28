from lcd1602 import LCD1602
import dht
from machine import I2C,Pin,ADC,PWM
from utime import sleep
import time

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
dht = dht.DHT11(Pin(18))
buzzer = PWM(Pin(16))
LED = Pin(20, Pin.OUT)
pot = ADC(0)

def VERT():
    buzzer.duty_u16(0)
    LED.value(0)
    d.clear()
    d.setCursor(0,0)
    d.print("Set:"+str(round(y)))
    d.setCursor(0,1)
    d.print("Ambient:"+str(temp))
    sleep(1)

def JAUNE():
    LED.value(1)
    sleep(0.5)
    LED.value(0)
    d.clear()
    d.setCursor(0,0)
    d.print("Set:"+str(round(y)))
    d.setCursor(0,1)
    d.print("Ambient:"+str(temp))
    
    
def ALARM():
    LED.value(1)
    sleep(0.1)
    LED.value(0)
    buzzer.freq(1000)
    buzzer.duty_u16(1000)
    d.clear()
    d.setCursor(0,0)
    d.print("ALARM")
    sleep(0.5)
    d.clear()
    sleep(0.5)
    

while True:
    
    
    y = ((-20)/(65000))*pot.read_u16() + 35      
    dht.measure()
    temp = dht.temperature()
    sleep(1)
    

    if temp <= y:
        VERT()
    if temp > y and temp <= (y + 3):
        JAUNE()
    if temp > (y + 3):
        ALARM()

        
