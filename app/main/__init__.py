from flask import Blueprint
from ..models.user import Permission


main = Blueprint(name='main', import_name=__name__, url_prefix='/')

from . import views, errors


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
