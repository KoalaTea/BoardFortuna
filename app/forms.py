from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField

class DominionForm(FlaskForm):
    class Meta:
        csrf = False
    base = BooleanField("base")
    base_1 = BooleanField("base 1st edition")
    base_2 = BooleanField("base 2nd edition")
    dark_ages = BooleanField("dark ages")
    seaside = BooleanField("seaside")
    prosperity = BooleanField("prosperity")
    guilds = BooleanField("guilds")
    cornucopia = BooleanField("cornucopia")
    num_players = SelectField("num_players", choices=[(2,'2'),(3,'3'),(4,'4')])
