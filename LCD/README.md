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

