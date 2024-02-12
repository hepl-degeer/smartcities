# GPIO 

## Exercice 1 : Clignotement de la Led avec un bouton poussoir
## Objectif : 
Créer un programme MicroPython qui permet de faire clignoter une LED à différentes vitesses en fonction du nombre de pressions sur un bouton poussoir.
## Matériel : 
- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module LED
- Module bouton poussoir
- Câbles
## Consignes : 
1. Branchez la LED et le bouton poussoir au microcontrôleur
2. Ecrivez un programme MicroPython qui répond aux exigences suivantes :
   - La LED doit clignoter à l'infini avec une fréquence de 0.5 Hz lorsque le bouton poussoir est pressé une fois.
   - La LED doit clignoter plus vite lorsque le bouton poussoir est préssé une second fois.
   - La LED doit s'éteindre lorsque le bouton poussoir est pressé une troisième fois
3. Testez votre programme et vérifiez qu'il fonctionne correctement

## Bonus : 
- Ajoutez un délai ou un effet dans les clignotements de la LED ou dans le passage d'une vitesse de clignotement à une autre
- Modifiez le nombre d'appuis nécessaires pour changer la vitesse de clignotement.

# Code : 

Le début du code est simple on importe les librairies et je définis un bouton sur la pin 16 et une LED sur la pin 16
```
import machine
import utime

button = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(18,machine.Pin.OUT)

val = 0
LED_state = 0
flag = 0

```
Avant de commencer le loop je définis une fonction d'interruption sur le bouton poussoir,
dans ce cas-ci, si le bouton poussoir passe à l'état haut (Rising) la variable global Flag passe à 1
```
def callback(button):
    global flag
    flag = 1
    
button.irq(trigger=button.IRQ_RISING, handler=callback)

```
Le loop consiste en 4 conditions if, la première est si le bouton poussoir est appuyé il déclenche le flag et est incrémenté à 1. Dans ce cas val vaut 1 et la LED clignote toutes les demi-secondes. 
La variable flag est directement remise à zéro.
```
while True:
    
    if flag == 1:
        val = val + 1
        flag = 0
    if val == 1:
        LED.value(1)
        utime.sleep(0.5)
        LED.value(0)
        utime.sleep(0.5)
```
![IMG_7771](https://github.com/hepl-degeer/smartcities/assets/159243839/c23f9115-694e-42b1-999a-d73a95929a50)

Si on appuie une deuxième fois sur le bouton le flag incrémente val à 2 et là, la LED clignote plus vite
```
    if val == 2:
        LED.value(1)
        utime.sleep(0.1)
        LED.value(0)
        utime.sleep(0.1)
```
![IMG_7772](https://github.com/hepl-degeer/smartcities/assets/159243839/e9a7e7fa-a7d6-498d-9188-3450c21b58c0)

Si on appuie une troisième et dernière fois sur le bouton, le flag incrémente val à 3 et éteint complètement la LED et réinitialise val à zéro. On peut réappuyer sur le bouton pour recommencer le cycle de la LED (Lent-vite-éteint).
```
    if val == 3:
        LED.value(0)
        val = 0
        utime.sleep(1)

```
![IMG_7773](https://github.com/hepl-degeer/smartcities/assets/159243839/6e45608d-44a0-43ed-8cfc-d30cbd261bb9)


# Remarque : 
L'utilisation d'une fonction d'interruption permet un changement à n'importe quel moment dans le code, sans l'interruption le changement était plus aléatoire et on devait appuyer à un timing très précis.
  
    
