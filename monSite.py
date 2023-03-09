from flask import Flask, render_template_string
import RPi.GPIO as GPIO
import time
import random

app = Flask(__name__)

# Configuration des broches pour les LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pins = [18, 23, 24]
GPIO.setup(led_pins, GPIO.OUT)

# Configuration des broches pour les boutons
button_pins = [4, 17, 27]
GPIO.setup(button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables du jeu
score = 0
game_over = False

# Fonction pour activer une LED
def activate_led(pin):
    GPIO.output(pin, GPIO.HIGH)

# Fonction pour désactiver une LED
def deactivate_led(pin):
    GPIO.output(pin, GPIO.LOW)

# Fonction pour jouer une partie
def play_game():
    global score
    global game_over
    while not game_over:
        led_pin = random.choice(led_pins)
        activate_led(led_pin)
        time.sleep(1.5)
        deactivate_led(led_pin)
        if GPIO.input(button_pins[led_pins.index(led_pin)]) == GPIO.LOW:
            score += 1
        else:
            game_over = True

# Route pour la page d'accueil
@app.route("/")
def home():
    html = """
    <html>
        <head>
            <title>Jeu de LEDs et de boutons</title>
        </head>
        <body>
            <h1>Bienvenue dans le jeu de LEDs et de boutons !</h1>
            <p>Cliquez sur le bouton ci-dessous pour commencer une partie.</p>
            <form action="/play" method="get">
                <button type="submit">Commencer une partie</button>
            </form>
        </body>
    </html>
    """
    return render_template_string(html)

# Route pour commencer une partie
@app.route("/play")
def play():
    global score
    global game_over
    score = 0
    game_over = False
    play_game()
    html = """
    <html>
        <head>
            <title>Résultat</title>
        </head>
        <body>
            <h1>Partie terminée !</h1>
            <p>Votre score est de {{ score }}.</p>
            <p>Cliquez sur le bouton ci-dessous pour revenir à la page d'accueil.</p>
            <form action="/" method="get">
                <button type="submit">Retour à l'accueil</button>
            </form>
        </body>
    </html>
    """
    return render_template_string(html, score=score)
