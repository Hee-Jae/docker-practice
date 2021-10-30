from flask import Flask
from view import bp

def create_app():
  app = Flask(__name__)
  
  app.register_blueprint(bp)
  app.secret_key = 'secret-key'
  
  return app

if __name__ == '__main__':
  create_app().run(host='0.0.0.0')