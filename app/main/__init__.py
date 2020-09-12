from flask import Blueprint


main = Blueprint(name='main', import_name=__name__, url_prefix='/')

from . import views, errors
