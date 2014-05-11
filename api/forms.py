from flask_wtf import Form
from wtforms import TextField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired, NumberRange

import constants

class PoetrySearchForm(Form):
    styles = SelectField('Poetry Styles', choices=constants.POETRY_STYLES)
    topics = SelectField('Topics', choices=constants.TOPICS)
