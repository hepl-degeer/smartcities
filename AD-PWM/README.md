# Exercice 2: Volume d'une mélodie
## Objectif: 
Créer un programme MicroPython qui permet de gérer le volume d'une mélodie jouée sur un buzzer. Le volume est contrôlé par un potentiomètre.
## Matériel:
- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module potentiomètre
- Buzzer
- Câbles
## Consignes:
1. Branchez le buzzer et le potentiomètre au microcontrôleur
2. Ecrivez un programme MicroPython qui répond aux exigences suivantes:
   - Une mélodie (au choix, soyez créatif) est jouée en boucle.
   - Le faite de changer le potentiomètre modifie directement le volume de la mélodie
3. Testez votre programme et vérifiez qu'il fonctionne correctement.

## Bonus:
- Ajoutez un bouton poussoir qui permet de changer de mélodie.
- Ajouter une LED qui clignote au rythme de la mélodie.

# Code:
## Setup:
Je définis les entrées et sorties, le buzzer (en PWM) auquel le volume est réglé sur la valeur par défaut (1000)
et on termine avec le potentiomètre en entrée analogique.
```
button = machine.Pin(18,machine.Pin.IN)
buzzer = PWM(Pin(27))
pot = ADC(0)
vol=1000
```
Je crée les fonctions pour chaque note de la mélodie (DO, RE, MI, FA, SO, LA, SI) avec leurs fréquences respectives. Dans le code ci-dessous, seulement DO et RE
sont montrés comme exemple. 
La particularité dans ce cas-ci est que chaque note possède la fonction volume() qui permet de régler le volume grâce au potentiomètre n'importe où dans le code.
```
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
```
## Loop:
Le While True possède les différentes notes qui composent la mélodie avec un delai entre chaque pour le rythme de la mélodie. 
```
while True:


    do()
    utime.sleep(0.25)
    re()
    utime.sleep(0.25)
    mi()
    utime.sleep(0.25)
    N()
    utime.sleep(0.01)
```
Remarque : Les Bonus ne sont présents dans le code. 

#Vidéo démonstration:

https://github.com/hepl-degeer/smartcities/assets/159243839/8d2d4701-4cd8-415c-a182-ea7aaae0dacd






    

