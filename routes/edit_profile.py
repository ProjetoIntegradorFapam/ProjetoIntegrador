#importando bibliotecas, frameworks e microframeworks
from flask import Blueprint, render_template

#instanciando "home" utilizando Blueprint (É OBRIGRATÓRIO utilizar "__name__" após o nome da view, ou seja, rota.)
bp = Blueprint('edit_profile', __name__)