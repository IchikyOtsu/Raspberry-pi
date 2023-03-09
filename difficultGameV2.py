from flask import Flask, render_template_string
from flask import request
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
EASY = 1.5  # LED remains on for 1.5 seconds
MEDIUM = 1.0  # LED remains on for 1.0 second
HARD = 0.5  # LED remains on for 0.5 seconds
# Fonction pour activer une LED
def activate_led(pin):
    GPIO.output(pin, GPIO.HIGH)

# Fonction pour désactiver une LED
def deactivate_led(pin):
    GPIO.output(pin, GPIO.LOW)

# Fonction pour jouer une partie
# Fonction pour jouer une partie
def play_game(base_difficulty):
    global score
    global game_over
    difficulty = base_difficulty
    previous_led_pin = None
    while not game_over:
        # Choisir une LED au hasard qui n'est pas la même que la précédente
        led_pin = random.choice([p for p in led_pins if p != previous_led_pin])
        previous_led_pin = led_pin

        activate_led(led_pin)
        time.sleep(difficulty)
        deactivate_led(led_pin)
        if GPIO.input(button_pins[led_pins.index(led_pin)]) == GPIO.LOW:
            score += 1
            # Augmenter la difficulté toutes les 5 secondes
            if score % 5 == 0:
                difficulty *= 1.1
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
    html = """
    <html>
        <head>
            <title>Sélectionner le niveau de difficulté</title>
        </head>
        <body>
            <h1>Sélectionner le niveau de difficulté :</h1>
            <form action="/game" method="get">
                <input type="radio" id="easy" name="difficulty" value="easy" checked>
                <label for="easy">Facile</label><br>
                <input type="radio" id="medium" name="difficulty" value="medium">
                <label for="medium">Moyen</label><br>
                <input type="radio" id="hard" name="difficulty" value="hard">
                <label for="hard">Difficile</label><br>
                <button type="submit">Commencer une partie</button>
            </form>
        </body>
    </html>
    """
    return render_template_string(html)

@app.route("/game")
def game():
    global score
    global game_over
    score = 0
    game_over = False
    difficulty = request.args.get('difficulty')
    if difficulty == 'easy':
        base_difficulty = EASY
    elif difficulty == 'medium':
        base_difficulty = MEDIUM
    elif difficulty == 'hard':
        base_difficulty = HARD
    play_game(base_difficulty)
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

