from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# Création d'une instance de TonalBuzzer sur la broche 21
buzzer = TonalBuzzer(21)

# Jouer les notes de la mélodie
buzzer.play(Tone("E4"))
sleep(0.5)
buzzer.play(Tone("F#4"))
sleep(0.5)
buzzer.play(Tone("G4"))
sleep(0.5)
buzzer.play(Tone("A4"))
sleep(0.5)
buzzer.play(Tone("B4"))
sleep(0.5)
buzzer.play(Tone("A4"))
sleep(0.5)
buzzer.play(Tone("G4"))
sleep(0.5)
buzzer.play(Tone("F#4"))
sleep(1)

# Arrêter le buzzer
buzzer.stop()
