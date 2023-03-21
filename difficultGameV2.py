from flask import Flask, render_template_string
from flask import request
import RPi.GPIO as GPIO
import time
import random

app = Flask(__name__)

# Configuration des broches pour les LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pins = [26, 13, 5]
GPIO.setup(led_pins, GPIO.OUT)

# Configuration des broches pour les boutons
button_pins = [19, 6, 7]
GPIO.setup(button_pins, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables du jeu
score = 0
game_over = False
EASY = 2.0  # La LED reste allumée pendant 1,5 seconde
MEDIUM = 1.5  # La LED reste allumée pendant 1,0 seconde
HARD = 1.0  # La LED reste allumée pendant 0,5 seconde
SPEED_INCREASE = 0.02 # Augmentation de la vitesse des LED par incrément de score

# Fonction pour activer une LED
def activate_led(pin):
    GPIO.output(pin, GPIO.HIGH)

# Fonction pour désactiver une LED
def deactivate_led(pin):
    GPIO.output(pin, GPIO.LOW)

# Fonction pour jouer une partie
def play_game(base_difficulty):
    global score
    global game_over
    difficulty = base_difficulty
    prev_led = -1  # valeur initiale de l'indice LED précédent
    while not game_over:
        led_pin = random.choice([x for x in led_pins if x != prev_led])  # Choisissez une LED au hasard qui n'était pas allumée auparavant
        prev_led = led_pin  # Stocker la LED actuelle en tant que LED précédente
        activate_led(led_pin)
        time.sleep(difficulty)
        deactivate_led(led_pin)
        button_pin = request_button()  # Obtenir le pin du bouton qui a été pressé
        if button_pin is not None:
            button_index = button_pins.index(button_pin)  # Obtenir l'index du bouton qui a été pressé
            if button_index != led_pins.index(led_pin):
                game_over = True
            else:
                score += 1
                difficulty -= SPEED_INCREASE  # Augmenter la vitesse des LED
                if difficulty < HARD:  # Vitesse minimale des DEL
                    difficulty = HARD
        else:
            game_over = True

# Fonction pour récupérer le pin du bouton qui a été pressé
def request_button():
    for button_pin in button_pins:
        if GPIO.input(button_pin) == GPIO.LOW:
            return button_pin
    return None

# Route pour la page d'accueil
@app.route("/")
def home():
    html = """
    <html>
        <head>
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

