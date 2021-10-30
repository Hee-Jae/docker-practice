from flask import Blueprint

bp = Blueprint('bp', __name__, url_prefix='/')

@bp.route('', methods=['GET'])
def home():
  return "Hello"