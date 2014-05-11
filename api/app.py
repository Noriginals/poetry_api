from flask import Flask
from flask_wtf.csrf import CsrfProtect

# Flask Initialization
app = Flask(__name__)
app.config.from_object('config')

# CSRF Protection
csrf = CsrfProtect()
csrf.init_app(app)
