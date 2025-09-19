from flask import Flask, request, render_template
from backend.models.pokemon import Pokemon

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    pokemon_data = None

    if request.method == 'POST':
        identifier = request.form.get('identifier')
        poke = Pokemon(identifier)
        pokemon_data = poke

    return render_template('index.html', pokemon=pokemon_data)