from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# Création d'une instance de TonalBuzzer sur la broche 21
buzzer = TonalBuzzer(21)

# Jouer les notes de la mélodie
buzzer.play(Tone("C5"))
sleep(0.5)
buzzer.play(Tone("C5"))
sleep(0.5)
buzzer.play(Tone("G5"))
sleep(0.5)
buzzer.play(Tone("G5"))
sleep(0.5)
buzzer.play(Tone("A5"))
sleep(0.5)
buzzer.play(Tone("A5"))
sleep(0.5)
buzzer.play(Tone("G5"))
sleep(1)
buzzer.play(Tone("F5"))
sleep(0.5)
buzzer.play(Tone("F5"))
sleep(0.5)
buzzer.play(Tone("E5"))
sleep(0.5)
buzzer.play(Tone("E5"))
sleep(0.5)
buzzer.play(Tone("D5"))
sleep(0.5)
buzzer.play(Tone("D5"))
sleep(0.5)
buzzer.play(Tone("C5"))
sleep(1)

# Arrêter le buzzer
buzzer.stop()




    



