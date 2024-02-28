# Exercice 3: Volume d'une mélodie
## Objectif: 
Créer un programme MicroPython qui permet de gérer un thermostat à plusieurs états.
## Matériel:
- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module capteur température/humidité
- Module LED
- Module potentiomètre
- Module écran LCD
- Module Buzzer
- Câbles
## Consignes:

1. Développez un programme en MicroPython sur le Raspberry Pico W pour:
   - Lire la valeur de la résistance variable et la convertir en une température de consigne dans une plage de 15°C à 35°C.
   - Lire la température mesurée par le capteur toutes les secondes environ.
   - Comparer la température mesurée à la température de consigne.
   - Afficher sur le module LCD:
      - La température de consigne, préfixée par "Set: ".
      - La température mesurée préfixée par "Ambient: ".
   - Contrôle:
      - Si la Température mesurée est supérieure à la température de consigne:
         - La LED bat à une fréquence de 0.5 Hz.
      - Si la température mesurée est supérieure de 3 degrés à la température de consignes:
         - Le buzzer sonne.
         - La LED clignote plus rapidement.
         - Le mot "ALARM" apparait sur l'écran LCD.

## Bonus:
- Afficher un battement progressif (dimmer) de la LED.
- Faire clignoter le mot "ALARM" à l'écran.
- Faire défiler le mot "ALARM" sur l'écran.

#Code: 

Je commence par importer les différentes librairies nécessaires pour le fonctionnement des modules, et je définis les noms des modules au bonnes pins du rapsberry
```
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
```

Je continue ensuite par définir les fonctions dans ce cas-ci (VERT, JAUNE et ALARME).
```
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
```
La fonction Jaune diffère de la VERT car cette dernière allume la LED à 0.5Hz. Je termine avec la fonction ALARME qui elle allume la LED à 0.1Hz et allume le buzzer. 
```
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
```
Le Loop est assez simple, "y" est la conversion linéaire du potentiomètre pour afficher une température sur l'écran LCD de 15°C à 35°C. Trois conditions pour la température, <= à la température mesurée la fonction VERT() est appelée, sinon si la température est 3° supérieur la fonction Jaune() est appelée, et pour finir le dernier cas si la température dépasse les 3°C par rapport à la température ambiante la fonction ALARME() est appelée. 
```
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
```



