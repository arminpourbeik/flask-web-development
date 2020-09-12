from flask import Blueprint

auth = Blueprint(name='auth', import_name=__name__)

from . import views
