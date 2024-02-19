import machine
from machine import ADC,Pin,PWM,I2C
import utime
import math


button = machine.Pin(18,machine.Pin.IN)
buzzer = PWM(Pin(27))
pot = ADC(0)
vol=1000

'''
do=1046
re=1175
mi=1318
fa=1397
so=1568
la=1760
si=1967
'''

def volume():
    val = pot.read_u16()
    #val = math.log10(val)
    return val
   
def do():
    buzzer.freq(1046)#DO
    buzzer.duty_u16(volume())
    volume()
def re():
    buzzer.freq(1175)#DO
    buzzer.duty_u16(volume())
    volume()
def mi():
    buzzer.freq(1318)#DO
    buzzer.duty_u16(volume())
    volume()
def fa():
    buzzer.freq(1397)#DO
    buzzer.duty_u16(volume())
    volume()
def so():
    buzzer.freq(1568)#DO
    buzzer.duty_u16(volume())
    volume()
def la():
    buzzer.freq(1760)#DO
    buzzer.duty_u16(volume())
    volume()
def si():
    buzzer.freq(1967)#DO
    buzzer.duty_u16(volume())
    volume()
def N():
    buzzer.duty_u16(0)


while True:


    do()
    utime.sleep(0.25)
    re()
    utime.sleep(0.25)
    mi()
    utime.sleep(0.25)
    N()
    utime.sleep(0.01)
    
    do()
    utime.sleep(0.25)
    re()
    utime.sleep(0.25)
    mi()
    utime.sleep(0.25)
    N()
    utime.sleep(0.01)
    
    do()
    utime.sleep(0.25)
    re()
    utime.sleep(0.25)
    mi()
    utime.sleep(0.25)
    do()
    utime.sleep(0.25)
    
    mi()
    utime.sleep(0.25)
    fa()
    utime.sleep(0.25)
    so()
    utime.sleep(0.5)
    
    mi()
    utime.sleep(0.25)
    fa()
    utime.sleep(0.25)
    so()
    utime.sleep(0.5)
    N()
    utime.sleep(0.01)
    
    so()
    utime.sleep(0.125)
    la()
    utime.sleep(0.125)
    so()
    utime.sleep(0.125)
    fa()
    utime.sleep(0.125)
    mi()
    utime.sleep(0.25)
    do()
    utime.sleep(0.25)
    
    so()
    utime.sleep(0.125)
    la()
    utime.sleep(0.125)
    so()
    utime.sleep(0.125)
    fa()
    utime.sleep(0.125)
    mi()
    utime.sleep(0.25)
    do()
    utime.sleep(0.25)
    
    re()
    utime.sleep(0.25)
    so()
    utime.sleep(0.25)
    do()
    utime.sleep(0.5)
    N()
    utime.sleep(0.01)
    
    re()
    utime.sleep(0.25)
    so()
    utime.sleep(0.25)
    do()
    utime.sleep(0.5)







    
    
    
    
    

    



