from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# Configuration du buzzer
buzzer = TonalBuzzer(21)

# Définition des notes
#C4 = Tone(261.63) # Do
#D4 = Tone(293.66) # Ré
#E4 = Tone(329.63) # Mi
#F4 = Tone(349.23) # Fa
#G4 = Tone(392.00) # Sol
#A4 = Tone(440.00) # La
#B4 = Tone(493.88) # Si
#C5 = Tone(523.25) # Do

# Jouer la mélodie
buzzer.play(Tone("G4"))
sleep(0.25)
buzzer.play(Tone("G4"))
sleep(0.25)
buzzer.play(Tone("G4"))
sleep(0.25)
buzzer.play(Tone("G4"))
sleep(0.25)
#2
buzzer.play(Tone("E4"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
#3
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("B3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)
#4
buzzer.play(Tone("F3"))
sleep(0.25)
buzzer.play(Tone("F3"))
sleep(0.25)
buzzer.play(Tone("E3"))
sleep(0.25)
buzzer.play(Tone("F3"))
sleep(0.25)
#5
buzzer.play(Tone("G3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)
buzzer.play(Tone("E3"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
#6
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("B3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)
#7
buzzer.play(Tone("G3"))
sleep(0.25)
buzzer.play(Tone("E3"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
#8
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("B3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)
#9
buzzer.play(Tone("F3"))
sleep(0.25)
buzzer.play(Tone("F3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
#10
buzzer.play(Tone("G3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("F3"))
sleep(0.25)
buzzer.play(Tone("E3"))
sleep(0.25)
#11
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("C4"))
sleep(0.25)
buzzer.play(Tone("B3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
#12
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("B3"))
sleep(0.25)
buzzer.play(Tone("A3"))
sleep(0.25)
buzzer.play(Tone("G3"))
sleep(0.25)

# Arrêt de la mélodie
buzzer.stop()
