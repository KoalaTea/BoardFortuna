from flask import render_template, request
from forms import DominionForm
from app import app
from dominion import dominion as d
import random

@app.route('/')
def index():
    sets = [i for i in d.dominion]
    form = DominionForm()
    return render_template("dominion.html", form = form, endpoint='http://localhost:5000/dominion/game')

@app.route('/dominion/game', methods=['POST'])
def dominion_game():

    # Get data from the form
    postdata = dict(request.form)
    print postdata
    num_players = int(postdata['num_players'][0])
    expansions = postdata.keys()
    expansions.remove('num_players')

    # Get all available cards from the chosen expansions
    available_cards = []
    for expansion in expansions:
        if postdata[expansion][0] == 'y' and d.has_key(expansion):
            for card in d[expansion]:
                available_cards.append((expansion, card))
    print available_cards

    # Pick a random first player
    first_player = random.randint(1, num_players)
    print first_player

    # Pick random card locations and add it to a set so that there can be no
    # duplicates, then copy the cards chosen to the final set
    cards_chosen = set()
    while len(cards_chosen) < 10:
        cards_chosen.add(random.randint(0, len(available_cards)-1))
    print cards_chosen
    final_set = []
    for loc in cards_chosen:
        final_set.append(available_cards[loc])
    print final_set

    # Return template of the game
    return render_template("dominion_game.html", cards=final_set, first_player=first_player)
